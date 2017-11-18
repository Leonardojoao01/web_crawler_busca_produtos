from ponto_frio_links import *
import requests

import urllib2
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread

val = 1
pagina = True


while pagina == True:
	link = ("https://search.pontofrio.com.br/?strBusca=jogos%20xbox%20360&paginaAtual="+str(val))

	#html = requests.get(link) #Baixa o html da pagina

	#variavel = str(html.content[:])

	pagina = buscar_links(link)
	val = val + 1
	print val
