import re
import requests
from bs4 import BeautifulSoup
import json
import scrapStock

# Atraves do requests e Soup pegar o titulo e preço
url = "https://www.magazineluiza.com.br/aparador-de-barba-philips-verde-limao-qp1424/p/af0hf57h18/pf/papp/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    title_tag = soup.find('h1', {'data-testid': 'heading-product-title'})
    title = title_tag.get_text(strip=True) if title_tag else 'Título não encontrado'

    price_tag = soup.find('p', {'data-testid': 'price-value'})

    if price_tag:
        price = price_tag.get_text(strip=True)
        price_numeric = re.sub(r'[^\d,]', '', price)
    else:
        price_numeric = 'Preço não encontrado'

    # Apos verificar o Network da página, foi encontrada uma API que tem a resposta se o estoque está disponivel para o cep informado (Função importada do arquivo scrapStock na mesma pasta)
    stock_availability = scrapStock.verificar_estoque();

    product_info = {
        'title': title,
        'stock_availability': stock_availability,
        'price_pix': price_numeric
    }

    json_file_path = 'product_info.json'

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(product_info, json_file, indent=2, ensure_ascii=False)

    print(json.dumps(product_info, indent=2, ensure_ascii=False))

else:
    print(f'Erro ao acessar a página: {response.status_code}')