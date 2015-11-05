#!/usr/bin/python
# -*- coding: latin-1 -*-
#from tabela import *
import requests

def valores(lista):

	compar = "sale price\">"
	nome = "<title>"
	nomjog = False
	valjog = False
	
	z=0
	w=0

	link = ""
	link2 = ""
	tam = len(lista)

	teste2 = True

	for y in xrange(0,tam):
		if((nome[z] == lista[y])):
			z = z + 1
			#w=0
			while(z == 7):	
				y = y +1
				if(teste2):
					y = y + 3
					teste2 = False
				if(y >= tam):
					z=0
				elif((lista[y] == "-") | (lista[y] == "<")):
					z=0
					nomjog = True
				else:
					link2+=lista[y]
				

		#if((compar[w] == lista[y])):
		#	w = w + 1
			#w=0
		#	while(w == 12):	
		#		w = w +1
		#		if(lista[y] == "R"):
		#			z=0
		#		else:						
		#			if(y >= tam):
		#				z=0
		#			elif(lista[y] == "<"):
		#				z=0
		#				valjog = True
		#			else:
		#				link+=lista[y]

		#if((compar[w] != lista[y])):
		#	w=0
		#if((nome[z] == lista[y])):
		#	z=0





		else:
			z=0

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
		print link2[:] + " # " + link
		#grafico(link2,link,line)
		#line = line +1
	else:
		print link2
