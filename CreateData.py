# Creating and normalizing data

import pandas as pd

XandYlist = ["Category", "km4week", "sp4week", "CrossTraining", "Wall21", "MarathonTime"] # creating list of columns for x and y
marathon_data = pd.read_csv("InitialMarathonData.csv", usecols = XandYlist)
marathon_data = marathon_data.fillna(value = 0);

def FixCrossTraining(string):
    if string == "":
        return 0;
    if string == 0:
        return 0;
    else:
        return string[9];

marathon_data['CrossTraining'] = marathon_data['CrossTraining'].apply(FixCrossTraining)

# Now dropping rows that are missing data
marathon_data = marathon_data.drop(index = [25, 34, 51, 53, 73, 80], axis = 0)
marathon_data = marathon_data.drop(index = [0,1,2], axis = 1)

# Saving the updated marathon data
marathon_data.to_csv('UpdatedMarathonData.csv') # saving data as a CSV


x_list = ["Category", "km4week", "sp4week", "CrossTraining", "Wall21"] # creating list of columns for x
y_list = ["MarathonTime"] # creating list of columns for y
x = pd.read_csv("UpdatedMarathonData.csv", usecols = x_list) # reading CSV into a dataframe
y = pd.read_csv("UpdatedMarathonData.csv", usecols = y_list) # reading CSV into a dataframe

def addWAM(string):
    return_value = 0;
    if string == "WAM":
        return_value = 1;
    return return_value;

def addMAM(string):
    return_value = 0;
    if string == "MAM":
        return_value = 1;
    return return_value;

def addMaleOver40(string):
    return_value = 0;
    if string != "MAM" and string != "WAM":
        return_value = 1;
    return return_value;

# Default is that the athlete is a male under the age of 40
x['isWAM'] = x['Category'].apply(addWAM) # adding the isWAM column
x['isMaleOver40'] = x['Category'].apply(addMaleOver40) # adding the isMaleOver40 column

# Now removing the Category column
del x["Category"]


x.to_csv('MarathonDataX.csv') # saving data as a CSV
y.to_csv('MarathonDataY.csv') # saving data as a CSV