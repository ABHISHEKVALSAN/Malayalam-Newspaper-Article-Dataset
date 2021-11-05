
import requests
from bs4 import BeautifulSoup

def mon2dig(month):
	month_dict = {'January': '01', 'February': '02', 'March': '03',
					'April': '04', 'May': '05', 'June': '06', 'July': '07',
					'August': '08', 'September': '09', 'October': '10',
					'November': '11', 'December': '12'}
	return month_dict.get(month,'00')

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
			f=open(str(filenameWithPath),'w+')
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
