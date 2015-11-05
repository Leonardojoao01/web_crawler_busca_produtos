#!/usr/bin/python

ficheiro = open("jogo.txt")#,"r") 
lista = ficheiro.readlines() 
i=0

compar = "lowPrice\">R$ "
z=0
link = ""

while(lista):
	tam = len(lista)
	
	for x in xrange(0,tam):
		
		if '<span class="lowPrice">' in lista[x]:
			palavra = lista[x]
			#print palavra
			tam2 = len(palavra) # Tamanho da String com o LINK
			#print tam2
			z=0

			for y in xrange(0,tam2):
				if(compar[z] == palavra[y]):
					z = z + 1
					w=0
					while(z == 13):	
						y = y +1
						if(y >= tam2):
							z=0
						elif(palavra[y] == "<"):
							z=0
							print link
							link = ""
						else:
							link+=palavra[y]
				else:
					z=0

	lista = ficheiro.readlines()
			
ficheiro.close()