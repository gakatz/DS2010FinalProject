import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import statsmodels.api as sm

x_training = pd.read_csv("MarathonDataXTraining.csv") # reading CSV into a dataframe
y_training = pd.read_csv("MarathonDataYTraining.csv") # reading CSV into a dataframe
x_testing = pd.read_csv("MarathonDataXTesting.csv") # reading CSV into a dataframe
y_testing = pd.read_csv("MarathonDataYTesting.csv") # reading CSV into a dataframe

print(x_training.shape)
print(y_training.shape)
print(x_testing.shape)
print(y_testing.shape)

# Creating an instance of the class Linear Regression
model = RandomForestRegressor()

# Fitting model to data
model.fit(x_training, y_training)

# Getting r_squared
r_squared = model.score(x_testing, y_testing)
print('r squared:', r_squared)

# Calculating adjusted_r_squared
# adjusted r squared = 1 - (1 - r squared)(n-1)/(n- p - 1) where n is the sample size and p is the number of predictors
p = 6.0;
n = 22.0;
adjusted_r_squared = 1.0 - ((1.0 - r_squared)*(n - 1.0))/(n - p - 1.0);
print('adjusted r squared:', adjusted_r_squared)


# The model's betas
#
# sm.add_constant(x_training)
# mod = sm.OLS(y_training, x_training)
# res = mod.fit()
#
# print(res.summary())
