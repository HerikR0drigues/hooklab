import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregue os dados JSON utilizando a biblioteca Pandas
dados = pd.read_json('dados_compras.json')

# Examine as primeiras linhas do conjunto de dados para entender sua estrutura.
print("\n======================================== Estrutura dos dados ============================================\n")
print(dados.head())
print("-------------------------------------------------------------------------------------------------------------")
print(dados.info())

# Verifique a presença de quaisquer valores ausentes nos dados.
print("\n========================================== Dados Ausentes ===============================================\n")
dados_ausentes = dados.isnull().sum()

if(dados_ausentes.any()):
    print("Há valores ausentes nos dados!")
    print(dados.isnull().sum())
else:
    print("Não há valores ausentes nos dados!")

# Identifique a quantidade total de compras realizadas.
print("\n================================== Total de de compras realizadas =======================================\n")

total_compras = dados.shape[0]
print(f'Total de compras realizadas: {total_compras}')

# Calcule a média, o valor mínimo e máximo gasto por compra
print("\n=================================== Média, valor mínimo e máximo ========================================\n")
media_gasto = dados['Valor'].mean()
min_gasto = dados['Valor'].min()
max_gasto = dados['Valor'].max()

print(f'Média: {media_gasto:.2f}')
print(f'Valor mínimo: {min_gasto:.2f}')
print(f'Valor máximo: {max_gasto:.2f}')

# Determine o produto mais caro e o produto mais barato.
print("\n============================= Produto mais caro e o produto mais barato ==================================\n")
produto_mais_caro = dados.loc[dados['Valor'].idxmax()]
produto_mais_barato = dados.loc[dados['Valor'].idxmin()]

print(f'Produto mais caro: {produto_mais_caro["Nome do Item"]} - {produto_mais_caro["Valor"]:.2f}')
print(f'Produto mais barato: {produto_mais_barato["Nome do Item"]} - {produto_mais_barato["Valor"]:.2f}')

# Analise a distribuição de gênero entre os consumidores
print("\n====================================== Distribuição de gênero ============================================\n")
distribuicao_genero = dados['Sexo'].value_counts()
print(distribuicao_genero.to_string())

# Calcule o valor total gasto em compras por gênero
print("\n=================================== Valor total gasto por gênero =========================================\n")
gasto_por_genero = dados.groupby('Sexo')['Valor'].sum()
print(gasto_por_genero.to_string())
print("\n==========================================================================================================\n")

# =============================================== VISUALIZAÇÃO DE DADOS ===============================================

# Paleta personalizada
cores_personalizadas1 = ["blue", "#FF1493", "green"]
cores_personalizadas2 = ["#FF1493", "blue", "green"]

# Gráfico 1: Distribuição de Gênero dos Consumidores
plt.figure(figsize=(10, 6))
sns.barplot(x=distribuicao_genero.index, y=distribuicao_genero.values, palette=cores_personalizadas1)
plt.title("Distribuição de Gênero dos Consumidores")
plt.xlabel("Gênero")
plt.ylabel("Quantidade de Consumidores")
plt.show()

# Gráfico 2: Gasto Total por Gênero
plt.figure(figsize=(10, 6))
sns.barplot(x=gasto_por_genero.index, y=gasto_por_genero.values, palette=cores_personalizadas2)
plt.title("Gasto Total por Gênero")
plt.xlabel("Gênero")
plt.ylabel("Valor Total Gasto (R$)")
plt.show()

# Gráfico 3: Distribuição do Valor das Compras
plt.figure(figsize=(12, 8))
sns.histplot(dados['Valor'], bins=30, kde=True, color='#6E0DFF')
plt.title("Distribuição do Valor das Compras")
plt.xlabel("Valor da Compra (R$)")
plt.ylabel("Frequência")
plt.show()
