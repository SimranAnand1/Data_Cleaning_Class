import pandas as pd 
import numpy as np 

data= pd.read_csv('D:\Adda247\Data_Cleaning_Class\StudentsPerformance.csv')

data=data.dropna()

data=data.drop_duplicates()

print(data.head())