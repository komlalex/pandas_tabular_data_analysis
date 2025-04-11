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
import matplotlib.pyplot as plt
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'
italy_covid_path = "./data/italy-covid-daywise.csv"

def download_data(url, path):
    if os.path.exists(path):
        print("File already exists. Skipping download.") 

    else: 
        request.urlretrieve(url, path)
        print(f"Donwload complete.") 

download_data(italy_covid_url, italy_covid_path)  

"""To read this file, we use the .read_csv method from Pandas."""
covid_df = pd.read_csv(italy_covid_path) 

"""Data from the file is read and stored in a DataFrame object - one of the core data 
structures for storing and working with tabular data""" 
#print(type(covid_df)) 

#print(len(covid_df))

"""Here is what we can tell by looking at the data frame: 
1. The file provides four daywise counts for covid-19 in Italy
2. The metrics reparted are new cases, new deaths and new tests 
3. Data is provided for 248 days: Dec 12, 2019 to Sep 3, 2020. 

Keep in mind that these are officially reported numbers, and the actual number of 
cases & deaths may be higher, as not all cases are diagnosed. 
We can view some basic information about the data frame by using the .info method.
"""
#print(covid_df.info()) 

"""It appears that each column contains values of a specific data type. For 
the numeric columns, you can view some statistical information like mean, standard 
deviation, minimum/maximum values of the non-empty values using the .describe method
"""

#print(covid_df.describe())

"""The columns property contains the list of columns within the data frame"""
res = covid_df.columns

print(res)