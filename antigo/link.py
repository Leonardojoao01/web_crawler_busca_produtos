#!/usr/bin/python
import requests
from valor import *

def links(lista):
	#print 
	compar = "url\" title=\""
	#compar = "title=\""
	z=0
	link = ""

	tam = len(lista)

	#for x in xrange(1,tam):
	if '<div class="hproduct"' in lista:
		for y in xrange(0,tam):

			if(compar[z] == lista[y]):
				z = z + 1
				w=0
				while(z == 12):	
					y = y +1
					if(y >= tam):
						z=0
					elif(lista[y] == "\""):
						z=0
						#print link

						html2 = requests.get(link)
						variavel2 = str(html2.content[:])
						valores(variavel2)


						link = ""
					else:
						link+=lista[y]
			else:
				z=0