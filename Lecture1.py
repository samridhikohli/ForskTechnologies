# -*- coding: utf-8 -*-
"""
Spyder Editor

This is first python class
"""


a=None      #decleration in python
            #it assigns the data type as the value entered for the variable
            #true is case sensitive use True
            #NULL in c is same as None in python (case sensitive)
            

type(a)     #will return the data type of a variable
            #a single char and even more than single char will be string type
            #double,single and double quotes doesnt matter for type
            
type(' ')   #will return str

int(3)      #will return int
float(3.2)  #will return float

print int(3.2) 

number=input("Enter the number: ")      #will store input in number

name=raw_input("Enter the name: ")     #will allow input of text 

type('7')       #will return str

type(int('7'))  #will return int (type casting converting str to int)

str1="Hello World"
len(str1)               #will return the length of string 
len("Welcome India")    #if execute  without print it will only show 13 and not 11

print len(str1)             #11
print len("Welcome India")  #13

print str1[0]       #H
print str1[0:5]     #Hello(starting index to end index but this end index is not included|SLICING)
print str1[4:]      #o world(strating index to end of string)
print str1[:8]      #Hello Wo(staring of string to 7 as 8 not included)
print str1[:]       #Hello World
print str1[-1]      #d(starting from back end is 0 so last letter is -1)
print str1[-1:-4]   #no output
print str1[0:8:2]   #HloW(starting from 0 till 7 with stepping of 2 start stepping from 0 only)
print str1[::-1]    #dlroW olleH(reverses the string)

str1==str1[::-1]    #false 

str1="Forsk Labs"
str2="Jaipur in MUJ"

print str1+str2          #conctenate without space
print str1+" "+str2      #with space
print str1,str2          #with space
print str1+32            #cannot concatenate diff data types
print str1+"32"          #can concatenate now

print str1.lower()       #convert str1 to lower case 
                         #but this does not overwrite the original string 
                         #str1 remains Forsk Labs

str1[0]='f'              #this is not allowed as str in read only write not allowed

print str1.find('Labs')  #6(starting index of this string)
print str1.find('labs')  #-1(index not found)

print str1.index('Labs')  #6
print str1.index('labs')  #error substring not found

str1="Hi from fine folks in Forsk"

print str1.split()        #splits it itno a list(array in C) of words
                          #['Hi', 'from', 'fine', 'folks', 'in', 'Forsk']
                          #by default splits based on space

print str1.split('f')     #will cut from f
                          #['Hi ', 'rom ', 'ine ', 'olks in Forsk']

str1="       Forsk Labs    "

print str1                #       Forsk Labs
print str1.strip()        #Forsk Labs(removes the extra spaces both in starting and ending)
                          
number=20

if number==10:            #If else statement NO SWITCH CASE IN PYTHON
    print "Yes"
else:
    print "No"
    
if number==10:            #If else if statement 
    print "Yes"
elif number==20:
    print "No"
    
while number<30:         #while loop
    print number 
    number=number+1        """20
                              21
                              22
                              23
                              24
                              25
                              26
                              27
                              28
                              29"""
                              
str1="Samridhi Kohli"
"""
Output:
    Kohli
    Samridhi
"""

list1=str1.split()      #1st method
print list1[1]
print list1[0]

print str1[9:]          #2nd method
print str1[0:9]

index=str1.find(" ")    #3rd method
print str1[index+1:]
print str1[:index]
