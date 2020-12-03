# Creating and normalize data

import pandas as pd

x_list = ["Category", "km4week", "sp4week", "CrossTraining", "Wall21"] # creating list of columns for x
y_list = ["MarathonTime"] # creating list of columns for y
x = pd.read_csv("MarathonData.csv", usecols = x_list) # reading CSV into a dataframe
y = pd.read_csv("MarathonData.csv", usecols = y_list) # reading CSV into a data frame
# x.fillna(value = 0)
# Need to get fillna line working and then edit the other CrossTraining values to be numerical

# Now I need to normalize data

x.to_csv('MarathonDataX.csv') # saving data as a CSV
y.to_csv('MarathonDataY.csv') # saving data as a CSV