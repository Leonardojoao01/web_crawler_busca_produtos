from link import *
import requests

import urllib2
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread

val = 0

for x in xrange(1,10):
	link = ("http://search.pontofrio.com.br/search?p=Q&lbc=pontofrio-br&uid=383564926&ts=custom&w=jogos%20de%20xbox%20360&af=&isort=score&method=and&view=grid&srt="+str(val))

	html = requests.get(link) #Baixa o html da pagina

	variavel = str(html.content[:])


	links(variavel)
	val = val + 20

#--------------------------------------------------------------

#urls = [
#	'http://search.pontofrio.com.br/search?p=Q&lbc=pontofrio-br&uid=383564926&ts=custom&w=jogos%20de%20xbox%20360&af=&isort=score&method=and&view=grid&srt=00',
#	'http://search.pontofrio.com.br/search?p=Q&lbc=pontofrio-br&uid=383564926&ts=custom&w=jogos%20de%20xbox%20360&af=&isort=score&method=and&view=grid&srt=20',
#	'http://search.pontofrio.com.br/search?p=Q&lbc=pontofrio-br&uid=383564926&ts=custom&w=jogos%20de%20xbox%20360&af=&isort=score&method=and&view=grid&srt=60',
#	'http://search.pontofrio.com.br/search?p=Q&lbc=pontofrio-br&uid=383564926&ts=custom&w=jogos%20de%20xbox%20360&af=&isort=score&method=and&view=grid&srt=80'
#]

#thread1 = Thread(target=links(str(requests.get(urls[0]).content[:])))
#thread2 = Thread(target=links(str(requests.get(urls[1]).content[:])))
#thread3 = Thread(target=links(str(requests.get(urls[2]).content[:])))
#thread4 = Thread(target=links(str(requests.get(urls[3]).content[:])))

#thread1.start()
#thread2.start()
#thread3.start()
#thread4.start()

#thread1.join()
#thread2.join()
#thread3.join()
#thread4.join()
