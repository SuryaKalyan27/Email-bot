import csv
from csv import reader
from csv import DictReader
import pandas as pd  

data = pd.read_csv('file.csv')

df = data.head()
print(df)

Email_list = df['Name'].tolist()
Email_Addr = df['email'].tolist()

