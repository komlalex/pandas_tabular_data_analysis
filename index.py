"""Reading a CSV file using Pandas 
Pandas is typically used for working with tabular data (similar to the data stored 
in a spreadsheet). Pandas provides helper functions to read data from various
file formats like CSV, Excel spreadsheets, HTML tables, JSON, SQL and more. 
Let's download a file italy-covid-daywise.csv which contains daywise Covid-19 data for
Italy in the following format: 

data,new_cases_new_deaths,new_tests
2020-04-21,2256.0,454.0,28095.0
2020-04-22,2729.0,534.0,44248.0 
...

This format of storing data is known as comma-separated values or CSV. 
"""
"""Download data"""
from urllib import request  
import os 
import pandas as pd
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'
italy_covid_path = "./data/italy-covid-daywise.csv"

def download_data(url, path):
    if os.path.exists(path):
        print("File already exists. Skipping download.") 

    else: 
        request.urlretrieve(url, path)
        print(f"Donwload complete.") 

download_data(italy_covid_url, italy_covid_path) 

covid_df = pd.read_csv(italy_covid_path) 
print(covid_df.tail())

