# MakeHealthChile2023

## Datasets

New Media Cloud and GoogleTrends data can be downloaded using the scripts ```generate_mediacloud.py``` and ```generate_googletrends.py```, located inside the folder **datasets**.

You can find a list of countries in the excel files *collections_country.csv* and *collections_country_latam.csv* (specific for Latin America).

Before running the scripts:

- To fetch data for specific keywords, modify the keyword list in the file *keywords.csv*.

- Change the configuration file ```config.py``` (instructions below)

```config.py``` allows one to change the list of countries, the timeframe, and the keywords for data retrieval.

For Media Cloud data, the dictionnary entitled ```login_info``` needs to be modified. To do so, connect to your [Media Cloud](https://mediacloud.org/) account and open the *Explorer tool*. Inspect the webpage and go to the *Network* tab. After making a query, click on *split-count*. On the right, in *Request Headers* and *cookie*, retrieve the ```mc_remember_token``` and ```mc_session``` values and insert them into ```config.py```.

![mediacloud](https://raw.githubusercontent.com/covasquezv/MakeHealthChile2023/master/images/mediacloud.png)

For Google Trends data, the ```header``` dictionnary must be updated. First, visit the [Google Trends website](https://trends.google.com/trends/?geo=US), inspect the webpage and go to the *Network* tab. After making a query, right click on explore, and click on *Copy as cURL (bash)*. Convert the command into a Python request using [curlconverter](https://curlconverter.com/). Retrieve only the ```header``` dictionnary.

![googletrends](https://raw.githubusercontent.com/covasquezv/MakeHealthChile2023/master/images/ggtrends.png)

## FALP dataset exploration

Scripts used to explore the FALP dataset are located at ``challenge_datasets/FALP/scripts``. A little description of the contents is shown below:

- ``explore_dataset.ipynb``: dataset characterization in terms of patients, cancer categories, and main diagnostic variables.
- ``cluster_analysis.ipynb``: kmeans clustering to explore possible relations between clusters and target variables.
- ``falp_preprocessing.py``: module with a class to standardize the raw dataset.
- ``get_dataset_summary.py``: script to generate a JSON file containing a summary of the FALP dataset.
- ``measure_dataset_quality.py``: script to measure the quality of the FALP dataset in terms of missing and unallowed values.
