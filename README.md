# webscraping-examples
### Passo a passo de como criar o seu primeiro scraper do zero!
#### Objetivo: 
Vamos utilizar como exemplo o [site da Nike](https://www.nike.com.br/nav/categorias/tenis/genero/feminino/tipodeproduto/calcados), com o objetivo de extrair as informações dos títulos e preços dos calçados femininos.
#### Requisitos:
- [Python](https://www.python.org/downloads/) instalado;
- Biblioteca [Requests](https://pypi.org/project/requests/) instalada;
- Biblioteca [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#) OU biblioteca [LXML](https://lxml.de/installation.html) instalada.
#### Sugestões:
- [Postman](https://www.postman.com/) OU [Insomnia](https://insomnia.rest/) instalado, ou alguma ferramenta para testes de requisições;
- [SelectorGadget](https://selectorgadget.com/).

##### PASSO A PASSO:
1. Definir o site que se deseja realizar o scraping e quais as informações você deseja extrair dele;
2. Acessar o site pelo próprio navegador e analisar em qual formato é retornado o conteúdo da página (JSON, HTML/XML…).
Dica: para analisar isso você pode utilizar o atalho Ctrl+Shift+i ou clicar com o botão direito do mouse na página e clicar em Inspecionar. Irá abrir o dev tools, o famoso ferramentas do desenvolvedor. Ali você pode analisar tudo sobre a requisição! Segue um link para apoio caso tenha alguma dificuldade: [Como abrir o Dev Tools](https://support.google.com/adsense/answer/10858959?hl=pt-BR#:~:text=Para%20abrir%20o%20DevTools%2C%20clique,%2C%20Linux%2C%20Chrome%20OS).
Depois você deve selecionar qual a requisição que lhe interessa o conteúdo. No meu caso, é a que tem o nome de calcados, pois foi para esse endpoint que eu efetuei a requisição. Primeiramente me certifico de estar na aba de Network, então clico em calcados e depois na aba de Response, para poder analisar o conteúdo da resposta da requisição. Neste caso, o conteúdo foi retornado em formato HTML:
![](/images/check_response.png)
3. Faça um teste de requisição utilizando uma aplicação de testes de API, como o Postman ou o Insomnia.
Dica: Aqui você pode utilizar a ferramenta CurlConverter para te fornecer todas as informações necessárias para a requisição (headers, payload, url…). Ao clicar com o botão direito em cima da sua requisição > Copy > Copy as curl (bash), você terá o conteúdo da sua requisição em curl:
![](/images/copy_curl.png)
Depois é só acessar uma ferramenta de conversor de curl, como o [CurlConverter](https://curlconverter.com/), e colar o conteúdo curl da requisição:
![](/images/curlconverter.png)
A ferramenta irá então fornecer já o código para o scraper, conforme a linguagem de sua preferência, junto com todas as informações necessárias para a requisição:
![](/images/curlconverter2.png)
OBS: A ferramenta traz como padrão headers e cookies para todas as requisições. Contudo, você vai perceber que nem sempre é necessário informar headers customizados para realizar uma requisição, e os cookies são sempre dinâmicos, então não devem ser utilizados de forma estática.

Depois você pode utilizar o Postman para testar a sua requisição:
![](/images/postman_request.png)

O Postman é uma ferramenta de testes de APIs muito rica. Não irei entrar em detalhes, mas deixarei um [Tutorial de uso Postman](https://learning.postman.com/docs/introduction/overview/) para você consultar caso surjam dúvidas ao usá-lo.

Continuando... Para o caso do site da Nike, por exemplo, não foi necessário colocar headers customizados. Somente com a URL a requisição já foi realizada com sucesso (código de status 200 e retorno conforme esperado!). Se você observar, na aba de Headers, aparecem 7 parâmetros, mas eu não cadastrei nenhum. Isso ocorre porque o próprio Postman já envia alguns parâmetros de header como padrão:
![](/images/postman_headers_default.png)
OBS: Caso você simule a conexão e o código de status da requisição não seja o esperado, é possível que seja necessário adicionar novos parâmetros nos headers ou alterar os parâmetros padrão do Postman.

5. Mão no código! Agora é hora de construir o seu código (ou copiar do curlconverter) e testá-lo.
```python
import requests

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://www.nike.com.br/?gad_source=1&gclid=Cj0KCQjw8pKxBhD_ARIsAPrG45lu19se-z4tPHw_pGBQMeKBwcaN0JvmTj8mpNTK0mVFMQSe3Qf-BPsaAtZWEALw_wcB',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

text = requests.get(url="https://www.nike.com.br/nav/categorias/tenis/genero/feminino/tipodeproduto/calcados", headers=headers)
print(text.status_code) # 200
```

Maravilha! Código de status com retorno 200! Mas saca só, com o tempo você pega uns macetes e conforme vai entendendo o que significa cada parâmetro do header, você entende que alguns são mais importantes que outros!

```python
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

text = requests.get(url="https://www.nike.com.br/nav/categorias/tenis/genero/feminino/tipodeproduto/calcados", headers=headers)
print(text.status_code) # 200
´´´
Se eu removo todos os meus headers, com exceção do user-agent, eu continuo tendo acesso a minha página normalmente. Mas, se eu remover o user-agent também, eu recebo um bloqueio no acesso à página (código 403):
```python
import requests

text = requests.get(url="https://www.nike.com.br/nav/categorias/tenis/genero/feminino/tipodeproduto/calcados")
print(text.status_code) # 403
```
Com isso, você entende que o único header necessário (neste caso!) é o user-agent, e que os demais são dispensáveis. E pronto, temos acesso ao conteúdo da nossa página! Como guardamos o conteúdo da requisição no objeto response, essa response possui alguns atributos, como o status_code (código de resposta), content (conteúdo/texto de retorno), url, headers, cookies… lembrando que essas informações são todas do objeto Response (resposta à requisição). Para acessar essas informações, é só digitar: response.status_code, response.text, e assim por diante…

**5. Parsing -> processamento do texto**
Temos já o retorno da página, porém, temos apenas o texto cru, sem separação de elementos. O que nós queremos é apenas os títulos e os valores dos produtos. Para isso, há bibliotecas dedicadas para o processamento de texto, como BeautifulSoup e Lxml. Neste tutorial vamos falar um pouco sobre as duas.

*- BeautifulSoup:* é uma biblioteca muito rica para lidar com páginas HTML/XML. Super indico a leitura da biblioteca, pois aqui passarei apenas por cima das possibilidades. Pois bem, quando estudamos como a estrutura de um documento HTML funciona, entendemos que ele é construído no formato de árvore. Assim, elementos possuem um relacionamento entre si: pai, primo, irmão. Conforme a imagem abaixo, onde, por exemplo, o elemento *div* é pai do elemento *ul*, que é pai dos elementos *li*. É importante entender isso para conseguirmos captar os elementos desejados em um arquivo HTML.

Ok, mas e como eu sei como capturar as tags específicas que eu quero? Se você clicar na seta ali indicado no número 1, e depois clicar no conteúdo que você deseja pegar (2), irá aparecer tanto um popup com as informações do elemento, quanto na própria resposta da requisição irá aparecer o elemento ao lado. Assim, você consegue ter acesso às informações do elemento: tipo da tag (se é div, span, p…), texto, class, id… essas informações são essenciais para captarmos o conteúdo do texto. Class e id são formas de identificarmos cada elemento na página, seja de forma coletiva/em grupo (class) ou de forma individual (id). 

Para o nosso exemplo, segue o código:
```python
import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

response = requests.get(url="https://www.nike.com.br/nav/categorias/tenis/genero/feminino/tipodeproduto/calcados", headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
titles = soup.find_all(name="div", attrs={"class", "ProductCard-styled__ProductName-sc-8f840517-9 iKtbYK"})
prices = soup.find_all(name="span", attrs={"class", "ProductCard-styled__CurrentPrice-sc-8f840517-11 jyXUjS"})
```
Você primeiramente cria um objeto do BeautifulSoup, passando como conteúdo a resposta da requisição, e informando qual o tipo de parser você deseja. Depois disso, a nossa variável soup já entende que aquele é um arquivo html. Assim, você utilizará o método find_all para encontrar todos os elementos que tenham o respectivo tipo, e com os atributos informados acima. No caso do título dos calçados, a informação está numa tag div, de classe ProductCard-styled__ProductName-sc-8f840517-9 iKtbYK. Já os preços se encontram em tags span, de classe ProductCard-styled__CurrentPrice-sc-8f840517-11 jyXUjS. Abaixo coloquei para printar na tela para mostrar como os textos foram obtidos de forma como desejado:
!()[/images/comparison_terminal.png]
!()[/images/comparison_site.png]

*- LXML:* Outra biblioteca que você pode utilizar é o lxml, que nos possibilita trabalhar com expressões em XPath. Junto com ele, uma extensão bacana é o SelectorGadget, que nos fornece expressões xpath de cada grupo de elementos. Ele é uma extensão que você pode adicionar ao seu navegador e será muito útil. Para utilizá-lo:
1. Você clica no canto superior direito no ícone da lupa.
2. Clica no elemento da página que você deseja capturar. A extensão busca padrões, então ao clicar em um elemento ele ficará verde e mostrará em amarelo todos os outros elementos que possuem semelhança. Caso você não queira esses elementos em amarelo, é só clicar em cima deles, que eles serão desconsiderados. Como no meu caso, os elementos em amarelo são do meu interesse, não faço nada.
3. Clica no botão Xpath na parte inferior da tela.
4. Copie o Xpath fornecido no popup. Pronto! Agora você já tem o XPath, ou seja, a localização do seu elemento XML.
()[/images/selector_elements.png]
Partindo para o código, a lógica é parecida com a anterior, a diferença é que agora usamos o XPath:
```python
import requests
from lxml import html

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

response = requests.get(url="https://www.nike.com.br/nav/categorias/tenis/genero/feminino/tipodeproduto/calcados", headers=headers)
tree = html.fromstring(response.content)
titles = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "iKtbYK", " " ))]')
prices = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "jyXUjS", " " ))]')
```
