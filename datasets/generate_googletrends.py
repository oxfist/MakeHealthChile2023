import os
import pandas as pd

from datetime import date, timedelta
from functools import partial
from time import sleep
from calendar import monthrange
from typing import Dict, List
from tqdm import tqdm
from pytrends.exceptions import ResponseError
from pytrends.request import TrendReq as UTrendReq

from config import (
    keywords,
    start_year,
    start_mon,
    stop_year,
    stop_mon,
    countries,
    iso_dic,
    headers,
)

GET_METHOD = "get"


class TrendReq(UTrendReq):
    """
    Child class of pytrends' TrendReq
    This allows to change the header to avoid 429 errors

    Source: https://stackoverflow.com/questions/50571317/pytrends-the-request-failed-google-returned-a-response-with-code-429

    Args:
        UTrendReq (TrendReq): native TrendReq object from pytrends
    """

    def _get_data(self, url, method=GET_METHOD, trim_chars=0, **kwargs):
        return super()._get_data(
            url, method=GET_METHOD, trim_chars=trim_chars, headers=headers,
            **kwargs
        )


def get_last_date_of_month(year: int, month: int) -> date:
    """
    Given a year and a month returns an instance of the date class
    containing the last day of the corresponding month.

    Source: https://stackoverflow.com/questions/42950/get-last-day-of-the-month-in-python

    Args:
        year (int): year
        month (int): month

    Returns:
        date: last day of the month
    """

    return date(year, month, monthrange(year, month)[1])


def convert_dates_to_timeframe(start: date, stop: date) -> str:
    """
    Given two dates, returns a stringified version of the interval between
    the two dates which is used to retrieve data for a specific time frame
    from Google Trends.

    Args:
        start (date): start date datetime format
        stop (date): stop date datetime format

    Returns:
        str: combination of the two dates in Y-M-D format
    """
    return f"{start.strftime('%Y-%m-%d')} {stop.strftime('%Y-%m-%d')}"


def _fetch_data(pytrends, build_payload, timeframe: str) -> pd.DataFrame:
    """
    Attempts to fecth data and retries in case of a ResponseError.

    Args:
        pytrends (TrendReq): TrendReq pytrends object with a _get_data
            method
        build_payload (build_payload): build_payload pytrends object loaded on
            a set of keywords
        timeframe (str): google trends timeframe format to fetch data

    Returns:
        pd.DataFrame: interest over time
    """
    attempts, fetched = 0, False
    while not fetched:
        try:
            build_payload(timeframe=timeframe)
        except ResponseError as err:
            print(err)
            print(f"Trying again in {60 + 5 * attempts} seconds.")
            sleep(60 + 5 * attempts)
            attempts += 1
            if attempts > 3:
                print("Failed after 3 attemps, abort fetching.")
                break
        else:
            fetched = True
    return pytrends.interest_over_time()


