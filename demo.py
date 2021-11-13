# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:16:53 2018

@author: MUJ
"""

#NUMPY LIBRARY
#used for mathematical operations on numerical data
#pandas inheritly uses numpy

import numpy as np

x=np.array([[1,2,3],[4,5,6]])   #converts the tuple or list data into a numpy array
                                #the type of different elements in the numpy array is int32 
                                #size is  (2,3) rows,columns
"""array([[1, 2, 3],
       [4, 5, 6]])"""

type(x)
""" numpy.ndarray"""           #numpy n dimensional array

print x.shape                  #(2L, 3L) returns a tuple as shape

x.dtype
""" dtype('int32')"""

x=np.float32(1.0)   
type(x)
"""numpy.float32"""

x=np.float64(1.0)
type(x)
"""numpy.float64"""

y=np.int_([1,2,4])               #will declare that individual items will be of int type

z=np.arange(20,dtype=np.uint8)    #u is unsigned int8 value that will be stored will take 8 bit
                                  #generates the data in series
                                  #dtype is data type here and we can exclusively determine the datatype
"""0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
"""

#WHEN YOU WANT TO PAD SOME DATA WE USE NP.ZEROS
#also used in image processing
#if dont want to use padding then use -fpack at compile time

#ZEROS
x=np.zeros((2,3))
"""
0	0	0
0	0	0
"""


x=np.zeros(2,3)     #data type not understood
                    #will take only one value as input
                    #thats why used a tuple in above example
x.dtype
"""dtype('float64')"""
    

type(x[0][0])    
""" numpy.float64"""           

#ONES
x=np.ones((2,3),dtype=np.int8)
"""
1	1	1
1	1	1
"""

x.dtype
"""dtype('int8')"""

#LINEAR SPACE
x=np.linspace(1,4,10,dtype=np.float64)   #(start number,end number,no of values to be generated between these two)
"""1
1.33333
1.66667
2
2.33333
2.66667
3
3.33333
3.66667
4
"""

#RANDOM VALUES
print np.random.random((2,3))           #random values always between 0 and 1
                                        #randomClass.randomFunction
"""[[ 0.37902067  0.72698027  0.2920645 ]
 [ 0.2375163   0.25138965  0.16008775]]"""

#SCALING
print np.random.random((2,3))*100   
"""[[  8.48194862  52.70692361  88.57042279]
 [ 44.6080646   65.26526212  39.72118098]]"""   #will scale values by 100

#ARANGE
a=np.arange(9)
print a
"""[0 1 2 3 4 5 6 7 8]"""

#RESHAPE
b=a.reshape(3,3)    #will reshape the above data 
                    #there will be no information loss
                    #dont write(2,3)
print b
"""
[[0 1 2]
 [3 4 5]
 [6 7 8]]"""

c=np.arange(8).reshape(2,2,2)
print c
"""[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]"""     #view by changing axis of c in variable explorer


a=np.arange(5)
b=np.arange(5)

#all operations menioned below dont change the initialized values

#ADDITION        #individual elements are added
print a+b
"""[0 2 4 6 8]"""

#SUBTRACTION
print a-b
"""[0 0 0 0 0]"""

#POWER
print a**2
"""[ 0  1  4  9 16]"""

#LOGICAL 
print a>3
"""[False False False False  True]"""

#SIN
print np.sin(a)
"""[ 0.          0.84147098  0.90929743  0.14112001 -0.7568025 ]"""

#MULTIPLICATION
print a*b
"""[ 0  1  4  9 16]"""


#NORNAL DISTRIBUTION
incomes=np.random.normal(27000,15000,10000)   #(central value also called median,standard deviation,total number of values to be generated)
#mean=median
#central+1 and central-1 combined has 60% data
#central+2 and centrall-2 combined has 95% data

np.mean(incomes)                   #values for mean and median are close
""" 26785.179108378488"""
np.median(incomes)
""" 26588.241285803073"""

#MATPLOT LIBRARY
#used for visualization

#HISTOGRAM
import matplotlib.pyplot as plt
plt.hist(incomes,20)               #output is given out as a histogram there will be 20 different bars displayed
plt.show                           #y axis here has the frequency    

￼
#APPENDING NEW VALUES
incomes=np.append(incomes,[100000000])   #appending ambanis high salary

np.median(incomes)
"""26588.241285803073"""

np.mean(incomes)
"""36778.823343709737"""

#that is by appending a value of high range then the median remains almost the same but the mean is highly changed
#thus median is not a correct parameter to judge when there is an outlier value in this came ambanis salary
#outlier value is identified by spike in graph given by matplot library using boxplot 

#BOXPLOT
plt.boxplot(incomes) 
#below value-min value
#above value-max value
#yellow line-median value
#circle values-outliers
#between min and yellow line (1st quadri)-25% data
#between yellow and box(2nd quadri)-25% data
#between box and max(3rd quadri)-25% data

#LINEAR RELATIONSHIP
import matplotlib.pyplot as plt

xs=[1,2,3,4,5]      #x axis
ys=[1,2,3,4,5]      #y axis
plt.plot(xs,ys)     #straight line

#LIST COMPREHENSION
xs=[1,2,3,4,5]
ys=[x**3 for x in xs]  #cube of every element in xs,for loop
plt.plot(xs,ys)        #curved 

xs=range(20)           
ys=[x**2 for x in xs]
plt.plot(xs,ys)   

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Matplotlib.Example")

plt.savefig("quad.jpg")  #will save the figure in the directory where your program is


x=np.arange(0,5,0.1)  #(start value,end value,stepping by value)
y=np.sin(x)
plt.plot(x,y)


#COLOR COORDINATING
t=np.arange(0.,5,0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')  #can write without color codes also it will automatically asign colors

#DETERMINING RANGE OF X AND Y AXIS
plt.axis([0,6,0,150])  #[range of x axis(0,6),range of y axis(0,150)]
plt.show()

#PIE CHART
names='CSE','ECE','IT','EE'
sizes=[15,30,25,10]

plt.pie(sizes,labels=names,autopct='%.4f%%')   #can display any number after decimal 
plt.show()

