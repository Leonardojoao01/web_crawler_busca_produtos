from bs4 import BeautifulSoup 
import requests 
import sys 
import re

class hamper(object):
    products = []
    
    def set_link(self, url):	# Pega o link de cada produto da pag
		lista = []
		i = 0
		r = requests.get(url)
		soup = BeautifulSoup(r.text)
    	
		for a in soup.findAll('a',{'class':'link url'}):
			link = a['title']
			lista.append(link)
			links = str(link).strip('[]')
            
			self.products.append(links)
			i += 1
		#return False
		
		def get_link(self):
			return self.products