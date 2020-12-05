from sklearn.linear_model import LinearRegression
from numpy import genfromtxt
from yellowbrick.regressor import ResidualsPlot
import pandas as pd
import numpy as np

# Create the train and test data
x_training = np.loadtxt("MarathonDataXTraining.csv", delimiter = ",") # reading CSV into numpy array
y_training = np.loadtxt("MarathonDataYTraining.csv", delimiter = ",") # reading CSV into numpy array
x_testing = np.loadtxt("MarathonDataXTesting.csv", delimiter = ",") # reading CSV into numpy array
y_testing = np.loadtxt("MarathonDataYTesting.csv", delimiter = ",") # reading CSV into numpy array

# Creating an instance of the class Linear Regression
model = LinearRegression()

# Making residual plot
visualizer = ResidualsPlot(model)

visualizer.fit(x_training, y_training)  # Fit the training data to the visualizer
visualizer.score(x_testing, y_testing)  # Makes predictions using the x_testing data and compares that to the actual marathon times
visualizer.show(model)                 # Finalize and render the figure