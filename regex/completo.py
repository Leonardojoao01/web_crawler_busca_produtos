from ponto_frio_links import *
import requests

import urllib2
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread

val = 0
pagina = True


while pagina == True:
	link = ("http://search.pontofrio.com.br/search?p=Q&lbc=pontofrio-br&uid=383564926&ts=custom&w=jogos%20de%20xbox%20360&af=&isort=score&method=and&view=grid&srt="+str(val))

	#html = requests.get(link) #Baixa o html da pagina

	#variavel = str(html.content[:])

	pagina = buscar_links(link)
	val = val + 20
	print val
