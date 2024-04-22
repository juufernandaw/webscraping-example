import requests
from lxml import html

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

response = requests.get(url="https://www.nike.com.br/nav/categorias/tenis/genero/feminino/tipodeproduto/calcados", headers=headers)
tree = html.fromstring(response.content)
titles = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "iKtbYK", " " ))]')
prices = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "jyXUjS", " " ))]')
