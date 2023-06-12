import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if(type(url) == str):
            return url.strip()
        else:
            return ""
    
    def valida_url(self):
        if(not self.url):
            raise ValueError('URL inválida!')        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('URL inválida!')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        self.url_base = self.url[:indice_interrogacao]
        return self.url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        self.url_base = self.url[indice_interrogacao+1:]
        return self.url_base

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if(indice_e_comercial == -1):
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    
    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f'URL BASE -> {self.get_url_base()} \nPARÂMETROS -> {self.get_url_parametros()}'
    
    def __eq__(self, other):
        return self.url == other.url
    
    
url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)
print(extrator_url.get_valor_parametro('moedaDestino'))
print(extrator_url.get_valor_parametro('moedaOrigem'))
print(extrator_url.get_valor_parametro('quantidade'))
print(len(extrator_url))
print(extrator_url)
print(extrator_url == extrator_url2)
print(id(extrator_url))
print(id(extrator_url2))
print(1 is True)

# Métodos da classe
metodos = dir(ExtratorURL)
print(metodos)
print('valida_url' in dir(ExtratorURL))
