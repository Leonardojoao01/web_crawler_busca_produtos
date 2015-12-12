import requests
#response = requests.get("http://search.pontofrio.com.br/search?w=jogos%20xbox%20360&utm_source=GP_Search&utm_medium=Cpc&utm_campaign=INST_Ponto_Frio")#, params={'q': 'busca qualquer coisa'})

#response = requests.get("http://www.pontofrio.com.br/Games/Xbox360/JogosXbox360/Jogo-Minecraft-Xbox-360-2266425.html")

response = requests.get("http://www.pontofrio.com.br/Games/Xbox360/JogosXbox360/Jogo-Call-of-Duty-Black-Ops-Xbox-360-266153.html")

#teste = "http://www.pontofrio.com.br/Games/Xbox360/JogosXbox360/Jogo-Pro-Evolution-Soccer-2016-Xbox-360-5452355.html"

#response = requests.get("http://produto.pontofrio.com.br/2266425?")# rel="product" href="http://search.pontofrio.com.br/search?p=R&srid=S1-2IADP&lbc=pontofrio-br&w=jogos%20xbox%20360&url=http%3a%2f%2fproduto.pontofrio.com.br%2f2266425%3f&rk=1&uid=390329640&sid=2&ts=custom&rsc=AjSE7B3UCy7XXah7&method=and&isort=score&view=grid&utm_source=GP_Search&utm_medium=Cpc&utm_campaign=INST_Ponto_Frio")

#response = requests.get(teste)

#print response.status_code

print response.content[:]
