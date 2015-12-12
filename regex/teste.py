from ponto_frio_search import product
from bs4 import BeautifulSoup 
import requests 
import sys 

for arg in sys.argv:
    if arg == "-l":
        url = raw_input('>> ')
	produto = product()     
	
	produto.set_name(url)
	produto.set_cash(url)
	
	print produto.get_name()
	print produto.get_cash()
