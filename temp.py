# -*- coding: utf-8 -*-
"""
Created on Wed Oct 03 17:31:24 2018

@author: MUJ
"""
#PANDAS MACHINE LEARNING LANGUAGE

import pandas as pd

#CSV FILES
#csv stands for comma separated values 

#Read CSV file
df=pd.read_csv("Salaries.csv")      #data frame also called data set



#Pandas support two data types which are data frames and series

df.head(10)     #lists out the first 10 rows/records
"""rank discipline   phd  service   sex    salary
0       Prof          B  56.0       49  Male  186960.0
1       Prof          A  12.0        6  Male   93000.0
2       Prof          A  23.0       20  Male  110515.0
3       Prof          A  40.0       31  Male  131205.0
4       Prof          B  20.0       18  Male  104800.0
5       Prof          A  20.0       20  Male  122400.0
6  AssocProf          A  20.0       17  Male   81285.0
7       Prof          A  18.0       18  Male       NaN
8       Prof          A  29.0       19  Male   94350.0
9       Prof          A  51.0       51  Male   57800.0
"""

df.head()       #if not mentioned anything the default value is taken as 5
"""rank discipline   phd  service   sex    salary
0  Prof          B  56.0       49  Male  186960.0
1  Prof          A  12.0        6  Male   93000.0
2  Prof          A  23.0       20  Male  110515.0
3  Prof          A  40.0       31  Male  131205.0
4  Prof          B  20.0       18  Male  104800.0
"""

df.tail()       #will give last 5 record takes 5 as default value
"""
rank discipline   phd  service     sex    salary
73       Prof          B  18.0       10  Female  105450.0
74  AssocProf          B  19.0        6  Female  104542.0
75       Prof          B  17.0       17  Female  124312.0
76       Prof          A  28.0       14  Female  109954.0
77       Prof          A  23.0       15  Female  109646.0
"""

df.tail(15)     #will give last 15 records
"""
 rank         discipline   phd  service     sex    salary
63       Prof          A  29.0       27  Female   91000.0
64  AssocProf          A  26.0       24  Female   73300.0
65       Prof          A  36.0       19  Female  117555.0
66   AsstProf          A   7.0        6  Female   63100.0
67       Prof          A  17.0       11  Female   90450.0
68   AsstProf          A   4.0        2  Female   77500.0
69       Prof          A  28.0        7  Female  116450.0
70   AsstProf          A   8.0        3  Female   78500.0
71  AssocProf          B  12.0        9  Female   71065.0
72       Prof          B  24.0       15  Female  161101.0
73       Prof          B  18.0       10  Female  105450.0
74  AssocProf          B  19.0        6  Female  104542.0
75       Prof          B  17.0       17  Female  124312.0
76       Prof          A  28.0       14  Female  109954.0
77       Prof          A  23.0       15  Female  109646.0
"""

df.dtypes   #data types
            #if data is in string or text format then its data type is object and called catagorical data
            #purely numerical then data type will be integer/float
            #combination of numeric and text data then data type will again be object 
"""
rank           object
discipline     object
phd           float64
service         int64
sex            object
salary        float64
dtype: object
"""

df.columns   #lists out information of all the columns in our data frame/set

"""Index([u'rank', u'discipline', u'phd', u'service', u'sex', u'salary'], dtype='object')"""
#showing dobject in end as some data is catagorical data 

df.axes      #information regarding rows and columns
"""[RangeIndex(start=0, stop=78, step=1),
 Index([u'rank', u'discipline', u'phd', u'service', u'sex', u'salary'], dtype='object')]"""

df.ndim      #two dimensional that is rows and columns
"""2"""

df.size      #78*6 which is rows*columns
"""468"""

df.shape     #information about number of rows and columns
"""(78, 6)"""

