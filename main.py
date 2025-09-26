# pandas
import pandas as pd

# web scraping
import requests

from bs4 import BeautifulSoup

# faz a requisição
pagina = requests.get("https://books.toscrape.com/catalogue/category/books/mystery_3/index.html")
# cria o objeto BeautifulSoup
dadosPagina = BeautifulSoup(pagina.text, 'html.parser')

# extraindo dados
titulos = dadosPagina.find_all('h3')

for t in titulos:
    titulos = t.a['title']
    print(titulos)
    
precos = dadosPagina.find_all('p', class_='price_color')

for p in precos:
    preco = p.get_text()
    print(preco)
    
avaliacoes = dadosPagina.find_all('p', class_='star-rating')

for a in avaliacoes:
    avaliacao = a['class'][1]
    print(avaliacao)
    
# salvando os dados em um arquivo
