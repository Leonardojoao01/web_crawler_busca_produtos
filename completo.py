from link import *
import requests

val = 0
#val = 1

for x in xrange(1,6):
	link = ("http://search.pontofrio.com.br/search?p=Q&lbc=pontofrio-br&uid=383564926&ts=custom&w=jogos%20de%20xbox%20360&af=&isort=score&method=and&view=grid&srt="+str(val))

	#link = ("http://busca.americanas.com.br/busca.php?q=jogos+xbox+360&page="+str(val))

	html = requests.get(link) #Baixa o html da pagina

	variavel = str(html.content[:])

#print variavel

	links(variavel)
	val = val + 20
	#val = val + 1