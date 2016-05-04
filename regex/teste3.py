from ponto_frio_hamper import hamper
from bs4 import BeautifulSoup 
import requests 
import sys 

for arg in sys.argv:
    if arg == "-l":
        url = raw_input('>> ')
	produto = hamper()  
	produto.set_link(url)
	print produto.get_link()