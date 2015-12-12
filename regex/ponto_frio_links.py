#from ponto_frio_valor import *

from bs4 import BeautifulSoup 
import requests 
import sys 

from ponto_frio_valor import *

def buscar_links(url):
    lista = []
    i = 0
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    for a in soup.findAll('a',{'class':'link url'}):#href=True):
        link = a['title']#a['href']
        i += 1
        lista.append(link)
        links = str(link).strip('[]')#.replace("u", "")#.replace("'", "")
        #print str(i) + ") " + str(links)
	buscar_links2(links)
	print links
    if i != 0:
	return True
   # print "\n>> Total = %d \n" % i
   # sys.exit() 
    return False

for arg in sys.argv:
    if arg == "-l":
       url = raw_input('>> ')
       buscar_links(url)