df.values   #will leave index and title
"""
array([['Prof', 'B', 56.0, 49L, 'Male', 186960.0],
       ['Prof', 'A', 12.0, 6L, 'Male', 93000.0],
       ['Prof', 'A', 23.0, 20L, 'Male', 110515.0],
       ['Prof', 'A', 40.0, 31L, 'Male', 131205.0],
       ['Prof', 'B', 20.0, 18L, 'Male', 104800.0],
       ['Prof', 'A', 20.0, 20L, 'Male', 122400.0],
       ['AssocProf', 'A', 20.0, 17L, 'Male', 81285.0],
       ['Prof', 'A', 18.0, 18L, 'Male', nan],
       ['Prof', 'A', 29.0, 19L, 'Male', 94350.0],
       ['Prof', 'A', 51.0, 51L, 'Male', 57800.0],
       ['Prof', 'B', 39.0, 33L, 'Male', 128250.0],
       ['Prof', 'B', 23.0, 23L, 'Male', 134778.0],
       ['AsstProf', 'B', 1.0, 0L, 'Male', 88000.0],
       ['Prof', 'B', nan, 33L, 'Male', 162200.0],
       ['Prof', 'B', 25.0, 19L, 'Male', 153750.0],
       ['Prof', 'B', 17.0, 3L, 'Male', 150480.0],
       ['AsstProf', 'B', 8.0, 3L, 'Male', 75044.0],
       ['AsstProf', 'B', 4.0, 0L, 'Male', 92000.0],
       ['Prof', 'A', 19.0, 7L, 'Male', 107300.0],
       ['Prof', 'A', 29.0, 27L, 'Male', 150500.0],
       ['AsstProf', 'B', 4.0, 4L, 'Male', 92000.0],
       ['Prof', 'A', 33.0, 30L, 'Male', 103106.0],
       ['AsstProf', 'A', 4.0, 2L, 'Male', 73000.0],
       ['AsstProf', 'A', 2.0, 0L, 'Male', 85000.0],
       ['Prof', 'A', 30.0, 23L, 'Male', 91100.0],
       ['Prof', 'B', 35.0, 31L, 'Male', 99418.0],
       ['Prof', 'A', 38.0, 19L, 'Male', 148750.0],
       ['Prof', 'A', 45.0, 43L, 'Male', 155865.0],
       ['AsstProf', 'B', 7.0, 2L, 'Male', nan],
       ['Prof', 'B', 21.0, 20L, 'Male', 123683.0],
       ['AssocProf', 'B', 9.0, 7L, 'Male', 107008.0],
       ['Prof', 'B', 22.0, 21L, 'Male', 155750.0],
       ['Prof', 'A', 27.0, 19L, 'Male', 103275.0],
       ['Prof', 'B', 18.0, 18L, 'Male', 120000.0],
       ['AssocProf', 'B', nan, 8L, 'Male', 119800.0],
       ['Prof', 'B', 28.0, 23L, 'Male', 126933.0],
       ['Prof', 'B', 45.0, 45L, 'Male', 146856.0],
       ['Prof', 'A', 20.0, 8L, 'Male', 102000.0],
       ['AsstProf', 'B', 4.0, 3L, 'Male', 91000.0],
       ['Prof', 'B', 18.0, 18L, 'Female', 129000.0],
       ['Prof', 'A', 39.0, 36L, 'Female', 137000.0],
       ['AssocProf', 'A', 13.0, 8L, 'Female', 74830.0],
       ['AsstProf', 'B', 4.0, 2L, 'Female', 80225.0],
       ['AsstProf', 'B', 5.0, 0L, 'Female', 77000.0],
       ['Prof', 'B', 23.0, 19L, 'Female', 151768.0],
       ['Prof', 'B', 25.0, 25L, 'Female', 140096.0],
       ['AsstProf', 'B', 11.0, 3L, 'Female', 74692.0],
       ['AssocProf', 'B', 11.0, 11L, 'Female', 103613.0],
       ['Prof', 'B', 17.0, 17L, 'Female', 111512.0],
       ['Prof', 'B', 17.0, 18L, 'Female', 122960.0],
       ['AsstProf', 'B', 10.0, 5L, 'Female', 97032.0],
       ['Prof', 'B', 20.0, 14L, 'Female', 127512.0],
       ['Prof', 'A', 12.0, 0L, 'Female', 105000.0],
       ['AsstProf', 'A', 5.0, 3L, 'Female', 73500.0],
       ['AssocProf', 'A', 25.0, 22L, 'Female', 62884.0],
       ['AsstProf', 'A', 2.0, 0L, 'Female', 72500.0],
       ['AssocProf', 'A', 10.0, 8L, 'Female', 77500.0],
       ['AsstProf', 'A', 3.0, 1L, 'Female', 72500.0],
       ['Prof', 'B', 36.0, 26L, 'Female', 144651.0],
       ['AssocProf', 'B', 12.0, 10L, 'Female', 103994.0],
       ['AsstProf', 'B', 3.0, 3L, 'Female', 92000.0],
       ['AssocProf', 'B', 13.0, 10L, 'Female', 103750.0],
       ['AssocProf', 'B', 14.0, 7L, 'Female', 109650.0],
       ['Prof', 'A', 29.0, 27L, 'Female', 91000.0],
       ['AssocProf', 'A', 26.0, 24L, 'Female', 73300.0],
       ['Prof', 'A', 36.0, 19L, 'Female', 117555.0],
       ['AsstProf', 'A', 7.0, 6L, 'Female', 63100.0],
       ['Prof', 'A', 17.0, 11L, 'Female', 90450.0],
       ['AsstProf', 'A', 4.0, 2L, 'Female', 77500.0],
       ['Prof', 'A', 28.0, 7L, 'Female', 116450.0],
       ['AsstProf', 'A', 8.0, 3L, 'Female', 78500.0],
       ['AssocProf', 'B', 12.0, 9L, 'Female', 71065.0],
       ['Prof', 'B', 24.0, 15L, 'Female', 161101.0],
       ['Prof', 'B', 18.0, 10L, 'Female', 105450.0],
       ['AssocProf', 'B', 19.0, 6L, 'Female', 104542.0],
       ['Prof', 'B', 17.0, 17L, 'Female', 124312.0],
       ['Prof', 'A', 28.0, 14L, 'Female', 109954.0],
       ['Prof', 'A', 23.0, 15L, 'Female', 109646.0]], dtype=object)
"""

