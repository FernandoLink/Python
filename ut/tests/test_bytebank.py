from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given or Arrange
        entrada = '13/03/2000' 
        esperado = 23
        funcionario_teste = Funcionario('Teste','13/03/2000', 1111)
        # When or Act
        resultado = funcionario_teste.idade()
        # Then or Assert
        assert resultado == esperado 

    def test_quando_sobrenome_recebe_Fernando_Link_deve_retornar_Link(self):
        entrada = ' Fernando Link '
        esperado = 'Link'
        link = Funcionario(entrada,'22/04/1970', 1111)
        resultado = link.sobrenome()
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000
        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100
        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000
            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()
            assert resultado

    def test_retorno_str(self):
        nome, data_nascimento, salario = 'Fernando Link', '22/04/1970', 12000
        esperado = 'Funcionario(Fernando Link, 22/04/1970, 12000)'
        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__()
        assert resultado == esperado

    