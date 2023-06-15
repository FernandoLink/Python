from validate_docbr import CPF, CNPJ
import re 
from datetime import datetime, timedelta

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos está incorreta!")
        

class DocCpf:

    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:   
            raise ValueError("CPF inválido!")
        
    def __str__(self):
        return self.format()

    def valida(self, documento):
        return CPF().validate(documento)
    
    def format(self):
        return CPF().mask(self.cpf)
    

class DocCnpj:

    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:   
            raise ValueError("CNPJ inválido!")
        
    def __str__(self):
        return self.format()

    def valida(self, documento):
        return CNPJ().validate(documento)
    
    def format(self):
        return CNPJ().mask(self.cnpj)
    
    
class Telefone:

    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Telefone inválido!")
        
    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao,telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao,self.numero)
        return f'+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}'


class Data:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
    
    def mes(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        return meses_do_ano[self.momento_cadastro.month - 1]

    def dia_da_semana(self):
        dia_semana_lista = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]
        return dia_semana_lista[self.momento_cadastro.weekday()]
    
    def tempo_cadastro(self):
        return (datetime.today() + timedelta(days=30)) - self.momento_cadastro
    

print(Documento.cria_documento('81628927968'))
print(Documento.cria_documento('30537846000126'))
print(Telefone('5541999283829'))
print(Data())
print(Data().mes())
print(Data().dia_da_semana())
print(Data().tempo_cadastro())
