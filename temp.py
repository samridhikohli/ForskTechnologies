# -*- coding: utf-8 -*-
"""
Created on Mon Oct 01 17:42:06 2018

@author: MUJ
"""
#JSON ARRAY CONTAINING TWO JSON OBJECTS
#JSONLINT.COM
#JSON NOT RELATED TO JAVASCRIPT 
#IT IS SUPPORTED BY ALL PROGRAMMING LANGUAGES
[
{
  "Name : "Raj Kumar",
  "Vehicle No : "DL5CC9241",
  "Model" : "Honda",
  "Status" : true,
  "mobile" : 9660407467         #if adding country code +91 then it will be a string and not a number
                                #"mobile": ["+91-9660407467", "966752421"] can be an array also
},
{
  "Name : "Ram",
  "Vehicle No : "RJ14XXXXXX",
  "Model" : "Maruti",
  "Status" : false
}
]
#data types allowed are boolean,number,array,string 

#CLIENT SERVER COMMUNICATION

#API
1.we use apis for connection and we get a unique id 
2.string after ? is called querry string 


#API METHODS
1.get method
2.post method


#REST API ALSO CALLED WEB SERVICE
url="http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=e9185b28e9969fb7a300801eb026de9c"


#Using urlib2 library
#Method 1 to get data
import urllib2
resp=urllib2.urlopen(url)   
print resp.read()           #read method in the library
"""{"coord":{"lon":75.82,"lat":26.92},"weather":[{"id":721,"main":"Haze","description":"haze","icon":"50d"}],"base":"stations","main":{"temp":308.15,"pressure":1010,"humidity":26,"temp_min":308.15,"temp_max":308.15},"visibility":5000,"wind":{"speed":2.6,"deg":320},"clouds":{"all":0},"dt":1538395200,"sys":{"type":1,"id":7814,"message":0.0018,"country":"IN","sunrise":1538354961,"sunset":1538397771},"id":1269515,"name":"Jaipur","cod":200}"""
#this is the same output shown in the web browser


#Using requests library
#Method 2 to get data
import requests            
resp=requests.get(url)
print resp.text
"""{"coord":{"lon":75.82,"lat":26.92},"weather":[{"id":721,"main":"Haze","description":"haze","icon":"50d"}],"base":"stations","main":{"temp":308.15,"pressure":1010,"humidity":26,"temp_min":308.15,"temp_max":308.15},"visibility":5000,"wind":{"speed":2.6,"deg":320},"clouds":{"all":0},"dt":1538395200,"sys":{"type":1,"id":7814,"message":0.0018,"country":"IN","sunrise":1538354961,"sunset":1538397771},"id":1269515,"name":"Jaipur","cod":200}"""
#this is the same output shown in the web browser

#POST AND GET METHOD
data={
         "Phone Number": "9660407467",
         "Name": "Samridhi",
         "College_Name": "MUJ",
         "Branch": "IT"
      }

#Rest API is different than normal URL as API does not create a UI it just gives back data in JSON form but URL gives UI in HTML/CSS format

#WEB SCRAPPING
import urllib2
wiki="https://wordpandit.com/29-states-capitals/"
page=urllib2.urlopen(wiki)          #validates the connection

from bs4 import BeautifulSoup
soup=BeautifulSoup(page)            #will store the entire html data in soup
print soup

right_table=soup.find('table',class_='alignleft')    #finding the table from the entire data received of the website in soup

A=[]    #empty lists to store the columns in the table
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.findAll("tr"):
    cells=row.findAll("td")
    
    A.append(cells[0].find(text=True))
    B.append(cells[1].find(text=True))
    C.append(cells[2].find(text=True))
    D.append(cells[3].find(text=True))
    E.append(cells[4].find(text=True))
    F.append(cells[5].find(text=True))
    
"""
LIST A
S.no
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
20
21
22
23
24
25
26

LIST B
States
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chhattisgarh
Goa
Gujarat
Haryana
Himachal Pradesh
Jammu & Kashmir
Jharkhand
Karnataka
Kerala
Madhya Pradesh
Maharashtra
Manipur
Meghalaya
Mizoram
Nagaland
Odisha (Orissa)
Punjab
Rajasthan
Sikkim
Tamil Nadu
Telangana (29th — State of India from June 2, 2014)
Tripura
Uttar Pradesh
Uttarakhand

LIST C
Capital
Amravathi (on 2nd June 2014)
Itanagar
Dispur
Patna
Raipur
Panaji
Gandhinagar
Chandigarh (shared with Punjab)
Simla, Dharamsala
Srinagar (Summer) Jammu (Winter)
Ranchi
Bengaluru
Thiruvananthapuram
Bhopal
Mumbai
Imphal
Shillong
Aizawl
Kohima
Bhubaneshwar
Chandigarh (shared with Haryana)
Jaipur
Gangtok
Chennai
Hyderabad
Agartala
Lucknow
Dehradun
Kolkata

LIST D
Chief Minister
Chandrababu Naidu
Pema Khandu
Sarbananda Sonowal
Nitish Kumar
Raman Singh
Manohar Parrikar
Vijay Rupani
Manohar Lal Khatter
Jai Ram Thakur
Mehbooba Mohammed Sayeed
Raghubar Das
HD Kumaraswamy
Pinarayi Vijayan
Shivraj Singh Chauhan
Devendra Fadnavis
Biren Singh (Ex-footballer)
Conrad Sangma
Pu Lalthanhawla
Neiphiu Rio
Naveen Patnaik
Capt Amrinder Singh
Vasundhara Raje
Pawan Chamling
Edapadi Palanisamy
K Chandrashekhar Rao
Biplab Kumar Deb
Yogi Adityanath

LIST E
Political party
(TDP)
(PPA)
(BJP)
(JDU)
(BJP)
(BJP)
(BJP)
(BJP)
(BJP)
(PDP)
(BJP)
(Congress in alliance with JDS)
(CPM)
(BJP)
(BJP)
(BJP)
(Congress)
(Congress)
(Nagaland People’s Front)
(BJD)
 (Congress)
(BJP)
(SDF)
(AIADMK)
(TRS)
 (BJP)
(BJP)
(BJP)

LIST F
Governor
E.S Lakshmi Narasimhan
B.D.Mishra
Jagdish Mukhi
Lalji Tandon
Balram Dass Tandon
Mridula Sinha
Om Prakash Kohli
Satyadev Narayan Arya
Acharya Dev Vrat
Satya Pal Malik
Draupadi Murmu
Vajubhai Vala
P. Sathasivam
Anandiben Patel
Chennamaneni Vidyasagar Rao
Najma Heptulla
Tathagata Roy
Kummanam Rajasekharan
Padmanabha
 Ganeshi Lal
V. P. Singh Badnore
Kalyan Singh
Ganga Prasad
Banwarilal Purohit
E.S Lakshmi Narasimhan
Kaptan Singh Solanki
Ram Naik

"""

#NOW WE CONNACTENATE ALL OF THESE LISTS INTO A SINGLE ENTITY CALLED DATA FRAME USING PANDAS