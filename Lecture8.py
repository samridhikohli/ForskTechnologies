# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:13:04 2018

@author: MUJ
"""

#PREPROCESSING CONTD.

#4>FEATURE SCALING

#if one column has high range values (in previous output Lecture 7 case last column) as compared to other column values then we need to balance 
#this is called FEATURE SCALING|NORMALIZATION

1.MIN MAX SCALING
scaled value=(value-min_value)/(max_value-min_value)

2.STANDARD SCALING
scaled value=(value-mean)/standard deviation




import pandas as pd

dataset2=pd.read_csv("Cricket_Salary_Data.csv") 
features=dataset2.iloc[:,:-1].values
labels=dataset2.iloc[:,3].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.preprocessing import Imputer                        
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(features[:,1:2])                            
features[:,1:2]=imputer.transform(features[:,1:2]) 

from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
features[:,0]=labelencoder.fit_transform(features[:,0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[0])
features=onehotencoder.fit_transform(features).toarray()
 
#Standard Scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()                                    #sc is object of StanardScaler class
features_train=sc.fit_transform(features_train)        #fit here will calculate mean and standard deviation
features_test=sc.transform(features_test)              #transform will simply divide and transform value
"""
array([[  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   1.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   3.00000000e+01,   1.00000000e+04],
       [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          1.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   3.10000000e+01,   5.00000000e+03],
       [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   1.00000000e+00,
          0.00000000e+00,   2.80000000e+01,   2.00000000e+04],
       [  1.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   2.90000000e+01,   2.00000000e+04],
       [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   1.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   3.10000000e+01,   1.00000000e+04],
       [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          1.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   2.80000000e+01,   5.00000000e+03],
       [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   1.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   3.60000000e+01,   2.00000000e+04],
       [  0.00000000e+00,   0.00000000e+00,   1.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   2.40000000e+01,   1.00000000e+04],
       [  0.00000000e+00,   1.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   2.70000000e+01,   1.00000000e+04],
       [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          1.00000000e+00,   2.82727273e+01,   5.00000000e+03],
       [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          1.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   2.30000000e+01,   1.00000000e+04],
       [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   1.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   2.40000000e+01,   5.00000000e+03],
       [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   1.00000000e+00,
          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
          0.00000000e+00,   2.82727273e+01,   5.00000000e+03]])
"""
       

#SUPERVISED MACHINE LEARNING

#REGRESSION UNDER SUPERVISED ML

#1 SIMPLE LINEAR REGRESSION ALGORITHM
x axis=features
y axis=labels
straight line graph 
the line we choose out of all possible lines will be called BEST FIT LINE
BEST FIT LINE will be the one for which d1^2+d2^2+...=D (min)
where d1,d2 are vertical distances of every point from the line
square because distance may be negative 
if point is close to best fit line then mis-match will be less else miss-match will be more (between prediction and actual value)

import pandas as pd

dataset=pd.read_csv("Income_Data.csv") 

features=dataset.iloc[:,:1].values
labels=dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

#SIMPLE LINEAR REGRESSION
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)

print regressor.predict(6.5)
"""
array([ 87311.83747437])
"""

label_pred=regressor.predict(features_test)    #predicting based on values in features_test

#VISUALIZING THE BEST FIT LINE FOR THE TEST RESULTS
import matplotlib.pyplot as plt
plt.scatter(features_test,labels_test,color='red')
plt.plot(features_train,regressor.predict(features_train),color='blue')
plt.show

#SCORE OF OUR TRAINING DATA
Score=regressor.score(features_test,labels_test)
""" 0.98816951572912604 """

#if score of training data is good but poor for test data then that is called OVERFITTING
#if score of both training data and test data is poor then called UNDERFITTING

#BEST MODEL WILL BE THE ONE WITH NO OVER OR UNDER FITTING
