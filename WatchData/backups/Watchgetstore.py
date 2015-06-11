# from BeautifulSoup import BeautifulSoup



import sys
import os
import Queue
import bs4
import urllib2
import hashlib
import pprint
from random import randint
import time
from config import *
from jsengine import *

import re

def bePolite(should_i,random = 2):
    if should_i == True:
        randseed = randint(1,random)
        time.sleep(randseed)



page=urllib2.urlopen('http://www.myshopping.com.au/PT--11_Watches__fs_g111111_e__').read()


temp = page.decode('utf8')#.encode("ascii","ignore")
#if JAVASCRIPT_BOOL == 0:
#mtest2=open("mtestB.txt","w")
#mtest2.write("url:"+"\n"+ temp)
#mtest2.close()

#content = bs4.BeautifulSoup(content,from_encoding='GB18030')

#-------------------------------------------------------------------------------------------  Read Main Page of Category shops
soup=bs4.BeautifulSoup(temp)#from_encoding="unicode"
content=soup.prettify()


#print content

links=soup.find_all('a')
#print links.prettify()
#
mtest3=open("WatchData/L1link.txt","w")

mtest2=open("WatchData/L2name.txt","w")

#



match=re.compile('^http://www.myshopping.com.au/PT--11_Watches__fs_c*')

for anchor in links:
    matched=re.match(match,anchor.get('href', '/'))
    if matched:
#    print anchor.body
        title = anchor.text
        title = title.replace(u'\xae','')
        mtest2.write(title+'\n')
        
        mtest3.write(anchor.get('href', '/')+'\n')
        

# mtest3.close()
       # print(anchor.get('href', '/'))
mtest3.close()
mtest2.close()
#--------------------------------------------------------------------------------------------------------------------

#-----------Read Second Level Page  //  100contacts per file. in case of socket error 

q = Queue.Queue()

domain_file = open("WatchData/L1link.txt","r")

for url in domain_file:
    seedurl = url.strip()
    q.put(seedurl)	

submatch=re.compile('^http://www.myshopping.com.au/SI--*')



i=1
j=1
mtest1=open("WatchData/L3link"+str(j)+".txt","w")
#mtest1=open("PData/L3linkALL.txt","w")

while not q.empty():
    	
    url = q.get()
    subpage=urllib2.urlopen(url).read()

    subtemp=subpage.decode('utf8')

    soup=bs4.BeautifulSoup(subtemp)
    #subcontent=soup.prettify()
    sublinks=soup.find_all('a')
    
    
    

    for subanchor in sublinks:
       	submatched=re.match(submatch,subanchor.get('href', '/'))
        if submatched:
 
            print subanchor.get('href','/')
            mtest1.write(subanchor.get('href', '/')+'\n') 
            break
    

 #   print randseed
   
    print i
    i=i+1
    bePolite(True)

    if i>100:
    	j=j+1
    	i=1
    	time.sleep(120)
    	mtest1.close()
    	mtest1=open("AutoData/L3link"+str(j)+".txt","w")

