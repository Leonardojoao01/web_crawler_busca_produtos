from ponto_frio_search import product
from bs4 import BeautifulSoup 
import requests 
import sys 

for arg in sys.argv:
    if arg == "-l":
        url = raw_input('>> ')
	produto = product(url)     
	
	#link = []
	#produto.set_link(url)
	produto.update()
	#link = produto.get_link()
	
	print produto.get_url()

	#produto.set_name()
	#produto.set_cash()
	
	print produto.get_name()
	print produto.get_cash()
