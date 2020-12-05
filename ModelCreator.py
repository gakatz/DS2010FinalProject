import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

x_training = pd.read_csv("MarathonDataXTraining.csv") # reading CSV into a dataframe
y_training = pd.read_csv("MarathonDataYTraining.csv") # reading CSV into a dataframe
x_testing = pd.read_csv("MarathonDataXTesting.csv") # reading CSV into a dataframe
y_testing = pd.read_csv("MarathonDataYTesting.csv") # reading CSV into a dataframe


# Creating an instance of the class Linear Regression
model = LinearRegression()

# Fitting model to data
model.fit(x_training, y_training)

# Getting r_squared
r_sq = model.score(x_testing, y_testing)
print('coefficient of determination:', r_sq)

# Calculating adjusted_r_squared
