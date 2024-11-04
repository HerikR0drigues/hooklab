# Desafio Estágio Hooklab

Desenvolvido por: **Herik Trombetta Rodrigues**

## Descrição
Este repositório contém o código desenvolvido para o desafio de estágio da empresa Hooklab. Abaixo estão as instruções de instalação das dependências e observações importantes sobre o comportamento do script em determinadas questões.

## Dependências
Para executar este projeto, é necessário instalar as seguintes dependências:
```bash
pip install requests beautifulsoup4 pandas webdriver-manager selenium matplotlib seaborn
```

## Como executar o código
Há cinco pastas (Questao1, Questao2, Questao2Bonus, Questao3 e Questao4), para cada questão basta entrar em cada uma delas e rodar o comando:
```bash
python scrap.py
```

## Estrutura do Projeto
- `Questao1` - Script para raspagem de dados do reddit, ele recupera o título, upvotes e links das três primeiras postagens do subreddit r/programming.
- `Questao2` - Script para recuperar os principais atributos de uma oferta fornecendo um arquivo JSON
- `Questao2Bonus` - Script de consulta de produto no site CLIMARIO, você fornece o item que quer buscar através do console (Exemplo: geladeira) e ele retorna o Link da oferta, Link da imagem, Preço e Título. (Faz Scraping na página)
- `Questao3` - Script para raspagem de dados, ele recupera o título, preço e disponibilidade de frete via API GraphQL de um produto específico do MAGAZINE LUIZA.
- `Questao4` - Script para análise de dados, ele lê um arquivo JSON já disponível dentro da propria pasta e faz algumas analises.

## Observações

- `Questao1`: Foi usado Selenium para pegar os números de "upvotes" pois ele se encontrava em uma shadow-root, sendo assim só sendo possível recuperar pelo selenium.
<<<<<<< HEAD
- `Questao2Bonus`: O script apresenta comportamento inesperado ao processar consultas (queries) com espaços, como em 'ar condicionado' mesmo após formatação da URL. Para consultas com uma só palavra e que contenha o item no site está OK.
- `Questao2Bonus`: Por razões desconhecidas, o script só carrega os primeiros 6 itens de uma lista, independentemente de haver mais itens disponíveis.
- `Questao3`: Foi encontrada uma requisição API GraphQL que responde à disponibilidade de frete conforme o CEP. Entretanto, as variáveis do script foram ajustadas para um link específico de produto, o que significa que o código é funcional apenas para esse produto.
