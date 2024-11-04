import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

products = []

# Input para o usuário digitar o produto que deseja buscar
product_query = input("Digite o nome do produto que deseja buscar: ")
product_query_formatted = product_query.replace(' ', '%20')

# Atraves do requests e Soup pegar os titulos, links e preços
url = f'https://www.climario.com.br/{product_query_formatted}?_q={product_query_formatted}&map=ft'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    div_container = soup.find('div', id='gallery-layout-container')

    product_divs = div_container.find_all('div', class_='vtex-search-result-3-x-galleryItem vtex-search-result-3-x-galleryItem--normal vtex-search-result-3-x-galleryItem--grid pa4')

    for product_div in product_divs:
        title = product_div.find('h3') 
        title_text = title.text.strip() if title else 'Título não encontrado'

        price = product_div.find('span', class_='vtex-product-price-1-x-spotPrice vtex-product-price-1-x-spotPrice--default')

        if price:
            price_text = price.text.strip()
            price_text = re.sub(r'[^0-9,]', '', price_text)
        else:
            price_text = 'Preço não encontrado'

        link = product_div.find('a', class_='vtex-product-summary-2-x-clearLink vtex-product-summary-2-x-clearLink--default h-100 flex flex-column')
        link_href = link['href'] if link and 'href' in link.attrs else 'Link não encontrado'

        if link_href != 'Link não encontrado':
            link_href = 'https://www.climario.com.br' + link_href

        img = product_div.find('img')
        img_src = img['src'] if img and 'src' in img.attrs else 'Imagem não encontrada'

        # Adicionando as informações do produto ao dicionário
        products.append({
            'title': title_text,
            'price': price_text,
            'link': link_href,
            'img': img_src,
        })
    # ----------------------------------------------------------------- #

    # Fazendo um dataframe com Pandas e armazenando em formato tabular
    df = pd.DataFrame(products)

    print(df)

    df.to_csv('questao2.csv', index=False)
else:
    print(f'Erro ao acessar a página: {response.status_code}')


