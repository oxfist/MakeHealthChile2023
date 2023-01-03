import requests
import os
import pandas as pd
from tqdm import tqdm
from typing import Dict, List

from config import (
    login_info,
    collections,
    keywords,
    start_date,
    end_date,
    collections_dic,
)


def get_media_cloud(
    login_info: Dict[str, str],
    collection_id: str,
    keyword: str,
    start_date: str,
    end_date: str,
) -> pd.DataFrame:
    """
    Collect Media Cloud data for a single collection id and a keyword

    Args:
        login_info (Dict[str, str]): cookies information
        collection_id (str): id of the collection on Media Cloud
        keyword (str): count media that contains this particular keyword
        start_date (str): YYYY-MM-DD format
        end_date (str): YYYY-MM-DD format

    Returns:
        pd.DataFrame: count, total_count and ratio over time for
            this collection and the given keyword
    """
    # cookies to log in
    cookies = {
        "_ga": "GA1.2.177331258.1652802621",
        "mc_session": login_info["mc_session"],
        "mc_remember_token": login_info["mc_remember_token"],
        "_gid": "GA1.2.1810614096.1660231096",
        "_gat": "1",
    }

    # headers
    headers = {
        "authority": "explorer.mediacloud.org",
        "accept": "*/*",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryRiANxqFYJ2WYTaHP",
        "origin": "https://explorer.mediacloud.org",
        "referer": "https://explorer.mediacloud.org/",
        "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }

    # data post request
    data = f'------WebKitFormBoundaryRiANxqFYJ2WYTaHP\r\nContent-Disposition: form-data; name="start_date"\r\n\r\n{start_date}\r\n------WebKitFormBoundaryRiANxqFYJ2WYTaHP\r\nContent-Disposition: form-data; name="end_date"\r\n\r\n{end_date}\r\n------WebKitFormBoundaryRiANxqFYJ2WYTaHP\r\nContent-Disposition: form-data; name="q"\r\n\r\n{keyword}\r\n------WebKitFormBoundaryRiANxqFYJ2WYTaHP\r\nContent-Disposition: form-data; name="uid"\r\n\r\n346f2268-bae8-4e12-a4b8-dec1d0824e9c\r\n------WebKitFormBoundaryRiANxqFYJ2WYTaHP\r\nContent-Disposition: form-data; name="sources"\r\n\r\n\r\n------WebKitFormBoundaryRiANxqFYJ2WYTaHP\r\nContent-Disposition: form-data; name="collections"\r\n\r\n{collection_id}\r\n------WebKitFormBoundaryRiANxqFYJ2WYTaHP\r\nContent-Disposition: form-data; name="searches"\r\n\r\n\r\n------WebKitFormBoundaryRiANxqFYJ2WYTaHP--\r\n'

    # get content from the webpage
    response = requests.post(
        "https://explorer.mediacloud.org/api/explorer/stories/split-count",
        cookies=cookies,
        headers=headers,
        data=data,
    )

    # convert to dataframe format
    df = pd.DataFrame.from_records(response.json()["results"]["counts"])
    df.set_index("date", inplace=True)  # date as index
    df.index = pd.to_datetime(df.index)  # datetime format
    return df


def get_media_cloud_aggregate(
    login_info: Dict[str, str],
    collections: List[str],
    keyword: str,
    start_date: str,
    end_date: str,
    collections_dic: Dict[str, str],
) -> pd.DataFrame:
    """
    Collect Media Cloud data for multiple collections
    and a keyword. Aggregate the data and return the results.

    Args:
        login_info (Dict[str, str]): cookies information
        collections (List[str]): id of the collection on Media Cloud
        keyword (str): count media that contains this particular keyword
        start_date (str): YYYY-MM-DD format
        end_date (str): YYYY-MM-DD format
        collections_dic (Dict[str, str]): Dictionnary that map collections
            as a string format to their corresponding Media Cloud
            collection id (e.g. "France": "34412146").

    Returns:
        pd.DataFrame: count, total_count and ratio over time for
            all the collections and the given keyword
    """
    df = None
    for collection in collections:
        collection_id = collections_dic[collection]
        sub_df = get_media_cloud(
            login_info, collection_id, keyword, start_date, end_date
        )
        # add collection name
        sub_df.columns = [c + f"_{collection}" for c in sub_df.columns]
        if df is None:  # first dataframe is the first collection
            df = sub_df.copy(deep=True)
        else:
            df = df.join(sub_df)  # join
    # save
    df.to_csv(os.path.join("datasets", "mediacloud", f"{keyword}.csv"),
              index=True)
    return df


def create_media_cloud_data(
    login_info: Dict[str, str],
    collections: List[str],
    keywords: List[str],
    start_date: str,
    end_date: str,
    collections_dic: Dict[str, str],
) -> None:
    """
    Collect Media Cloud data for multiple collections and multiple keywords.
    Aggregate the data for each keyword and save the results.

    Args:
        login_info (Dict[str, str]): cookies information
        collections (List[str]): id of the collection on Media Cloud
        keywords (List[str]): list of keywords to process
        start_date (str): YYYY-MM-DD format
        end_date (str): YYYY-MM-DD format
        collections_dic (Dict[str, str]): Dictionnary that map collections
            as a string format to their corresponding Media Cloud
            collection id (e.g. "France": "34412146").
    """
    for i in tqdm(range(len(keywords))):
        keyword = keywords[i]
        print(keyword)
        get_media_cloud_aggregate(
            login_info, collections, keyword, start_date, end_date, collections_dic
        )


if __name__ == "__main__":
    create_media_cloud_data(
        login_info, collections, keywords, start_date, end_date, collections_dic
    )
