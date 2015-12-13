from bs4 import BeautifulSoup 
import requests 
import sys 
import re

## get_link >> get_name & get_cash

class product(object):
    name = ""
    cash = ""
    link21 = []

    def set_name(self, url):
		requestResult = requests.get(url)
    	matches = re.findall('<b itemprop="name">[^<]*', requestResult.text)
    	self.name = matches[0].split(">")[1]

    def get_name(self):
		return self.name

    def set_cash(self, url):
		requestResult = requests.get(url)
		matches = re.findall('<i class="sale price">[^<]*', requestResult.text)
		self.cash = matches[0].split(">")[1]
	
    def get_cash(self):
		return self.cash

	def set_link(self, url):	# Pega o link de cada produto da pag
		#lista = []
    	i = 0
    	r = requests.get(url)
    	soup = BeautifulSoup(r.text)
    	
    	for a in soup.findAll('a',{'class':'link url'}):
    	    link = a['title']
    	    
    	    lista.append(link)
    	    links = str(link).strip('[]')
			self.link21[i] = links
			i += 1

		return False

	def get_link(self, pos):
		return self.link21[pos]

	#def set_DB(self, name, cash, link):
		#Conecta DB


