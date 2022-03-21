# author: James Connolly

# import the csv file dataset

import pandas as pd

irisData = pd.read_csv("iris_dataset.csv")

# Identify the columns and there datatypes using the dataframe info method.
# This will print the full summary with columns, count and datatypes

print(irisData.shape)

# Use the describe method to analyse the data where the values can be
# used further on in the program.
print(irisData.describe())