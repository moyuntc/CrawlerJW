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


q = Queue.Queue()

domain_file = open("PData/L3all766.txt","r")

for url in domain_file:
    seedurl = url.strip()
    q.put(seedurl)

#mtest1=open("PData/L4Data"+str(j)+".txt","w")
#mtest1=open("PData/L3linkALL.txt","w")

i=1
j=8
#mtest1=open("PData/L3link"+str(j)+".txt","w")
memail=open("PData/email"+str(j)+".txt","w")
mphone=open("PData/phone"+str(j)+".txt","w")


while not q.empty():
    	
    url = q.get()
    subpage=urllib2.urlopen(url).read()

    subtemp=subpage.decode('utf8')

    soup=bs4.BeautifulSoup(subtemp)
    links=soup.find_all('tr')

# page=urllib2.urlopen('http://www.myshopping.com.au/SI--811__Shop_Inside_Homewares_Gifts').read()

#http://www.myshopping.com.au/SI--2678__Dungeon_Crawl    #no email 
# http://www.myshopping.com.au/SI--21430508__247Deals_com_au

#temp = page.decode('utf8')#.encode("ascii","ignore")
#soup=bs4.BeautifulSoup(temp) #from_encoding="unicode"

# for  anchor in links:
#a=soup.find_all('td')
	#print anchor.get('href', '/')
	# if anchor.text=="Phone":	
	# 	print "PhoneNo."+a
	# else: 
	# 	print "none"
 #anchor.text

    em=soup.findAll(text=re.compile("@"))
    if em:
	    memail.write(em[0]+"\n")
	    print em[0]
    else:
	    memail.write("None\n") 
	    print url
    


    # ph=soup.findAll(text=re.compile("03"))
    # if ph:

    # else:
	   #  mphone.write("None\n")
    phoneid = soup.find(attrs={"class":"siDtV"});
 # print type(phoneid)
    if phoneid: 
    	mphone.write(phoneid.string+"\n")
	print phoneid.string
    else: 
    	mphone.write("None"+"\n")

    print i
    i=i+1
    bePolite(True)
	
    if i>100:
    	j=j+1
    	i=1
    	memail.close()
    	mphone.close()
    	memail=open("PData/email"+str(j)+".txt","w")
    	mphone=open("PData/phone"+str(j)+".txt","w")
	time.sleep(120)

    	# if(phoneid=="Phone"):
    	# 	print phoneid.string
     #    		phoneid = soup.find(attrs={"class":"siDtT"});	


	                           #  <div style="padding-bottom:10px"></div>
                            # <table>
                            #     <tbody>
                            #         <tr>
                            #             <td class="siDtT">

                            #                 Phone

                            #             </td>
                            #             <td class="siDtV">

                            #                 03 9931 0160

                            #             </td>
                            #         </tr>
                            #         <tr>
                            #             <td class="siDtT">

                            #                 Fax

                            #             </td>
                            #             <td class="siDtV">

                            #                 03 9931 0114

                            #             </td>
                            #         </tr>
                            #         <tr>
                            #             <td class="siDtT">

                            #                 Email

                            #             </td>
                            #             <td class="siDtV">

                            #                 support@comeinside.com.au

                            #             </td>
                            #         </tr>
                            #         <tr></tr>
                            #         <tr></tr>


#
# mtest3=open("email.txt","w")

# mtest2=open("phone.txt","w")

# #

# import re
# q = Queue.Queue()

# match=re.compile('^http://www.myshopping.com.au/PT--185_Toys_Games__*')

# for anchor in links:
#     matched=re.match(match,anchor.get('href', '/'))
#     if matched:
# #    print anchor.body
#         title = anchor.text
#         title = title.replace(u'\xae','')
#         mtest2.write(title+'\n')
        
#         mtest3.write(anchor.get('href', '/')+'\n')
        

# # mtest3.close()
#        # print(anchor.get('href', '/'))


# mtest3.close()
# mtest2.close()


# #-------------------------------------------------------------
# domain_file = open("L1link.txt","r")

# for url in domain_file:
#     seedurl = url.strip()
#     q.put(seedurl)

# submatch=re.compile('^http://www.myshopping.com.au/SI--*')
# mtest1=open("L3link.txt","w")
# while not q.empty():
	
#     url = q.get()
#     subpage=urllib2.urlopen(url).read()

#     subtemp=subpage.decode('utf8')

#     soup=bs4.BeautifulSoup(subtemp)
#     #subcontent=soup.prettify()
#     sublinks=soup.find_all('a')

#     for subanchor in sublinks:
#        	submatched=re.match(submatch,subanchor.get('href', '/'))
#         if submatched:
#             print subanchor.get('href','/')
#             mtest1.write(subanchor.get('href', '/')+'\n') 
#             break
#     bePolite(True,3)

# mtest1.close()


# http://www.myshopping.com.au/SI--21430508__247Deals_com_au