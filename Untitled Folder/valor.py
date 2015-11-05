#!/usr/bin/python
# -*- coding: latin-1 -*-
import requests

def valores(lista):

	compar = "sale price\">"
	nome = "<title>"
	nomjog = False
	valjog = False
	z=0

	link = ""
	link2 = ""
	tam = len(lista)

	teste2 = True

	for y in xrange(0,tam):
		if((nome[z] == lista[y])):
			z = z + 1
			w=0
			while(z == 7):	
				y = y +1
				if(teste2):
					y = y + 3
				if(y >= tam):
					z=0
				elif((lista[y] == "-") | (lista[y] == "<")):
					z=0
					nomjog = True
					
				else:
					link2+=lista[y]
				teste2 = False
		else:
			z=0

	for y in xrange(0,tam):

		if((compar[z] == lista[y])):
			z = z + 1
			w=0
			while(z == 12):	
				y = y +1
				if(lista[y] == "R"):
					z=0
				else:						
					if(y >= tam):
						z=0
					elif(lista[y] == "<"):
						z=0
						valjog = True
					else:
						link+=lista[y]
		else:
			z=0
	z=0

	if(valjog & nomjog):
		print link2 + " # " + link
	else:
		print link2
