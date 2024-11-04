import requests
import json

# Função para verificar a disponibilidade de estoque com CEP do usuário
def verificar_estoque():
    cep = input("Digite o CEP (ex: 88101000): ")

    # URL da API GraphQL
    url = "https://federation.magazineluiza.com.br/graphql"

    # Query
    query = """
        query shippingQuery($shippingRequest: ShippingRequest!) {
          shipping(shippingRequest: $shippingRequest) {
            status
          }
        }
    """

    # Variáveis para payload com dados atualizados
    variables = {
        "shippingRequest": {
            "metadata": {
                "categoryId": "PF",
                "clientId": "f2cdc878-9339-4000-8abf-3c306836cd02",
                "organizationId": "magazine_luiza",
                "pageName": "",
                "partnerId": "0",
                "salesChannelId": "45",
                "sellerId": "olistplus",
                "subcategoryId": "PAPP"
            },
            "product": {
                "currency": "BRL",
                "dimensions": {
                    "height": 0.12,
                    "length": 0.2,
                    "weight": 0.35,
                    "width": 0.11
                },
                "exchangeRate": None,
                "id": "O2EIT0I89QX3GBOX",
                "idExchangeRate": None,
                "originalPriceForeign": None,
                "price": 386.43,
                "quantity": 1,
                "type": "product"
            },
            "zipcode": cep 
        }
    }


    # Envio da requisição POST
    response = requests.post(url, json={"query": query, "variables": variables})

    # Verificação da resposta
    if response.status_code == 200:
        response_data = response.json()
        status = response_data.get("data", {}).get("shipping", {}).get("status", "")

        if status == "OK":
            return "Estoque disponível"
        else:
            return "Estoque não disponível"
    else:
        return f"Erro ao acessar a API: {response.status_code}"