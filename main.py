# pandas
import pandas as pd

# web scraping
import requests
from bs4 import BeautifulSoup
import re  # para limpar caracteres especiais do preço

# faz a requisição
pagina = requests.get("https://books.toscrape.com/catalogue/category/books/mystery_3/index.html")
dadosPagina = BeautifulSoup(pagina.text, 'html.parser')

# listas para guardar os dados
titulos = []
precos = []
avaliacoes = []

# extraindo títulos
titulos_html = dadosPagina.find_all('h3')
for t in titulos_html:
    titulo = t.a['title']
    titulos.append(titulo)

# extraindo preços (robusto)
precos_html = dadosPagina.find_all('p', class_='price_color')
for p in precos_html:
    preco_texto = p.get_text().strip()                    # remove espaços
    preco_texto = re.sub(r'[^\d.,]', '', preco_texto)    # remove qualquer caractere que não seja número, ponto ou vírgula
    preco_texto = preco_texto.replace(',', '.')          # transforma vírgula em ponto, se houver
    preco = float(preco_texto)
    precos.append(preco)

# extraindo avaliações
avaliacoes_html = dadosPagina.find_all('p', class_='star-rating')
mapa_avaliacoes = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

for a in avaliacoes_html:
    avaliacao = a['class'][1]              # pega a palavra (One, Two, etc.)
    avaliacao_num = mapa_avaliacoes[avaliacao]  # converte para número
    avaliacoes.append(avaliacao_num)

# cria o DataFrame com pandas
df = pd.DataFrame({
    "Título": titulos,
    "Preço (£)": precos,
    "Avaliação (1-5)": avaliacoes
})

# cria coluna de custo-benefício
df["Custo-Benefício"] = (df["Avaliação (1-5)"] / df["Preço (£)"]).round(2)

# ordena os livros do melhor custo-benefício para o pior
df_filtrado = df.sort_values(by="Custo-Benefício", ascending=False)

# mostra tabela no terminal
print("\n📊 Livros ordenados por custo-benefício:\n")
print(df_filtrado.to_string(index=False))

# salva em CSV
df_filtrado.to_csv("livros_custo_beneficio.csv", index=False, encoding="utf-8")
print("\n✅ Arquivo 'livros_custo_beneficio.csv' salvo com sucesso!")
