from link import *
import requests

val = 0

for x in xrange(1,3):
	link = ("http://search.pontofrio.com.br/search?p=Q&lbc=pontofrio-br&uid=383564926&ts=custom&w=jogos%20de%20xbox%20360&af=&isort=score&method=and&view=grid&srt="+str(val))

	#link = ("http://busca.americanas.com.br/busca.php?q=jogos+xbox+360&page=2")

#link = "http://www.pontofrio.com.br/Games/Xbox360/JogosXbox360/Jogo-Pro-Evolution-Soccer-2016-Xbox-360-5452355.html"

	html = requests.get(link) #Baixa o html da pagina

	variavel = str(html.content[:])

#print variavel

	links(variavel)
	val = val + 10