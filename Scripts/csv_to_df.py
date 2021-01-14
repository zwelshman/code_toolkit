import os
import pandas as pd 
import csv

#### Integrate Python and R ####


#### Import raw data CSV into dataframe ####
def read_CSV_DF():
        path = "./Data_Raw/"
        fileName = "Test.csv"
        df_csv = pd.read_csv(path+fileName)
        return df_csv

df=read_CSV_DF()
print(read_CSV_DF())

#### Perform some reshaping of the data ####

#### Perform some functions to the data ####



