# Creating and normalizing data

import pandas as pd

x_list = ["Category", "km4week", "sp4week", "CrossTraining", "Wall21"] # creating list of columns for x
y_list = ["MarathonTime"] # creating list of columns for y
x = pd.read_csv("InitialMarathonData.csv", usecols = x_list) # reading CSV into a dataframe
y = pd.read_csv("InitialMarathonData.csv", usecols = y_list) # reading CSV into a dataframe
x = x.fillna(value = 0);

def FixCrossTraining(string):
    if string == "":
        return 0;
    else:
        return string(9);

x['CrossTraining'] = x['CrossTraining'].apply(FixCrossTraining)

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

x['isWAM'] = x['Category'].apply(addWAM) # adding the isWAM column
x['isMAM'] = x['Category'].apply(addMAM) # adding the isMAM column
x['isMaleOver40'] = x['Category'].apply(addMaleOver40) # adding the isMaleOver40 column

# Now removing empty rows and the Category column

print(x)

# Now I need to normalize data

x.to_csv('MarathonDataX.csv') # saving data as a CSV
y.to_csv('MarathonDataY.csv') # saving data as a CSV