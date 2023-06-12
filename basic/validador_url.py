import re

urls = ['bytebank.com/cambio',
'bytebank.com.br/cambio',
'www.bytebank.com/cambio',
'www.bytebank.com.br/cambio',
'http://www.bytebank.com/cambio',
'http://www.bytebank.com.br/cambio',
'https://www.bytebank.com/cambio',
'https://www.bytebank.com.br/cambio',
'https://bytebank/cambio',
'https://bytebank.naoexiste/cambio',
'ht://bytebank.naoexiste/cambio']

padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')

for url in urls:
    match = padrao_url.match(url)
    if not match:
        print(f'A URL -> {url} é inválida!')
    else:
        print(f'A URL -> {url} é válida!')

