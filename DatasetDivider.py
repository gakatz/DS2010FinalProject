# Takes the data and divides it into training and testing data
import pandas as pd
from sklearn.model_selection import train_test_split

x = pd.read_csv("MarathonDataX.csv") # reading CSV into a dataframe
y = pd.read_csv("MarathonDataY.csv") # reading CSV into a data frame

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.75, random_state=42)

print(f"Test labels:\n{x_train}")
print(f"Train labels:\n{y_train}")
print(f"Test labels:\n{x_test}")
print(f"Train labels:\n{y_test}")

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

