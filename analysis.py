# author: James Connolly

# import the csv file dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import csv file for pandas
iris_data = pd.read_csv("iris_data.csv")

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
# Reference - https://realpython.com/python-csv/
print("\n-----Analysis of the data-----")
print(iris_data.describe())
with open("iris_summary.txt", "w") as f:
    data = f.write('Summary of variables for the Iris dataset\n'+str(iris_data.describe()))

# show the duplicated rows
print("\n-----No duplicates as shown-----")
iris_data[iris_data.duplicated()]

# count the exact number of species
# Reference - https://www.tutorialspoint.com/how-can-i-show-figures-separately-in-matplotlib
# Reference to close figures for the data to show only within the named function -
# https://matplotlib.org/2.0.2/api/pyplot_api.html

print("\n-----Count for the number of species-----")
print(iris_data.value_counts("species"))

# histogram for sepal length data
print("\n-----Sepal Length Histogram-----")

def sepal_length_histo_func():
    plt.figure(figsize = (11,8))
    x = iris_data["sepal_length"]
    plt.hist(x, bins = 20, color = "blue")
    plt.title("Sepal Length in cm")
    plt.xlabel("Sepal_Length_in_cm")
    plt.ylabel("Count")
    plt.savefig("sepal_length.png")
    plt.close()
sepal_length_histo_func()

# histogram for sepal width data
print("\n-----Sepal Width Histogram-----")

def sepal_width_histo_func():
    plt.figure(figsize = (11,8))
    x = iris_data["sepal_width"]
    plt.hist(x, bins = 20, color = "blue")
    plt.title("Sepal Width in cm")
    plt.xlabel("Sepal_Width_in_cm")
    plt.ylabel("Count")
    plt.savefig("sepal_width.png")
    plt.close()
sepal_width_histo_func()

# histogram for petal length data
print("\n-----Petal Length Histogram-----")

def petal_length_histo_func():
    plt.figure(figsize = (11,8))
    x = iris_data["petal_length"]
    plt.hist(x, bins = 20, color = "green")
    plt.title("Petal Length in cm")
    plt.xlabel("Petal_Length_in_cm")
    plt.ylabel("Count")
    plt.savefig("petal_length.png")
    plt.close()
petal_length_histo_func()

# histogram for petal width data
print("\n-----Petal Width Histogram-----")

def petal_width_histo_func():
    plt.figure(figsize = (11,8))
    x = iris_data["petal_width"]
    plt.hist(x, bins = 20, color = "green")
    plt.title("Petal Width in cm")
    plt.xlabel("Petal_Width_in_cm")
    plt.ylabel("Count")
    plt.savefig("petal_width.png")
    plt.close()
petal_width_histo_func()

# scatter plots
# Reference - https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.DataFrame.plot.scatter.html
print("\n-----Scatter plot for Sepal Length vs Sepal Width-----")

def sepal_scatter_func():
    plt.scatter(iris_data["sepal_length"], iris_data["sepal_width"])
    plt.title("Sepal Length vs Sepal Width", loc ="left", fontsize=15)
    plt.xlabel("sepal_width")
    plt.ylabel("sepal_length")
    plt.savefig("Sepal_Scatter_plot.png")
    plt.close()
sepal_scatter_func()

print("\n-----Scatter plot for Petal Length vs Petal Width-----")

def petal_scatter_func():
    plt.scatter(iris_data["petal_length"], iris_data["petal_width"])
    plt.title("Petal Length vs Petal Width", loc ="left", fontsize=15)
    plt.xlabel("petal_width")
    plt.ylabel("petal_length")
    plt.savefig("Petal_Scatter_plot.png")
    plt.close()
petal_scatter_func()


