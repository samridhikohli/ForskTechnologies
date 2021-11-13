# -*- coding: utf-8 -*-
"""
This is second python class
"""

#FOR LOOP
str1="Forsk Labs"

for item in str1:      #for loop,here item is not index but the value
    print item         """F
                        o
                        r
                        s
                        k
 
                        L
                        a
                        b
                        s
                        """

for x in str1:          #not necessarily to use item can use anything
    print x
    

number=10               #prints the odd numbers between 10 and 40
while number<40:
    if number%2!=0:
        print number
    number=number+1


number=10               #on getting value 20 it will exit
while number<30:
    if number==20:
        break
    print number
    number=number+1


number=10               #will print 10 to 29
while number<30:
    if number==20:
         number=number+1
         continue
    else:
        print number
        number=number+1
    
#LIST

list1=[1,2,3,4,5,6,7]    #strings are read only and immutable but we can change the lists 
                         #lists are mutable

list4=[1,'Jaipur']       #can have heterogenous data unlike array

type(list1)              #list
   
print list1[0:4]        #{1,2,3,4}

len(list1)              #7

list1.append(15)        #[1,2,3,4,5,6,7,15] inserts at the last

list1.insert(1,34)      #[1,34,2,3,4,5,6,7,15] inserts value at specified index 

list1[0]=56             #value overwritten that is it is not read only unlike string it is thus mutable

list1.sort()            #sorts in ascending order inplace sorting
print list1             #[2, 3, 4, 5, 6, 7, 15, 34, 56]

list1.reverse()         #[56, 34, 15, 7, 6, 5, 4, 3, 2]
print list1

list1.remove(34)        #[56, 15, 7, 6, 5, 4, 3, 2] checking from variable explorer if not used print


if 34 in list1:         #Item does not exist as already removed 34 in previous step
    list1.remove(34)
else:
    print"Item does not exist"
    

list1.find()            #Error no find method for list

list1.index(3)          #6 that is index of value 3 in list1 is 6

list1.pop()             #throws value 2 from the list (last number in list)

list2=[30,40,50]
list1.append(list2)     #[56, 15, 7, 6, 5, 4, 3, [30, 40, 50]] append the entire list2 after list1

print list1[7][2]       #50 (7th index row and 2nd index column)

list1.extend(list2)     #inserts individual items of list2 in list1
"""56
15
7
6
5
4
3
[30, 40, 50]
30
40
50
"""

for item in list2:
    list1.append(item)

del list1[0]                #delete element at index 0
                            #delete is not a method for list but a universal method
                    

list3=[1,2,3,3,2,2,5,6]     #[1, 3, 3, 5, 6] removing all 2s
for item in list3:
    if 2 in list3:
        list3.remove(2)
    else:
        continue
 
list3=[1,2,3,3,2,2,5,6]     
for item in list3:         #gives desired output but error as loop keeps iterating but cant find more 2s to remove
    list3.remove(2)


list3=[1,2,3,3,2,2,5,6]  
for item in list3:
    if item==2:            #mismatching of indexing does not give us correct output
        list3.remove(2)    #[1, 3, 3, 2, 5, 6]
        

list3=[1,2,3,3,2,2,5,6]
while 2 in list3:          #[1, 3, 3, 5, 6] removing all 2s optimal method
    list3.remove(2)
    

#FUNCTIONS
def add2(a,b):
    return a+b

add2(4,5)                 #9


def add2(a,b):
    print a+b
print add2(4,5)         #9(executing the add2 function prints a+b)
                        #None(function call gets returned none as no return type)
                
def add2(a,b=10):
    return a+b
print add2(4)           #14(4+10 b in this function is default value used when we dont specify value of b)
print add2(4,5)         #9(4+5 b is used as 5 and no use of default value 10)


def add2(a=10,b):       #error non-default argument follows default argument 
    return a+b          #cannot write default value first only allowed in the end
            
def add2(a=10,b=5):        
    return a+b
print add2(b=4,a=5)     #9(can explicitly change the order)


def add2(a,b):
    """This function adds two values"""
    return a+b
print add2(4,5)         #9(Doc string(string in triple quotes) will not be printed)
print add2.func_doc     #This function adds two values (Used to find the documented text in function)


a=[1,2]     
b=[1,2]

a==b        #True(Only checking the values inside the lists)

a is b      #False(Different memory for a and b,is valid for only same memory)

c=a
a is c      #True(Same memory of a and c)

#FILTER FUNCTION
def f(x):
    return x%3==0
f(3)    #True
f(4)    #False

list1=range(2,25)   #25 is excluded 
"""
output is
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
20
21
22
23
24
"""

filter(f,list1)     #[3, 6, 9, 12, 15, 18, 21, 24] 
                    #applies filter on list1 based on function f when it returns true
                    #second parameter should be iterable 

def f(x):
    return x%3     #non zero value treated as true and those values are thus filtered
list1=range(2,25)
filter(f,list1)
"""
output is [2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23]

"""

#MAP FUNCTION
def cube(x):
    return x**3
map(cube,[1,2,3,4,5])   #[1, 8, 27, 64, 125] cubes all items in list 
                    

#REDUCE FUNCTION                    
def add(x,y):
    return x+y
reduce(add,[1,2,3,4,5]) #15 adds all values 
                        #here x=1 and y=2 x+y=3 now returned value of x+y is x which is 3 and y is 3 and so on
                    
#hadoop(software for big data analyses)mainly uses map and reduce function
#python called functional programming language as we can pass functions as parameters
#but python is not a complete functional programming language
                        
#EXTRA DATA TYPE
tuple1=(1,3,4,5)
type(tuple1)          #tuple(tuples cannot be modified) 

#tuple different from list as it is immutable but list is mutable
#tuple different from string as tuple takes numbers and strings takes text

#DIVMOD FUNCTION
divmod(34,5)        #(6,4) gives quotient,remainder and the output is a tuple

q,r=divmod(34,5)    #unpacking of the tuple 
print q             #6
print r             #4
                    
x=(3)
type(x)             #int and not tuple for single number it will only be int
