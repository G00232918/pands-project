# pands-project
* Fisher's Iris dataset - Analysis
* Author - James Connolly
* Student_Number - G00232918
* Module - Programming & Scripting

# Introduction

The Iris flower data set is a specific set of information compiled by Ronald Fisher, a biologist, in the 1930s. It describes particular biological characteristics of various types of Iris flowers, specifically, the length and width of both pedals and the sepals, which are part of the flower’s reproductive system. (Techopedia)

Discriminant analysis is a statistical classification method used when the dependent variable is categorical. Discriminant analysis looks for the best linear combination of independent variables that will discriminate between the categories of the dependent variables and to see if significant differences exists among the groups of predictor variables. (statisticsolutions)

The Iris dataset use, is for people to explore the world of data mining, it has become a common testing tool in recent times. 

# Analysis of data

Firstly I read the file into program by importing csv. Pandas is imported as pd for convenience when using the library in the code. Matplotlib is used to create the histograms and seaplot for the heatmap at the end of the program.

I used the following - irisData = pd.read_csv("iris_dataset.csv")

Once the file was read in, I used the shape command to show how many rows and columns were present. This was for me to get the scope of how much data I was reviewing. With this command it showed there was 150 rows with 5 columns. 

From my research I found that this is common practice in data analysis to use the head command to check that you are actually reviewing the correct data before your analysis begins. So I printed out the first 5 lines from the dataset to show that I was.

Checking for missing values, in this dataset there is no missing values. This is to ensure that there is no biased estimaties that can lead to invalid results.

Following on I used the data info command to understand more about the data. From this I found that none of the columns had any null values. Four columns are numerical type and there is one column used as the categorical type.

Data describe then broke down in the following columns -
* count - This showed that there was an equal number of attributes for the four columns.
* mean - This shows that sepal length column has the highest mean. From the mean value it shows that the petal has the more differential features than the sepal. As the petal width is much smaller than the petal length.
* min value - Shows the minimum value for each column.
* standard deviation - The standard deviation shows how dispersed the data. In this dataset the most dispersed variable is the sepal width.
* 25% / 50% / 75% - These are the percentages of the numeric values. Again sepal length column is showing the highest values
* max value - Shows the maximum value for each column.


With the data describe information, this gave a desription of the variables. I wrote the results to a text file - iris_summary.txt.

From further research for data analysis, one important action to take is to check if there is any duplicates. If there is duplicates and they are not found it can give you a false overiew of the data. In this dataset, there is no duplicates after I ran the following code - iris_data[iris_data.duplicated()].

I checked and counted the number species before I began plotting any histograms. I wanted to know approximately how the data should look. Having the count gave me a view on what to expect. Also I created a pie chart function where you can see the count visually. This is a good representation for a user as they can instantly pick up if there is a species that is dominant. You can see there is an equal share for each species in the pie chart.

# Histograms

The histograms then follow. See the following list with name and png file -
* Sepal Length Histogram - sepal_length.png
* Sepal Width Histogram - sepal_width.png
* Petal Length Histogram - petal_length.png
* Petal Width HIstogram - petal_width.png

 # Summary -

From the Sepal Length I found that the highest counts in the range of 5cm - 5.5cm in length. Also the higher amounts are between 5cm and 6.5cm, so the Sepal length grow to this size more consistently. For Sepal Width, the most frequent range to grow to, is 2.5cm to 3.5cm.

For Petal length, the highest count is clearly in the range of 1cm - 2cm. Also for the Petal Width the highest count is at the lower end of the scale from the range from 0-1cm. 

The Sepal is a bigger part of the Iris according to the counts in the histogram data. 

# Scatter Plots

I then created the scatter plots. See the following list with name and png file -
* Sepal Scatter Plot - sepal_scatter_plot.png
* Petal Scatter Plot - petal_scatter_plot.png
* Sepal Length v Petal Length Plot - sepalvpetal_len_Scatter_plot.png
* Sepal Width v Petal Width Plot - sepalvpetal_wid_scatter_plot.png
* Sepal Length v Petal Width - sepallen_v_petalwid_scatter_plot.png
* Sepal Width v Petal Length - sepalwid_v_petallen_scatter_plot.png

# Summary -

The majority of the scatter plots don't show any strong relationship bar the Petal Scatter plot. This shows that there is a strong linear relationship for the Petal Scatter plot because the plots are showing around the middle of the diagram. There doesn't appear to be any outliers.

Finally I created a heatmap to review the correlation - sns-heatmap.png. A heatmap contains values representing various shades of the same colour for each value to be plotted. Usually the darker shades of the chart represent higher values than the lighter shade. For a very different value a completely different colour can also be used. (tutorialspoint) 

Petal length and width are positively correlated (0.96), which tells us that as one gets larger so does the other, indicating that petal length and width have a close relationship.

# References -
* techopedia - https://www.techopedia.com/definition/32880/iris-flower-data-set
* statisticssolutions - https://www.statisticssolutions.com/discriminant-analysis/ 
* tutorialspoint - https://www.tutorialspoint.com/python_data_science/python_heat_maps.htm#:~:text=Advertisements,colour%20can%20also%20be%20used.








