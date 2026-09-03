# Create a students.csv file using the sample data in these notes. 
# Read it into a DataFrame and print: head(), shape, columns, dtypes, info(), unique values of Placed, and value_counts() of Placed.

import pandas as pd
import numpy as np

df =pd.read_csv("student_placement_data.csv")

print(df.head())

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df['Placed'].unique())
print(df["Placed"].value_counts)