def get_daily_data(
    word: str,
    start_year: int,
    start_mon: int,
    stop_year: int,
    stop_mon: int,
    geo: str = "US",
    verbose: bool = True,
    wait_time: float = 5.0,
) -> pd.DataFrame:
    """
    Given a word, fetches daily search volume data from Google Trends and
    returns results in a pandas DataFrame.
    Details: Due to the way Google Trends scales and returns data, special
    care needs to be taken to make the daily data comparable over different
    months. To do that, we download daily data on a month by month basis,
    and also monthly data. The monthly data is downloaded in one go, so that
    the monthly values are comparable amongst themselves and can be used to
    scale the daily data. The daily data is scaled by multiplying the daily
    value by the monthly search volume divided by 100.

    For a more detailed explanation see http://bit.ly/trendsscaling

    Args:
        word (str): Word to fetch daily data for.
        start_year (int): the start year
        start_mon (int): start 1st day of the month
        stop_year (int): the end year
        stop_mon (int): end at the last day of the month
        geo (str): geolocation
        verbose (bool): If True, then prints the word and current time frame
            we are fecthing the data for.
    Returns:
        complete (pd.DataFrame): Contains 4 columns.
            The column named after the word argument contains the daily search
            volume already scaled and comparable through time.
            The column f'{word}_unscaled' is the original daily data fetched
            month by month, and it is not comparable across different months
            (but is comparable within a month).
            The column f'{word}_monthly' contains the original monthly data
            fetched at once. The values in this column have been backfilled
            so that there are no NaN present.
            The column 'scale' contains the scale used to obtain the scaled
            daily data.
    """
    # Set up start and stop dates
    start_date = date(start_year, start_mon, 1)
    stop_date = get_last_date_of_month(stop_year, stop_mon)

    # Start pytrends for US region
    pytrends = TrendReq()
    # Initialize build_payload with the word we need data for
    build_payload = partial(
        pytrends.build_payload, kw_list=[word], cat=0, geo=geo, gprop=""
    )

    # Obtain monthly data for all months in years [start_year, stop_year]
    monthly = _fetch_data(
        pytrends, build_payload, convert_dates_to_timeframe(start_date,
                                                            stop_date)
    )

    # Get daily data, month by month
    results = {}
    # if a timeout or too many requests error occur we need to adjust wait time
    current = start_date
    while current < stop_date:
        last_date_of_month = get_last_date_of_month(current.year,
                                                    current.month)
        timeframe = convert_dates_to_timeframe(current, last_date_of_month)
        if verbose:
            print(f"{word}:{timeframe}")
        results[current] = _fetch_data(pytrends, build_payload, timeframe)
        current = last_date_of_month + timedelta(days=1)
        sleep(wait_time)  # don't go too fast or Google will send 429s

    daily = pd.concat(results.values()).drop(columns=["isPartial"])
    complete = daily.join(monthly, lsuffix="_unscaled", rsuffix="_monthly")

    # Scale daily data by monthly weights so the data is comparable
    complete[f"{word}_monthly"].ffill(inplace=True)  # fill NaN values
    complete["scale"] = complete[f"{word}_monthly"] / 100
    complete[word] = complete[f"{word}_unscaled"] * complete.scale

    return complete


def extract_country_list(
    keyword: str,
    start_year: int,
    start_mon: int,
    stop_year: int,
    stop_mon: int,
    countries: List[str],
    iso_dic: Dict[str, str],
) -> pd.DataFrame:
    """
    Extract and merge daily and monthly google trends data for different
    countries over a given period with a specific keyword.
    Save intermediate results for each combination of keyword / country.

    Args:
        keyword (str): Word to fetch daily data for.
        start_year (int): the start year
        start_mon (int): start 1st day of the month
        stop_year (int): the end year
        stop_mon (int): end at the last day of the month
        countries (List[str]): list of countries we want to
            fetch data for
        iso_dic (Dict[str, str]): Dictionnary that map country names
            to their corresponding two letters ISO code
            (e.g. "France": "FR")

    Returns:
        pd.DataFrame: contains daily and monthly google trends values
            for all the countries and the specific keyword over time.
    """
    res = None
    for i in tqdm(range(len(countries))):
        country = countries[i]
        print(country)
        iso_country = iso_dic[country]
        df = get_daily_data(
            word=keyword,
            start_year=start_year,
            start_mon=start_mon,
            stop_year=stop_year,
            stop_mon=stop_mon,
            geo=iso_country,
            verbose=True,
            wait_time=5.0,
        )
        df = df[[f"{keyword}_unscaled", f"{keyword}_monthly"]]
        df.columns = [country, f"{country}_monthly"]
        if res is None:
            res = df
        else:
            res = res.join(df)
        df.to_csv(os.path.join("datasets", "googletrends",
                               f"{keyword}_{country}.csv"),
                  index=True)
    res.to_csv(os.path.join("datasets", "googletrends",
                            f"{keyword}.csv"),
               index=True)
    return res


def ggtrends_multiple_keywords(
    keywords: List[str],
    start_year: int,
    start_mon: int,
    stop_year: int,
    stop_mon: int,
    countries: List[str],
    iso_dic: Dict[str, str],
) -> None:
    """
    Process multiple keywords to extract multiple google trends data
    over time for a specific set of countries.

    Args:
        keywords (List[str]): Words to fetch daily data for.
        start_year (int): the start year
        start_mon (int): start 1st day of the month
        stop_year (int): the end year
        stop_mon (int): end at the last day of the month
        countries (List[str]): list of countries we want to
            fetch data for
        iso_dic (Dict[str, str]): Dictionnary that map country names
            to their corresponding two letters ISO code
            (e.g. "France": "FR")
    """
    for keyword in keywords:
        _ = extract_country_list(
            keyword, start_year, start_mon, stop_year, stop_mon, countries, iso_dic
        )


if __name__ == "__main__":
    ggtrends_multiple_keywords(
        keywords, start_year, start_mon, stop_year, stop_mon, countries, iso_dic
    )
