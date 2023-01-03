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
login_info = {"mc_session": "",
              "mc_remember_token": ""}

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
