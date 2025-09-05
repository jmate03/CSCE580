# jsmateo 2025 heavily based on Supervised-Regression example on class repo
# Model to predict weight, given height using linear regression
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the data
datadir = '../../data/'
datafile = datadir + "data.csv"

data = pd.read_csv(datafile)

#debugging prints
#print(data.head())
#print(data.shape)
#data.info()

# Data of interest
x = data ['Height (cm)'] # independent variable
y = data ['Weight (kg)'] # dependent variable (to be predicted)

x, y = np.array(x), np.array(y)
x = x.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
#print (x_train.size, x_test.size, y_train.size, y_test.size)
model = LinearRegression().fit(x_train, y_train)


# Model info
print (' Model details:')
print (' -  intercept : ', model.intercept_)
print (' -  coeff : ', model.coef_)

# Predicted values for train and test
y_pred_train = model.predict(x_train)
y_pred_test = model.predict(x_test)

# Function to predict error statistics
def print_stats(y_actual, y_pred):
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_actual, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_actual, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_actual, y_pred)))

# Print for training data
print("-----------Training data stats: -----------")
print_stats(y_train, y_pred_train)
# Print for test data
print("-----------Test data stats: -----------")
print_stats(y_test, y_pred_test)

# Graph results
plt.scatter(x_test, y_test, color='black')
plt.plot(x_test, y_pred_test, color='blue', linewidth=5)
plt.xticks(())
plt.yticks(())
plt.show()

# Testing the model with a custom value for height
# height = np.array([[175]])
# predicted_weight = model.predict(height)
# print(predicted_weight)