# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:31:35 2020

@author: walia
"""

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
import pickle

USAhousing = pd.read_csv('USA_Housing.csv')


X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAhousing['Price']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)
from sklearn.linear_model import LinearRegression

lm = LinearRegression()

lm.fit(X_train,y_train)


coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])

pickle.dump(lm, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))


predictions = lm.predict(X_test)

