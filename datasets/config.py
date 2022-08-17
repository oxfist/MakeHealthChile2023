import os
import pandas as pd

#########################
# Common parameters
#########################

keywords = list(pd.read_csv(os.path.join("datasets", "keywords.csv"),
                            encoding='latin')["Keywords"])

#########################
# Media Cloud parameters
#########################

# TO COMPLETE
login_info = {"mc_session": "4264de9e-fd8e-4133-a30e-57153b67a5ea",
              "mc_remember_token": "8d6ecada0cc37b8bbfaf4e353df926b3e4652dc56efa6a7a5a15f0dacbc6129c|7d45dcee9a8b3d5fad5e39e5c4b32bf84074dd85dcc6d7f1751dd1f9d4f416aee6a908f6f2d07d266907f45284e63db997dd2c53a3cdec2767f4a68a7792783b"}

# Only latam
df_tags_country_latam = pd.read_csv(os.path.join("datasets",
                                                 "collections_country_latam.csv"))
df_tags_country_latam.index = df_tags_country_latam["Country name"]
collections_dic = df_tags_country_latam.to_dict()["tags_id"]
collections = list(collections_dic.keys())

"""
# World
df_tags_country = pd.read_csv(os.path.join("datasets",
                                           "collections_country.csv"))
df_tags_country.index = df_tags_country["Country name"]
collections_dic = df_tags_country.to_dict()["tags_id"]
collections = list(collections_dic.keys())
"""

start_date = '2020-01-01'
end_date = '2022-08-15'


#########################
# Google Trends parameters
#########################

start_year = 2020
start_mon = 1
stop_year = 2022
stop_mon = 7

# Only latam
df_tags_country_latam = pd.read_csv(os.path.join("datasets",
                                                 "collections_country_latam.csv"))
df_tags_country_latam.index = df_tags_country_latam["Country name"]
countries = list(df_tags_country_latam["Country name"])
iso_dic = df_tags_country_latam.to_dict()["ISO 3166 ALPHA-2"]

"""
# World
df_tags_country = pd.read_csv(os.path.join("datasets",
                                           "collections_country.csv"))
df_tags_country.index = df_tags_country["Country name"]
countries = list(df_tags_country["Country name"])
iso_dic = df_tags_country.to_dict()["ISO 3166 ALPHA-2"]
"""

# TO COMPLETE
headers = {}
