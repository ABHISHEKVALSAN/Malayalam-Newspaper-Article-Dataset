"""





"""

import requests
import codecs
import errno
import os
from bs4 import BeautifulSoup
import os
def mon2dig(month):
	if month=="January":
		return "01"
	elif month=="February":
		return "02"
	elif month=="March":
		return "03"
	elif month=="April":
		return "04"
	elif month=="May":
		return "05"
	elif month=="June":
		return "06"
	elif month=="July":
		return "07"
	elif month=="August":
		return "08"
	elif month=="September":
		return "09"
	elif month=="October":
		return "10"
	elif month=="November":
		return "11"
	elif month=="December":
		return "12"
	else:
		return "00"
def conv2fname(s):
	flist=s.split()
	m=mon2dig(flist[2])
	if int(flist[1])<10:
		filename="1"+flist[3][2:]+m+"0"+flist[1]
	else:
		filename="1"+flist[3][2:]+m+flist[1]
	return filename,flist[3]

def getdata(i):
	url="https://www.janmabhumidaily.com/news"+str(i)
	resp=requests.get(url)
	if resp.status_code==200:
		soup=BeautifulSoup(resp.text,'html.parser')
		links =soup.findAll("p",{"class":"text-center"})
		if len(links) != 1:
			


			txt=soup.findAll("h1")[0].text
			txt+="\n"+soup.findAll("div",{"class":"myd"})[1].text
			txt+="\n"+soup.findAll("p",{"class":""})[0].text
			

			fname, year = conv2fname(soup.findAll("div",{"class":"myd"})[1].text)
			
			path= #"/home/abhi/Desktop/ir/project/JB/"+year+"/"
			ext=str(i)
			filename=path+fname+ext+".utf8"
			
			f=codecs.open(str(filename),'w','utf-8')
			f.write("<DOC>\n<DOCNO>"+fname+ext+".utf8</DOCNO>\n<TEXT>\n"+txt+"\n</TEXT>\n</DOC>")
			f.close()
	else:
		print "error"
for i in xrange(500000,800000):
	if i%100==0:
		print i
	getdata(i)
