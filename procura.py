#!/usr/bin/python

ficheiro = open("tes5.txt")#,"r") 
lista = ficheiro.readlines() 
i=0

compar = "title="
z=0
link = "leo"

while(lista != "\0"):
	i=0

	tam = len(lista)
	

	
	while(lista[i] != "\0"):
		#print lista[i]
		if '<div class="hproduct"' in lista[i]:
			#print lista[i+1]
			#Pegar o link aqui
			palavra = lista[i+1]
			#j=0
			print palavra
			#while(palavra[j]) :
				#print palavra[j]
				#    title="
			#	while(compar[z] == palavra[j]):
					
			#		while(z==5):
			#			if(palavra[j] == "\""):
			#				z=0
						#link = palavra[j]
						#link.append(palavra[j])
			#			j = j+1

 			#		z = z+1
			#		j = j+1
			#	j = j + 1
			#print link		

				

		#print lista[19]

		i = i + 1
	#print lista[10]
	lista = ficheiro.readlines()

#ficheiro.close()