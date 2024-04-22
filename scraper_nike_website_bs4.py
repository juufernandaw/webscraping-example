import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

response = requests.get(url="https://www.nike.com.br/nav/categorias/tenis/genero/feminino/tipodeproduto/calcados", headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
titles = soup.find_all(name="div", attrs={"class", "ProductCard-styled__ProductName-sc-8f840517-9 iKtbYK"})
prices = soup.find_all(name="span", attrs={"class", "ProductCard-styled__CurrentPrice-sc-8f840517-11 jyXUjS"})
