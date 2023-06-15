import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")
        
    def __str__(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def acessa_via_cep(self):
        url = f'https://viacep.com.br/ws/{cep}/json/'
        r = requests.get(url)
        return  r


cep = "82900150"
objeto_cep = BuscaEndereco(cep)
a = objeto_cep.acessa_via_cep().json()
print(a['logradouro'])
