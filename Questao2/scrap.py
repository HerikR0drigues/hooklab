import json
import pandas as pd

# Carrega o conteúdo do arquivo JSON
with open('api_response.json', 'r', encoding='utf-8') as file:
    dados = json.load(file)

# Lista para armazenar os dados dos produtos
produtos_lista = []

# Itera sobre cada chave que começa com "Product:"
for chave, produto in dados.items():
    if chave.startswith("Product:"):
        # Extrai informações principais do produto
        titulo = produto.get('productName')
        link = produto.get('link')
        preco = dados.get(f"${chave}.priceRange.sellingPrice", {}).get('highPrice')

        # Coleta URLs das imagens do produto
        item_chave = f"{chave}.items({{\"filter\":\"ALL\"}}).0"
        image_urls = [
            dados[img.get('id')].get('imageUrl') 
            for img in dados.get(item_chave, {}).get('images', []) 
            if img.get('id') and dados.get(img.get('id'))
        ]

        # Adiciona os dados do produto à lista
        if titulo:
            produtos_lista.append({
                "Titulo": titulo,
                "Preço": preco,
                "Link": 'https://www.climario.com.br' + link,
                "Imagens": ", ".join(image_urls)
            })

# Cria um DataFrame e salva em um arquivo CSV
df_produtos = pd.DataFrame(produtos_lista)
df_produtos.to_csv('ofertas.csv', index=False, encoding='utf-8')

print("Dados salvos em ofertas.csv")
