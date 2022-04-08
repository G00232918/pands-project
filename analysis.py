# author: James Connolly

# import the csv file dataset

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns

iris_data = pd.read_csv("iris_data.csv")
# Assigning indices for Iris dataset
# https://realpython.com/python-csv/
with open("iris.txt", "w") as f:
    data = f.write("Dataframe for Iris dataset")

# use the head function to ensure you have the correct dataframe
print("Showing the first 5 lines\n")
print(iris_data.head())

# Check for Missing Values
print("\n-----Show any missing values-----")
print(iris_data.isnull().sum())

# Identify the columns and there datatypes using the dataframe info method.
# This will print the full summary with columns, count and datatypes
print("\n-----Show data shape-----")
print(iris_data.shape)

# To gather more info on data 
print("\n-----Data Info results-----")
print(iris_data.info())

# Use the describe method to analyse the data where the values can be
# used further on in the program.
# https://realpython.com/python-csv/
print("\n-----Analysis of the data-----")
print(iris_data.describe())
with open("iris_summary.txt", "w") as f:
    data = f.write('Summary of variables for the Iris dataset\n'+str(iris_data.describe()))

# show the duplicated rows
print("\n-----No duplicates as shown-----")
iris_data[iris_data.duplicated()]

# count the exact number of species
print("\n-----Count for the number of species-----")
print(iris_data.value_counts("species"))

# histogram for sepal length data
print("\n-----Sepal Length Histogram-----")

plt.figure(figsize = (11,8))
x = iris_data["sepal_length"]

plt.hist(x, bins = 20, color = "blue")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_in_cm")
plt.ylabel("Count")
plt.savefig("sepal_length.png")

# histogram for sepal width data
print("\n-----Sepal Width Histogram-----")

plt.figure(figsize = (11,8))
x = iris_data["sepal_width"]

plt.hist(x, bins = 20, color = "blue")
plt.title("Sepal Width")
plt.xlabel("Sepal_Width_in_cm")
plt.ylabel("Count")
plt.savefig("sepal_width.png")

# histogram for petal length data
print("\n-----Petal Length Histogram-----")

plt.figure(figsize = (11,8))
x = iris_data["petal_length"]

plt.hist(x, bins = 20, color = "green")
plt.title("Petal Length")
plt.xlabel("Petal_Length_in_cm")
plt.ylabel("Count")
plt.savefig("petal_length.png")

# histogram for petal width data
print("\n-----Petal Width Histogram-----")

plt.figure(figsize = (11,8))
x = iris_data["petal_width"]

plt.hist(x, bins = 20, color = "green")
plt.title("Petal Width")
plt.xlabel("Petal_Width_in_cm")
plt.ylabel("Count")
plt.savefig("petal_width.png")