df.describe()   #only works on numeric data
                #nan is short for not a number and is a missing value
                #missing values will be represented by nan in data frame
"""
        phd    service         salary
count  76.000000  78.000000      76.000000
mean   19.605263  15.051282  108003.355263
std    12.508215  12.139768   28525.350088
min     1.000000   0.000000   57800.000000
25%    10.000000   5.250000   87250.000000
50%    18.500000  14.500000  104671.000000
75%    27.250000  20.750000  127077.750000
max    56.000000  51.000000  186960.000000
"""
#service column has two missing values that's why count is 76 instead of 78
#same goes for salary column

df.max()       
"""
rank            Prof
discipline         B
phd               56
service           51
sex             Male
salary        186960
dtype: object
"""

df.min()
"""
rank          AssocProf
discipline            A
phd                   1
service               0
sex              Female
salary            57800
dtype: object
"""

df.mean()
"""
phd            19.605263
service        15.051282
salary     108003.355263
dtype: float64
"""
df.median()
"""
phd            18.5
service        14.5
salary     104671.0
dtype: float64
"""

df.sample(5)        #Any random 5 records from the data frame
"""
rank discipline   phd  service     sex    salary
50   AsstProf          B  10.0        5  Female   97032.0
13       Prof          B   NaN       33    Male  162200.0
56  AssocProf          A  10.0        8  Female   77500.0
61  AssocProf          B  13.0       10  Female  103750.0
21       Prof          A  33.0       30    Male  103106.0
"""

df.head(5).mean()       #mean of first 5 records
"""
phd            30.2
service        24.8
salary     125296.0
dtype: float64
""""
df["phd"]       #data frame should only contain information under the phd column
"""0     56.0
1     12.0
2     23.0
3     40.0
4     20.0
5     20.0
6     20.0
7     18.0
8     29.0
9     51.0
10    39.0
11    23.0
12     1.0
13     NaN
14    25.0
15    17.0
16     8.0
17     4.0
18    19.0
19    29.0
20     4.0
21    33.0
22     4.0
23     2.0
24    30.0
25    35.0
26    38.0
27    45.0
28     7.0
29    21.0

48    17.0
49    17.0
50    10.0
51    20.0
52    12.0
53     5.0
54    25.0
55     2.0
56    10.0
57     3.0
58    36.0
59    12.0
60     3.0
61    13.0
62    14.0
63    29.0
64    26.0
65    36.0
66     7.0
67    17.0
68     4.0
69    28.0
70     8.0
71    12.0
72    24.0
73    18.0
74    19.0
75    17.0
76    28.0
77    23.0
Name: phd, Length: 78, dtype: float64
"""

df['rank']
df['rank'].value_counts()                  #returns the count of a particular value 
"""
Prof         46
AsstProf     19
AssocProf    13
Name: rank, dtype: int64
"""

df['rank'].value_counts(normalize=True)     #normalize means that the result will be given in percentage
"""
Prof         0.589744
AsstProf     0.243590
AssocProf    0.166667
Name: rank, dtype: float64
"""
df['salary'].mean()
"""
108003.3552631579
"""

df['salary'].describe()
"""
count        76.000000
mean     108003.355263
std       28525.350088
min       57800.000000
25%       87250.000000
50%      104671.000000
75%      127077.750000
max      186960.000000
Name: salary, dtype: float64
"""

df['salary'].count()
"""76"""

#FIILTER CONDITIONS

df_sub=df[(df['salary']>120000)]        #will select only those professors whose salary is greater than 120000

