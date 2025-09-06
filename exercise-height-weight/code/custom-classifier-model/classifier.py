# jsmateo 2025 
# heavily based on Supervised-Regression-Classification example on class repository
# Model to predict BMI category given height using logistic regression
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

datadir = '../../data/'
datafile = datadir + "data.csv"

data = pd.read_csv(datafile)

#print(data.columns)
# Data of interest
x = data ['Height (cm)']
y = data ['BMI Category = C1, C2, C3, C4']

x, y = np.array(x), np.array(y)
x = x.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

logreg = LogisticRegression(C=1e5)
model = logreg.fit(x_train, y_train)

# Model info
print (' Model details:')
print (' -  intercept : ', model.intercept_)
print (' -  coeff : ', model.coef_)

# Predicted values for train and test
y_pred_train = model.predict(x_train)
y_pred_test = model.predict(x_test)

print("-----------Confusion Matrix: -----------")
CM = confusion_matrix(y_test, y_pred_test)
print (CM)
