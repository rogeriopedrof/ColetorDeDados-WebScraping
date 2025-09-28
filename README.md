# COLETOR DE DADOS - LIVROS 
5W1H

1 What (O que é?)
Um projeto em Python que coleta automaticamente dados públicos de livros do site books.toscrape.com (categoria "Mystery"), usando web scraping com requests e BeautifulSoup, tratando os dados com pandas, calculando o custo-benefício (avaliação/preço) e exportando para um arquivo .csv.

2 Why (Por que?)
Praticar técnicas de web scraping, manipulação de dados com pandas, e automação para criar uma lista organizada de livros com base em custo-benefício. Útil para análises de mercado, recomendações de leitura ou estudos de dados sobre livros.

2 Who (Quem participa?)

Rogério - Web scraping
Lucas - Pandas
Ygor - Suporte e Revisão

3 Where (Onde será usado?)

O script pode ser executado em qualquer sistema operacional (Windows, Linux, macOS) com Python instalado.
Os resultados são salvos em um arquivo livros_custo_beneficio.csv, que pode ser aberto em planilhas (Excel, Google Sheets) ou usado em ferramentas de análise de dados.


4 When (Quando usar?)

5 Sempre que for necessário coletar e organizar dados de livros de forma automatizada.
Ideal para análises rápidas de preços, avaliações ou para encontrar livros com bom custo-benefício na categoria "Mystery".


6 How (Como funciona?)

O usuário clona o repositório (se hospedado no GitHub) ou copia o script fornecido.
Instala as dependências (pip install requests beautifulsoup4 pandas).
Executa o script principal (python main.py).
O programa:

Acessa a página https://books.toscrape.com/catalogue/category/books/mystery_3/index.html.
Extrai títulos, preços e avaliações usando BeautifulSoup.
Organiza os dados em um pandas DataFrame, calcula o custo-benefício (avaliação/preço).
Ordena os livros por custo-benefício (do melhor para o pior).
Exibe a tabela no terminal e salva os dados em livros_custo_beneficio.csv.
