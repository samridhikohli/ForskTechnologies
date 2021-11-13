# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:16:19 2018

@author: MUJ
"""

#APRORI ALGORITHM|ASSOCIATION

#which item sold with respect to another item

#SUPPORT
#popularity of an item say item X
#support=item bought divided by total number of items

#CONFIDENCE
#likelihood or probability of purchasing another item say item Y related to this item
#confidence=supprort of both items(X,Y) divided by support of item X

#LIFT
#it can so happen that item Y is more popular than X so LIFT=support(X,Y) divided by (support(X)*support(Y))
#if lift>1 then strong association
#if lift=1 the items are neutral
#if lift<1 the negative association


import pandas as pd

dataset=pd.read_csv('Market_Basket_Optimisation.csv',header=None)  #as we doont have any column name and the data starts from first line itself

transactions=[]

#needs data in the list format
for i in range(0,7501):
    transactions.append(list(dataset.values[i]))
    

from apyori import apriori
rules=apriori(transactions,min_support=0.004,min_confidence=0.25,min_lift=4)    
#min_support 0.004 used to find those items from dataset which has atleast some popularity that is being sold 4 times a day so 28.0 (which is 7days*4 times being sold)/7500(total no. of items)

results=list(rules)   #typecasting
              
