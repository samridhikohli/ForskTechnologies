# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:07:31 2018

@author: MUJ
"""

#NLP|NATURAL LANGUAGE PROCESSING|CLASSIFICATION
#used when your data is in text form and is continuos
#can come under both supervised and unsupervised machine learing
#library used is NATURAL LANGUAGE TOOL KIT
#can predict based on reviews if positive or negative so then will come under CLASSIFICATION
#can predict if the place will have communal rights based on what they write on social media

#STEPS FOR ALGORITHM

#1.NOISE REMOVAL
#converts text to features
#takes only the data which matters
#example if we have loved this place can be converted to loved place as the sentiment remains the same
#so we can remove uneccessary things like . , spaces

#2.STEMMING
#finding the root word
#example if we have love loved loving all be converted to love
#so loved place will now be love place

#after step2 we make a dictionary of the unique words with their count

#3.VECTORIZATION
#we then make that many number of columns (number of unique words) this will be VECTORIZATION and we will use this as our feature
#this is called BAG OF WORDS MODEL
#converting the textual data to numerical form

import pandas as pd

dataset=pd.read_csv('Restaurant_Reviews.tsv',delimiter='\t',quoting=3)      
#tab separated values(.tsv)
#by default it takes the delimiter as ,
#quoting 3 means that we are dropping the double quotes

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

#stopwords are and,the..

from nltk.stem.porter import PorterStemmer

#performing noise removal and stemming on first row
review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][0])
review=review.lower()
review=review.split()       
"""['wow', 'loved', 'this', 'place']"""

ps = PorterStemmer()
review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
""" ['wow', u'love', 'place']"""

review = ' '.join(review)  #converting the list back to string
""" u'wow love place' """

#Now we append everything in the array corpus for all rowws
corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)


# this text to features now
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)      #taking initial 1500 values of features as they are most frequent
features = cv.fit_transform(corpus).toarray()

labels = dataset.iloc[:, 1].values

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,p=2) 
classifier.fit(features_train,labels_train)

labels_pred=classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_pred)
"""array([[74, 23],
       [55, 48]], dtype=int64)"""
    
#instead use Naive Bayes which is better
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(features_train, labels_train)    
    
labels_pred=classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_pred)
"""array([[55, 42],
       [12, 91]], dtype=int64)"""
    
