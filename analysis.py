# author: James Connolly

# import the csv file dataset

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

iris_data = pd.read_csv("iris_data.csv")
# use the head function to ensure you have the correct dataframe
print("Showing the first 5 lines\n")
print(iris_data.head())

# Check for Missing Values
print("Show any missing values\n")
print(iris_data.isnull().sum())

# Identify the columns and there datatypes using the dataframe info method.
# This will print the full summary with columns, count and datatypes
print("Show data shape\n")
print(iris_data.shape)

# To gather more info on data 
print("\n-----Data Info results------")
print(iris_data.info())

# Use the describe method to analyse the data where the values can be
# used further on in the program.
print(iris_data.describe())
with open("iris.txt", "w") as f:
    data = f.write('Summary of varaibles for the Iris dataset\n'+str(iris_data.describe()))

# show the duplicated rows
iris_data[iris_data.duplicated()]

# count the exact number of species
print(iris_data.value_counts("species"))




