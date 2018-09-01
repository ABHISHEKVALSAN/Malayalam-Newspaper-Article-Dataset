import requests
import codecs

from bs4 import BeautifulSoup

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
			txt			=soup.findAll("h1")[0].text\
							+"\n"+soup.findAll("div",{"class":"myd"})[1].text\
							+"\n"+soup.findAll("p",{"class":""})[0].text
			fname, year 		= conv2fname(soup.findAll("div",{"class":"myd"})[1].text)
			path			= "DataSet/"
			filename		=fname+str(i)+".utf8"
			filenameWithPath	=path+filename
			f=codecs.open(str(filename),'w','utf-8')
			f.write("<DOC>\n<DOCNO>"+filename+"</DOCNO>\n<TEXT>\n"+txt+"\n</TEXT>\n</DOC>")
			f.close()
			print("Writing file "+filename+" to "+path)
		else:
			print("File missing at "+url)
	else:
		print("error")
def main():
	for i in range(164676,800000):
		getdata(i)
if __name__=="__main__":
	main()