df_sub=df[(df['salary']>120000) & (df['phd']>10) & (df['sex']=='Female')]   #can apply three conditions using & operator
                                                                            #can use or opertor also

#SERIES DATA TYPE

#behaves like an array
#gives only rows values and no columns

s1=df[df['sex']=='Female']['salary']

s1.shape
"""(39L,)"""

#TYPE CASTING

DF1=pd.DataFrame(s1)     #converted series into data frame

type(s1) 
"""pandas.core.series.Series"""

type(DF1)
"""pandas.core.frame.DataFrame"""

df[['rank','salary']]   #selecting  two columns in the data frame

#METHOD LOC

df.loc[10:15,['rank','sex']]       #row selection,column selection
                                   #here the second value in slicing is included unlike in python strings
"""
     rank   sex
10      Prof  Male
11      Prof  Male
12  AsstProf  Male
13      Prof  Male
14      Prof  Male
15      Prof  Male
"""                                   
                             
df.loc[10:]

#METHOD ILOC

#index location
#row selection,column selection
#column selection will be given by index location
#here the second value in slicing is not included

df.iloc[2:10,[0,2,3]]
"""
 rank   phd  service
2       Prof  23.0       20
3       Prof  40.0       31
4       Prof  20.0       18
5       Prof  20.0       20
6  AssocProf  20.0       17
7       Prof  18.0       18
8       Prof  29.0       19
9       Prof  51.0       51
"""
                                   
df.iloc[0]      #only the first row
"""
rank            Prof
discipline         B
phd               56
service           49
sex             Male
salary        186960
Name: 0, dtype: object
"""

df.iloc[1:5, :-1]
"""
 rank discipline   phd  service   sex
1  Prof          A  12.0        6  Male
2  Prof          A  23.0       20  Male
3  Prof          A  40.0       31  Male
4  Prof          B  20.0       18  Male
"""
df.iloc[:,0]    #all rows and first column

df.iloc[:,-1]   #last column

df.iloc[0:7]    #first 7 rows

df.iloc[:,0:2]  #first 2 column

df.iloc[1:3,0:2]
"""
  rank discipline
1  Prof          A
2  Prof          A
"""

#READ A DATABASE WITH NULL VALUES

import pandas as pd
salary=pd.read_csv("Salaries.csv")

salary.isnull()

salary.isnull().any()           #by default takes columwise that is axis=0

salary.isnull().any(axis=0)     #when axis=0 then check columnwise
                                #when axis=1 then check rowwise
"""
rank          False
discipline    False
phd            True
service       False
sex           False
salary         True
dtype: bool
"""
salary.isnull().any(axis=1)
"""
0     False
1     False
2     False
3     False
4     False
5     False
6     False
7      True
8     False
9     False
10    False
11    False
12    False
13     True
14    False
15    False
16    False
17    False
18    False
19    False
20    False
21    False
22    False
23    False
24    False
25    False
26    False
27    False
28     True
29    False
 
48    False
49    False
50    False
51    False
52    False
53    False
54    False
55    False
56    False
57    False
58    False
59    False
60    False
61    False
62    False
63    False
64    False
65    False
66    False
67    False
68    False
69    False
70    False
71    False
72    False
73    False
74    False
75    False
76    False
77    False
Length: 78, dtype: bool
"""

salary[salary.isnull().any(axis=1)]     #makes a separate data frames based on null values that exist rowwise
"""
          rank discipline   phd  service   sex    salary
7        Prof          A  18.0       18  Male       NaN
13       Prof          B   NaN       33  Male  162200.0
28   AsstProf          B   7.0        2  Male       NaN
34  AssocProf          B   NaN        8  Male  119800.0
"""

salary[salary.isnull().any(axis=1)].head()
"""
         rank discipline   phd  service   sex    salary
7        Prof          A  18.0       18  Male       NaN
13       Prof          B   NaN       33  Male  162200.0
28   AsstProf          B   7.0        2  Male       NaN
34  AssocProf          B   NaN        8  Male  119800.0
"""

salary[salary.isnull().any(axis=1)].head(2)
"""
    rank discipline   phd  service   sex    salary
7   Prof          A  18.0       18  Male       NaN
13  Prof          B   NaN       33  Male  162200.0
"""

#DROP MISSING VALUES

new_df=salary.dropna()      #will delete the entire row if it has a missing value in any of the columns

#MISSING VALUE REPLACE
1.can replace by average
2.can replace by value with maximum frequency
3.can replace by the just preceeding value

salary=salary.fillna(salary['phd'].mean())

salary=salary.fillna(salary.mean())   #will automatically take mean for every column and replace missing value by mean