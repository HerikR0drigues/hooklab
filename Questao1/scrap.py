import requests
from bs4 import BeautifulSoup
import pandas as pd
import scrapSelenium

titles = []
upvotes = []
links = []

# Atraves do requests e Soup pegar os titulos e links
url = 'https://www.reddit.com/r/programming/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    shreddit_feed = soup.find('shreddit-feed')

    shreddit_posts = shreddit_feed.find_all('shreddit-post', limit=3)

    for shreddit_post in shreddit_posts:
        title_tag = shreddit_post.find('a')
        
        title = title_tag.text
        link = 'https://www.reddit.com' + title_tag['href']

        titles.append(title)
        links.append(link)
else:
    print(f'Erro ao acessar a página: {response.status_code}')
# ----------------------------------------------------------------- #

# Atraves do Selenium pegar os upvotes (pois eles se encontram em uma shadow-root)
# Funcao importada do arquivo scrapSelenium localizada na mesma pasta
upvotes = scrapSelenium.getUpVotes()

# Fazendo um dataframe com Pandas e armazenando em formato tabular
df = pd.DataFrame({
    'Titulo': titles,
    'Upvotes': upvotes,
    'Links': links
})

df.to_csv('questao1.csv', index=False)

