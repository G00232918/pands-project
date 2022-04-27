# author: James Connolly

# imports used for the analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read in the csv file
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
# Reference - https://www.geeksforgeeks.org/find-duplicate-rows-
# in-a-dataframe-based-on-all-or-selected-columns/
print("\n-----No duplicates as shown-----")
iris_data[iris_data.duplicated()]

# count the exact number of species
# Reference - https://www.tutorialspoint.com/how-can-i-show-figures-separately-in-matplotlib
# Reference to close figures for the data to show only within the named function -
# https://matplotlib.org/2.0.2/api/pyplot_api.html
print("\n-----Count for the number of species-----")
print(iris_data.value_counts("species"))

# show species on a pie chart
# Reference - https://www.w3schools.com/python/matplotlib_pie_charts.asp
print("\n-----Species Pie Chart-----")

def pie_chart_species_func():
    plt.figure(figsize = (11,8))
    x = iris_data.value_counts("species")
    irislabels = ["Iris-setosa", "Iris-veriscolor", "Iris-virginica"]
    iriscolors = ["black", "yellow", "blue"]
    plt.pie(x, labels = irislabels, colors = iriscolors)
    plt.savefig("pie_chart_species.png")
    plt.close()
pie_chart_species_func()


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
    plt.title("Petal_Length_in_cm")
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
    plt.xlabel("sepal_length")
    plt.ylabel("sepal_width")
    plt.savefig("Sepal_Scatter_plot.png")
    plt.close()
sepal_scatter_func()

print("\n-----Scatter plot for Petal Length vs Petal Width-----")

def petal_scatter_func():
    plt.scatter(iris_data["petal_length"], iris_data["petal_width"])
    plt.title("Petal Length vs Petal Width", loc ="left", fontsize=15)
    plt.xlabel("petal_length")
    plt.ylabel("petal_width")
    plt.savefig("Petal_Scatter_plot.png")
    plt.close()
petal_scatter_func()

print("\n-----Scatter plot for Petal Length vs Sepal Length-----")

def sepalvpetal_len_scatter_func():
    plt.scatter(iris_data["petal_length"], iris_data["sepal_length"])
    plt.title("Petal Length vs Sepal Length", loc ="left", fontsize=15)
    plt.xlabel("petal_length")
    plt.ylabel("sepal_length")
    plt.savefig("sepalvpetal_len_Scatter_plot.png")
    plt.close()
sepalvpetal_len_scatter_func()

print("\n-----Scatter plot for Petal Width vs Sepal Width-----")

def sepalvpetal_wid_scatter_func():
    plt.scatter(iris_data["petal_width"], iris_data["sepal_width"])
    plt.title("Petal Width vs Sepal Width", loc ="left", fontsize=15)
    plt.xlabel("petal_width")
    plt.ylabel("sepal_width")
    plt.savefig("sepalvpetal_wid_scatter_plot.png")
    plt.close()
sepalvpetal_wid_scatter_func()

print("\n-----Scatter plot for Sepal Length vs Petal Width-----")

def sepallen_v_petalwid_scatter_func():
    plt.scatter(iris_data["sepal_length"], iris_data["petal_width"])
    plt.title("Sepal Length vs Petal Width", loc ="left", fontsize=15)
    plt.xlabel("sepal_length")
    plt.ylabel("petal_width")
    plt.savefig("sepallen_v_petalwid_scatter_plot.png")
    plt.close()
sepallen_v_petalwid_scatter_func()

print("\n-----Scatter plot for Sepal Width vs Petal Length-----")

def sepallwid_v_petallen_scatter_func():
    plt.scatter(iris_data["sepal_width"], iris_data["petal_length"])
    plt.title("Sepal Width vs Petal Length", loc ="left", fontsize=15)
    plt.xlabel("sepal_width")
    plt.ylabel("petal_length")
    plt.savefig("sepalwid_v_petallen_scatter_plot.png")
    plt.close()
sepallwid_v_petallen_scatter_func()

# checking correlation
print("\n-----Heatmap-----")

def heatmap_func():
    plt.figure(figsize=(10,11))
    # command to create the heatmap, annot = true is write each data value in the cell.
    x = sns.heatmap(iris_data.corr(),annot=True)
    plt.plot()
    figure = x.get_figure() 
    figure.savefig("sns-heatmap.png")
    plt.close()
heatmap_func()
