from bs4 import BeautifulSoup 
import requests 
import sys 
import re

## get_link >> get_name & get_cash

class product(object):
	name = ""
	cash = ""
	url = ""

	def __init__(self, url):
		self.url = url

	def set_name(self):
		requestResult = requests.get(self.url)
		matches = re.findall('<b itemprop="name">[^<]*', requestResult.text)
		self.name = matches[0].split(">")[1]

	def get_name(self):
		return self.name

	def set_cash(self):
		requestResult = requests.get(self.url)
		matches = re.findall('<i class="sale price">[^<]*', requestResult.text)
		self.cash = matches[0].split(">")[1]
	
	def get_cash(self):
		return self.cash

	def update(self):
		#if(self.name == ""):
		self.set_name()
		self.set_cash()
			
	def get_url(self):
		return self.url
	#def set_DB(self, name, cash, link):
		#Conecta DB