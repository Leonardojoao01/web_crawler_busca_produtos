from bs4 import BeautifulSoup 
import requests 
import sys 
import re

class product(object):
    name = ""
    cash = ""
    
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
