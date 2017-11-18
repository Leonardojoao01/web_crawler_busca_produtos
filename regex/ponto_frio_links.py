# -*- encoding: utf-8 -*-
#from ponto_frio_valor import *

from bs4 import BeautifulSoup 
import requests 
import sys 

from ponto_frio_valor import *

def buscar_links(url):
    lista = []
    i = 0
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")     # N lembro, tem haver com a biblioteca de PARSE
    #print soup.findAll('a',{'class':'link url'})
    for a in soup.findAll('a',{'class':'link url'}):#href=True):    # Procura dentro o códido HTML essa conf, para depois encontrar o link
        #link = a['title']#a['href']
        link = a['href']        # HREF é a tag onde encontra-se o link para acessar o jogo
        #print link
        i += 1
        lista.append(link)      # Adicina os links do produtos em uma pilha/fila para posteriormente acessar os produtos
        #links = str(link).strip('[]')#.replace("u", "")#.replace("'", "")
    
    for link_produto in lista:             # Percorre a lista em busca dos links

      buscar_links2(link_produto)          # Chama o método para acessar o produto, pegando o nome e valor 
    #print lista
  #  if i != 0:
    return True
   # print "\n>> Total = %d \n" % i
   # sys.exit() 
   # return False

for arg in sys.argv:
    if arg == "-l":
       url = raw_input('>> ')
       buscar_links(url)
