from bs4 import BeautifulSoup as soup
import requests
import lxml
from urllib.request import urlopen as uReq
import string
import re
import json
import pymysql
import time


# extracting from web
filename = "abc.csv"  #File Creation
f = open(filename , "w")  # File Write Function
header = "Abstracts\n"   #File Header Name
f.write(header)

n=1
while n <=6:    #Loop which control iteration of pages
   m = str(n)
   ul = 'https://link.springer.com/search/page/'+ m +'?facet-content-type=Article&facet-journal-id=13119&sortOrder=newestFirst'
   uclien = uReq(ul)   #main page link request
   page = uclien.read()   #page Reading
   uclien.close()

   psoup = soup(page, "html.parser")   #page parsing

   coniner = psoup.findAll("p", {"class": "title"})  #Extracting Clas name title becuase we require all the papers links

   for con in coniner:   #Now explore each title in the page
     ref = con.get('href')    #get href of each title
     murl = 'https://link.springer.com' + ref + ''
     uclen = uReq(murl)
     pag = uclen.read()
     uclen.close()

     psou = soup(pag, "html.parser")

     if(psou.find("a", {"class": "Para"})):  #find para class from page which contain abstracts
        coer = psou.find("a", {"class": "Para"})
        coer = coer.getText()
        coer = coer.replace(","," ")
        print (coer)

        try:
         f.write(coer + "\n")
        except:
            print("Exception")
   print (n)
   n = n+1
#time.sleep()

#print("Mission Complete") """
