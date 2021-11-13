# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 17:24:11 2018

@author: MUJ
"""

#3.POLYNOMIAL PREGRESSION ALGORITHM
y=x^3+x^2+x
y is the label
x and all its powers in matrix are features

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Normal Linear Regression
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.ft(features,labels)

#Using polynomial regression and fiting on the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_object=PolynomialFeatures(degree=6)
features_poly=poly_object.fit_transform(features)

lin_reg_2=LinearRegression()
lin_reg_2.fit(features_poly,labels)

#4.DECISION TREE REGRESSION

#y=avg(x1,x2) is the mapping function on which we perform our predictions
#data is split and we get different clusters say male and female and then we perform our predictions say height of a female and height of a male
#instead of the entire dataset of everyone(male+female) we have now split it into two different categories
#this will come under both CLASSIFICATION and REGRESSION 
#because first we will divide the dataset and then to predict we can see which data points are more in which category
#the feature which has high INFORMTION GAIN(most important feature) will be selected as the root node

import pandas as pd
import numpy as np


dataset=pd.read_csv('Position_Salaries.csv')
features=dataset.iloc[:,1:2].values
labels=dataset.iloc[:,2].values

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(features,labels)

labels_pred=regressor.predict(6.5)

features_grid=np.arange(min(features),
max(features),0.01)
features_grid=features_grid.reshape(-1,1)
plt.scatter(features,labels,color='red')
plt.plot(features_grid,
         regressor.predict(features_grid),color='blue')
plt.show()


#5.RANDOM FOREST REGRESSION

#will get predictions from n number of decision tree
#we can define  the number of decision trees want
#and then will average out the predictions from all tree
#ENSEMBLE LEARNING where decison is dependent on predictions from many models
#best for undistributed data
#not necessary that this will always give better results as when data very less
#will increase the cimputation cost


#CLASSIFICATION UNDER SUPERVISED ML
"""
this comes under supervised machine learning
here we predict the entire category instead of a single value
admission yes no
placed yes no
purchased yes no
overweight yes no
"""

#1.LOGISTIC REGRESSION ALGORITHM

#it is a linear classifier
#gives us a probability
#if probability>=50 percent then yes else no
#binary

dataset1=pd.read_csv('Social_Network_Ads.csv')
features=dataset1.iloc[:,[2,]].values
labels=dataset1.iloc[:,4].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()                                    
features_train=sc.fit_transform(features_train)        
features_test=sc.transform(features_test)    

#Normal linear regression
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.ft(features_train,labels_train)

#Logistic Regression
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(features_train,labels_train)

labels_pred=classifier.predict(features_test)

#we get a confusion matrix in classification
#right side is what we predict
#bottom side is actual values

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_pred)


