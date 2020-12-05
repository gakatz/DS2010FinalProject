# Takes the data and divides it into training and testing data
import pandas as pd
from sklearn.model_selection import train_test_split

x = pd.read_csv("MarathonDataX.csv") # reading CSV into a dataframe
y = pd.read_csv("MarathonDataY.csv") # reading CSV into a data frame

x_training, y_training, x_testing, y_testing = train_test_split(x, y, train_size=0.75, random_state=42)

x_training.to_csv('MarathonDataXTraining.csv')
y_training.to_csv('MarathonDataXTesting.csv')
x_testing.to_csv('MarathonDataYTraining.csv')
y_testing.to_csv('MarathonDataYTesting.csv')

print(f"Test labels:\n{x_training}")
print(f"Train labels:\n{y_training}")
print(f"Test labels:\n{x_testing}")
print(f"Train labels:\n{y_testing}")

