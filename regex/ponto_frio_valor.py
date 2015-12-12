from bs4 import BeautifulSoup 
import requests 
import sys 
import re

def buscar_links2(url):
    requestResult = requests.get(url)
   
    matches = re.findall('<b itemprop="name">[^<]*', requestResult.text)
    print matches[0].split(">")[1]

    matches = re.findall('<i class="sale price">[^<]*', requestResult.text)
	
   # print matches   
    print  matches[0].split(">")[1]

for arg in sys.argv:
    if arg == "-l":
       url = raw_input('>> ')
       buscar_links2(url)
