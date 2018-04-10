import requests
from bs4 import BeautifulSoup
import os
'''i=0
arr={}'''
headers={ 'User-Agent': 'Wikiscraper 1.0'
		}
f=open("./Wordlist.txt", 'w+')
source_code=requests.get("https://en.wiktionary.org/wiki/Appendix:1000_basic_English_words", headers=headers)
text=source_code.text
soup=BeautifulSoup(text)
for link in soup.findAll('div', {'class':'mw-content-ltr'}):
	soup1=BeautifulSoup(str(link))
	'''for link1 in soup1.findAll('b'):
		arr[i]=link1.string
		i=i+1'''
	for link2 in soup1.findAll('dl'):
		soup2=BeautifulSoup(str(link2))
		for link3 in soup2.findAll('a'):
			f.write(link3.string+"\n")
		f.write("\n")
f.close()
