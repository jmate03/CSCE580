# jsmateo 2025 based on Supervised-Regression on class repo
# test running pandas
import pandas as pd
import numpy as np
import os

# print(os.getcwd())

# datadir = '../data/'
# datafile = datadir + "data.csv"
script_dir = os.path.dirname(os.path.abspath(__file__))
datafile = os.path.join(script_dir, '..', '..', 'data', 'data.csv')
data = pd.read_csv(datafile)

#debugging prints
# print(data.head())
# print(data.shape)
# data.info()

condition = (data['Height (cm)'] > 140.0) & (data['BMI (numeric)'] < 30.0)
data_test = data[condition]
data_test.head()