# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 17:14:09 2018

@author: MUJ
"""

#2 MULTIPLE LINEAR REGRESSION 
Q=ax+by+cz
three dimensional data
straight line
x,y,z are multiple features and Q is label


import pandas as pd
import numpy as np

dataset=pd.read_csv("Salary_Classification.csv") 

features=dataset.iloc[:,:4].values
labels=dataset.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
features[:,0]=labelencoder.fit_transform(features[:,0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[0])
features=onehotencoder.fit_transform(features).toarray()
"""
1	0	0	2300	0	1.1
0	1	0	2100	1	1.3
1	0	0	2104	2	1.5
0	0	1	1200	1	2
0	1	0	1254	2	2.2
0	0	1	1236	1	2.9
1	0	0	1452	2	3
0	1	0	1789	1	3.2
0	0	1	1645	1	3.2
0	0	1	1258	0	3.7
0	1	0	1478	3	3.9
1	0	0	1257	2	4
1	0	0	1596	1	4
0	1	0	1256	2	4.1
0	0	1	1489	3	4.5
1	0	0	1236	3	4.9
0	1	0	2311	2	5.1
0	0	1	2245	3	5.3
1	0	0	2365	1	5.9
1	0	0	1500	3	6
0	1	0	1456	2	6.8
0	1	0	1760	1	7.1
0	0	1	2400	4	7.9
1	0	0	2148	3	8.2
0	0	1	1450	2	8.7
0	0	1	1000	4	9
0	1	0	1540	3	9.5
1	0	0	1500	2	9.6
0	1	0	3000	4	10.3
0	0	1	2100	3	10.5
"""

#if we have n hot encoded columns then we can remove the one column as we already know the values in next column

#Avoiding the dummy trap
features=features[:,1:]     #we are neglecting the values in column 0 (droping one column)
                            #helps in neglecting the redundant values 

#MULTICOLINEARITY 
if values of one column are dependent on the next column
    
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
    
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)

pred=regressor.predict(features_test) 
"""
43891.3
126961
62010.5
61270.2
112781
106172
"""

#Predicting for some other values
x=np.array([0,0,1150,3,4]).reshape(1,5)   
"""
Here 0,0 is Development as when we first label encoded we saw that Development got 0 
now in one hot encoding dev will be 1,0,0 (Development,Testing,UX)
and we dropped first column so now it is 0,0 
we have converted this list into a nd array as predict function takes a nd array and it should be a 2D array thus used reshape
default we write reshape(1,-1) when we domt know number of columns (here we wrote 5 as we know the value)
default we write reshape(-1,1) when we dont know number of rows
"""

regressor.predict(x)
""" 
array([ 62362.14371688])
"""

#Now we try to find those columns/features that have maxiumum impact/play an important role in predicting the value

import statsmodels.formula.api as sm

#adding constant value to the model to make it a straight line that is const+ax+by+cz
features=np.append(arr=np.ones((30,1)),values=features,axis=1)

#FINDING THE MOST IMPORTANT FEATURES
features_opt=features[:,[0,1,2,3,4,5]]
regressor_opt=sm.OLS(endog=labels,exog=features_opt).fit()  #optimal least square that is finds the best fit line
regressor_OLS.summary()                                     #gives the table


#DIMENSION REDUCTION|BACKWARD ELIMINATION
#DROPPING NON IMPORTANT VALUES
#drop the one with high p value as high p value means less important feature

#if p value>5 percent then drop the column else retain the features
#at a time we can remove only one feature

features_opt=features[:,[0,1,3,4,5]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()  
regressor_OLS.summary()     

features_opt=features[:,[0,3,5]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()  
regressor_OLS.summary()  

features_opt=features[:,[0,5]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()  
regressor_OLS.summary()   

print regeressor.coef_

#so now we can use this most important feature to train our model instead of passing all the features
