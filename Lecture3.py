# -*- coding: utf-8 -*-
"""
This is third class

"""
#DICTIONARY
#key value pair combinations here there are 4

dict1={'fname':'John',\
       'lname':'Miller',\
       'profession':'plumber',\
       'age':'32'}

#if we print dict1 then not necessray that it will print in same order of initialization 

dict1['fname']      #John
dict1['age']        #32

dict1['fname']='James' 
"""
Now dict is
32
James
Miller
plumber
"""

#you can change values in dictionary that is it is not read only

dict1.items()   #list of all items that are part of your dictionary
"""
[('lname', 'Miller'),
 ('age', '32'),
 ('profession', 'plumber'),
 ('fname', 'James')]
"""
dict1.keys()    #list of all keys in the dictionary
"""
'lname', 'age', 'profession', 'fname']
"""

dict1.values()  #list of the values in the dictionary
"""
['Miller', '32', 'plumber', 'James']
"""


for key in dict1.keys():
    print key
"""lname
age
profession
fname"""

for k,v in dict1.items():
    print k,v
"""
lname Miller
age 32
profession plumber
fname James
"""

for k,v in dict1.items():
    print v,k
"""
Miller lname
32 age
plumber profession
James fname
"""
#problem to find frequency of words in the list

words=["one","two","one","two","three","four","one"]
freq={}     #empty dictiiionary can also use freq=dict()
for word in words:
    if word in freq:
        freq[word]=freq[word]+1
    else:
        freq[word]=1
print freq    #{'four': 1, 'three': 1, 'two': 2, 'one': 3}


str1="Manipal University"
freq={}
for letter in str1:
    if letter in freq:
        freq[letter]=freq[letter]+1
    else:
        freq[letter]=1
print freq
"""
{' ': 1,
 'M': 1,
 'U': 1,
 'a': 2,
 'e': 1,
 'i': 3,
 'l': 1,
 'n': 2,
 'p': 1,
 'r': 1,
 's': 1,
 't': 1,
 'v': 1,
 'y': 1}
"""

#REGULAR EXPRESSION
#when want to search an element in bulk data with minimum latency
#use sublime text editor

""" \d will search for digits in the file
    
    \d\d will search for two consecutive digits in file
    
    \d{4} will search for four consecutive digits in file
    
    \d{3,4} will search for all digits with min length 3 and max length 4
    
    \d{4,} will search for digits with min 4 and max length infinite
    
    \D will search for any character which is not a  digit in the file
    
    \. if want to search dots in file
    
    [abc] any of a,b or c
    
    [abc]{2} any of a,b,c in two combinations
    
    [^abc] anything except a or b or c
    
    [^a-zA-Z0-9] nothing from a-z and A-Z and 0-9
    
    ^ABC only search for string starting with ABC
    
    ABC$ only search for string ending with ABC
    
    ABC\$$ will search for string ending with ABC$ here including the dollar by using \$
    
    \w any alpha numneric character
    
    \W not alpha numeric character
    
    \s any white space
    
    \S any non white space character
    
    (abc|def) either abc or def
    
    [a-c]+\.{4}[d-f]+   + means 1 or more output from range a to c followed by 4 dots and 1 or more occurence from range d to f
    
    [a-c]*\.{4}[d-f]    * means 0 or more and same of above expression
    
    [a-c]?\.{4}[d-f]    ? means either 0 or 1 and same of above expression
    
    ^[a-z0-9_-]{3,16}$  should start from any of a-z or 0-9 or _ or - and in the range with min length 3 and max length 16 and $ denotes that it should also end with a-z or 0-9 or - or _
    
    ^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,8})$  for an email id
    
"""
    
import re   #libraray to import regular expressions
            #has three methods match,search,findall
            #match used when want to search regular expression in the starting of the list only will not travel the entire string
            #search used when want to search the regular expression in the entire string and will return that address
            #find all used when want to search the entire string and will return all the matches
            
            
#CHECKING DD-MM-YYYY FORMAT
result=re.findall(r'\d{2}-\d{2}-\d{4}','Kunal 34-3456,11-11-2011')
print result    #['11-11-2011']

#CHECKING PHONE NUMBER AND COUNTRY CODE
li=['+91-8999999999','999999-999','99999x9999']          
for val in li:
    if re.match(r'\+[0-9]{2}-[8-9]{1}[0-9]{9}',val):
     print 'yes'
    else:
        print 'no'
"""
yes
no
no
"""

