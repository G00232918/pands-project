# pands-project
* Fisher's Iris dataset - Analysis
* author - James Connolly
* student_Number - G00232918
* module - Programming & Scripting

* Introduction

The Iris flower data set is a specific set of information compiled by Ronald Fisher, a biologist, in the 1930s. It describes particular biological characteristics of various types of Iris flowers, specifically, the length and width of both pedals and the sepals, which are part of the flower’s reproductive system.

Fisher considered the question of what linear function of the four measurements would maximise the ratio of the difference between the specific means to the standard deviation between species. Based on the combination of the four measurement features of the sample of plants in the iris datas set, he developed a linear discriminant model to discriminate or distinguish the Iris species from each other.

Discriminant analysis is a statistical classification method used when the dependent variable is categorical. Discriminant analysis looks for the best linear combination of independent variables that will discriminate between the categories of the dependent variables and to see if significant differences exists among the groups of predictor variables. 

The Iris dataset use, is for people to explore the world of data mining, it has become a common testing tool in recent times. 


Analysis of data

Firstly I read the file into program by importing csv. Pandas is imported as pd for convieniece when using the library in the code.

I used the following -

irisData = pd.read_csv("iris_dataset.csv")

Once the file was read in, I used the shape command to show how many rows and columns were present. This was for me to get the scope of how much data I was reviewing. With this command it showed thre was 150 rows with 5 columns. 

From my research I found then that is common practice in data analaysis to use the head command to check that you are actuaclly reviewing the correct data before your analysis begins. So I printed out the first 5 lines from the dataset to show that I was.

Checking for missing values, in this dataset there is no missing values. This is to ensure that there is biased estimaties that can lead to invalid results.

The next to do was to use the data info command to understand more about the data. From this I found that none of the columns had any null values. Four columns are numerical type and there is one columen used as the categorical type.

Data describe then broke down in the following columns -
* count - This showed that there was an equal number of attributes for the four columns.
* mean - This shows that column 1 has the highest mean so the highest numerical values are in column 1(sepal length).
* min value - Shows the minimum value for each column.
* standard deviation - 
* 25% / 50% / 75% - This the percentages of the numeric values. Again column 1 is showing with tthe highest values
* max value - Shows the maximum value for each column.

As from further research for data analysis, one important action to take is to check if there is any duplicates. If there is duplicates it can they are not found it can give you a false pveriew of the data. In this dataset, there is no duplicates after I ran the following code - iris_data[iris_data.duplicated()].

I checked and counted the number species before I began plotting any histograms. I wanted to know approximately how the data should look. Having the count gave me a view on what to expect. 

The histograms then follow. See the following list with name and png file -
* Sepal Length Histogram - sepal_length.png
* Sepal Width Histogram - sepal_width.png
* Petal Length Histogram - petal_length.png
* Petal Width HIstogram - petal_width.png






