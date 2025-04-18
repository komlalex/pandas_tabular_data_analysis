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
res = type(covid_df)

res =len(covid_df)

"""Here is what we can tell by looking at the data frame: 
1. The file provides four daywise counts for covid-19 in Italy
2. The metrics reparted are new cases, new deaths and new tests 
3. Data is provided for 248 days: Dec 12, 2019 to Sep 3, 2020. 

Keep in mind that these are officially reported numbers, and the actual number of 
cases & deaths may be higher, as not all cases are diagnosed. 
We can view some basic information about the data frame by using the .info method.
"""
#res = covid_df.info()

"""It appears that each column contains values of a specific data type. For 
the numeric columns, you can view some statistical information like mean, standard 
deviation, minimum/maximum values of the non-empty values using the .describe method
"""

res = covid_df.describe()

"""The columns property contains the list of columns within the data frame by using
the .shape method."""
res = covid_df.shape

"""You can also retrieve the number of rows and columns in the data frame by usig"""
res = covid_df.columns
"""Here's a summary of the functions & methods we've looked at so far.

*pd.read_csv - Read data from a csv file into a Pandas DataFrame object
*.info - View basic information about rowss, columns & data types
* .describe - Vview statistical information about numeric columns 
* .columns - Get the list of column names 
* shape - Get the number of rows and coulmns as a tuple 
"""

"""retrieving data from a data frame 
The first thing you might want to do is to retrieve data from this data frame e.g. 
the counts of specific day or rge list of values in a specific column. To do this, it 
might help to understand the internal representation of the data in a data frame. Conceptually, 
you canm think of a data frame as a dictionary of lists; the keys are the column names, 
and the values are lists/arrays containing data for the respective columns.
"""
# Pandas format is similar to this 
covid_data_dict = {
    "data": ["2020-08-30", "2020-08-31", "2020-09-01", "2020-09-02"], 
    "new_cases": [1444, 1365, 996, 975], 
    "new_deaths": [1, 4, 6, 8], 
    "new_tests": [53541, 42583, 54395, None]
} 

"""Representing data in the above format has a few benefits
1. All values in a column typically have the same type of value, so it is more 
efficient to store them in a single array 
2. Retrieving the values for a particular row simply requires extracting the elements 
at a given index from each of the columns 
3. The representation is more compact (column names are recorded only ones) compared 
to other formats where you might use a dictionary for each row of data. 

"""

new_cases = covid_df["new_cases"]

"Each column is represented using a data structure called Series, which is essentially a numpy"
"array wiht some extra methods" 
res = type(new_cases) 

"""
Just like arays we can rettrtieve a specific value using the indexing notation []
""" 
#print(new_cases[240]) 
 
"""Pandas also provides .at method to directly retrieve a specific rnow & column""" 
res = covid_df.at[246, "new_cases"]

"""Instead of uising the indexing notation [], Pandas also allows accessing columns 
as properties pf the data frame using the . notation. However, this might only work 
for columns whoes names do not contain spaces or special characters
""" 
new_cases = covid_df.new_cases 

"""Further nore, you can provide a list of columns within the indexing notation""" 
cases_df = covid_df[["date", "new_cases"]] 

"""
Note: the new dataframe cases_df is simply a view of the original data frame 

Sometimes, you might need to make a full copy of the data frame, in which case we 
use the .copy method
"""
covid_df_copy = covid_df.copy() 

"""
The dat within the covid_df_copy is completely seperated from covid_df, and changing the "
values inside one of them wil not affect the other.
"""

"""To access a specific row of data, Pandas provides the .loc method""" 
loc = covid_df.loc[243]
#print(loc)

"""Note: Each retrieved row is also a Series"""
#print(type(loc))

"""To view the first or last few rows of data, we can use the .head and .tail methods""" 
head = covid_df.head(5)
tail = covid_df.tail(10)  


"""NaN vs 0"""
nan = covid_df.at[0, "new_tests"]
print(type(nan)) 

"""The distinction bewtween 0 and NaN is subtle but important. In this dataset, it represents 
that daily test numbers were not reported on specific dates. In fact, Italy 
started reporting daoly tests on April 2020. By that time, 935310 tests had already 
been conducted. 

We can find the first index that contain a NaN values using first_valid_index"""
valid = covid_df.new_tests.first_valid_index() 

"""Let's look at a few rows before and after this index to verify that the values indeed 
change from NaN to actual numbers. We can do this by parsing a range to loc"""
res = covid_df.loc[: valid] 

"""The .sample method can be used to retrieve a random sample of rows from the data frame""" 
sample = covid_df.sample(20) 

"""ANALYZING DATA FROM DATA FRAMES
Let's try to answer some questions about our data 

Q: What is the total number of reported cases and deaths related to Covid-19 in Italy?
Similar to Numpy arrays, a Pandas series suports the  .sum method to answer these questions.
"""
total_cases = covid_df.new_cases.sum() 
total_deaths = covid_df.new_deaths.sum() 
print(f"The number of reported cases is {int(total_cases)} and the number of reported deaths is {int(total_deaths)}.")

"""
Q: What is the overall death rate (ration of deaths to reported cases)
""" 
death_rate = covid_df.new_deaths.sum() / covid_df.new_cases.sum() 
print(f"The overall reported death rate in Italy is {death_rate*100:.2f}%.") 

"""
What is the overall number of tests conducted? A total number of 
935310 test were conducted before daily test numbers were being reported. 
We can check the first non-NaN index using first_valid_index
"""
initial_tests = 935_310  
total_tests = initial_tests + covid_df.new_tests.sum()
print(total_tests)

"""Q: What fraction of tests reported a positive result?
""" 
positive_rate = total_cases / total_tests  

print(f"{positive_rate*100:.2f}% of tests in Italy led to a positive diagnosis.")

"""QUERYING AND SORTING ROWS
Let's say we want only to look at the days which had more than 1000 reported 
cases. We can use a boolean expression to check which rows satisfy this criterion.
""" 
high_cases = covid_df.new_cases > 1000 
print(high_cases) 

"""The boolean expression returns a series containing True and False 
boolean values. The result is a data frame with a subset of rows from the origin""" 
high_new_cases_df = covid_df[high_cases] 


"""We can write this succinctly on a single line by passing the boolean expression 
as an index to the data frame. 
"""
high_cases = covid_df[covid_df.new_cases > 1000] 
print(high_new_cases_df)

"""The data frame contains 72 roaws, but only the first 5 & last 5 rows 
are displayed by default with Jupyter, for brevity. To view all the rows, 
we can modify some display options.""" 
from IPython.display import display
with pd.option_context("display.max_rows", 100): 
    display(high_cases)