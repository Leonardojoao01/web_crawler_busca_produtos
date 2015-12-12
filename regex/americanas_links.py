from bs4 import BeautifulSoup 
import requests 
import sys 

def buscar_links(url):
    lista = []
    i = 0
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    for a in soup.findAll('a',{'class':'url'}):#href=True):
        link = a['href']
        i += 1
        lista.append(link)
        links = str(link).strip('[]')#.replace("u", "")#.replace("'", "")
        print str(i) + ") " + str(links)
	
    if i == 0:
	print "Nenhum item"
	
    print "\n>> Total = %d \n" % i
    #sys.exit() 

for arg in sys.argv:
    while arg == "-l":
       url = raw_input('>> ')
       buscar_links(url)
