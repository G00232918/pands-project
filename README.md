# pands-project
* Fisher's Iris dataset - Analysis
* Author - James Connolly
* Student_Number - G00232918
* Mpdule - Programming & Scripting

* Introduction

The Iris flower data set is a specific set of information compiled by Ronald Fisher, a biologist, in the 1930s. It describes particular biological characteristics of various types of Iris flowers, specifically, the length and width of both pedals and the sepals, which are part of the flower’s reproductive system. (Techopedia)

Discriminant analysis is a statistical classification method used when the dependent variable is categorical. Discriminant analysis looks for the best linear combination of independent variables that will discriminate between the categories of the dependent variables and to see if significant differences exists among the groups of predictor variables. (statisticsolutions)

The Iris dataset use, is for people to explore the world of data mining, it has become a common testing tool in recent times. 


* Analysis of data

Firstly I read the file into program by importing csv. Pandas is imported as pd for convieniece when using the library in the code.

I used the following -

irisData = pd.read_csv("iris_dataset.csv")

Once the file was read in, I used the shape command to show how many rows and columns were present. This was for me to get the scope of how much data I was reviewing. With this command it showed thre was 150 rows with 5 columns. 

From my research I found then that is common practice in data analysis to use the head command to check that you are actuaclly reviewing the correct data before your analysis begins. So I printed out the first 5 lines from the dataset to show that I was.

Checking for missing values, in this dataset there is no missing values. This is to ensure that there is biased estimaties that can lead to invalid results.

The next to do was to use the data info command to understand more about the data. From this I found that none of the columns had any null values. Four columns are numerical type and there is one columen used as the categorical type.

Data describe then broke down in the following columns -
* count - This showed that there was an equal number of attributes for the four columns.
* mean - This shows that column 1 has the highest mean so the highest numerical values are in column 1(sepal length). From the eman value it shows that the petal has the more differential features than the sepa. As the petal width is much smaller than the petal length.
* min value - Shows the minimum value for each column.
* standard deviation - 
* 25% / 50% / 75% - This the percentages of the numeric values. Again column 1 is showing with tthe highest values
* max value - Shows the maximum value for each column.

As from further research for data analysis, one important action to take is to check if there is any duplicates. If there is duplicates it can they are not found it can give you a false pveriew of the data. In this dataset, there is no duplicates after I ran the following code - iris_data[iris_data.duplicated()].

I checked and counted the number species before I began plotting any histograms. I wanted to know approximately how the data should look. Having the count gave me a view on what to expect. Also I created a pie chart function where you can see the count visually. This is a good representation for a user as they can instantly pick up if there is species that is dominant. You can see there is an equal share for each species in the pie chart.

The histograms then follow. See the following list with name and png file -
* Sepal Length Histogram - sepal_length.png
* Sepal Width Histogram - sepal_width.png
* Petal Length Histogram - petal_length.png
* Petal Width HIstogram - petal_width.png

Histogram Summary -

From the Sepal Length I found that the highest counts in the range of 5cm - 5.5cm. Also the higher amounts are between 5cm and 6.5cm, so the Sepal length grow to this size more consistently. For Sepal Width, the most frequent range to grow to, is 2.5cm to 3.5cm.

For Petal length, the highest count is clearly in the range of 1cm - 2cm. Also for the Petal Width the highest count is at the lower end of the scale from the range from 0-1cm. 

The Sepal is a bigger part of the Iris according to the counts in the histogram data. 

I then created the scatter plots. See the following list with name and png file -
* Sepal Scatter Plot - sepal_scatter_plot.png
* Petal Scatter Plot - petal_scatter_plot.png
* Sepal Length v Petal Length Plot - sepalvpetal_len_Scatter_plot.png
* Sepal Width v Petal Width Plot - sepalvpetal_wid_scatter_plot.png
* Sepal Length v Petal Width - sepallen_v_petalwid_scatter_plot.png
* Sepal Width v Petal Length - sepalwid_v_petallen_scatter_plot.png

Scatter plot summary -

The majority of the scatter plots don't show any strong relationship bar the Petal Scatter plot. This shows that there is a strong linear relationship for the Petal Scatter plot because the plots are showing around the middle of the diagram. These doesn't appear to be any outliers.

Finally I created a heatmap to review the correlation - sns-heatmap.png. A heatmap contains values representing various shades of the same colour for each value to be plotted. Usually the darker shades of the chart represent higher values than the lighter shade. For a very different value a completely different colour can also be used. (tutorialspoint) 

In any heatmap the higher values are shown closer to one and the light colours are for the smaller values. 

Petal length and width are positively correlated (r = 0.96), which tells us that as one gets larger so does the other, indicating that petal length and width have a close relationship.

* References -
https://www.techopedia.com/definition/32880/iris-flower-data-set
https://www.statisticssolutions.com/discriminant-analysis/ 
https://www.tutorialspoint.com/python_data_science/python_heat_maps.htm#:~:text=Advertisements,colour%20can%20also%20be%20used.








