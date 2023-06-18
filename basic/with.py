class MeuGerenciadorDeContexto:
    def __enter__(self):
        # Lógica de inicialização do contexto
        print("Iniciando o contexto")
        # Você pode retornar um valor opcional que será associado à variável após o 'as'
        return "Valor associado"

    def __exit__(self, exc_type, exc_value, traceback):
        # Lógica de encerramento do contexto
        print("Encerrando o contexto")
        # Você pode tratar exceções ou liberar recursos dentro deste método

# Exemplo de uso do gerenciador de contexto personalizado
with MeuGerenciadorDeContexto() as valor:
    print("Dentro do contexto")
    print("Valor associado:", valor)

# O bloco de código dentro do 'with' é executado dentro do contexto criado pelo gerenciador.
# A saída esperada será:
# Iniciando o contexto
# Dentro do contexto
# Valor associado: Valor associado
# Encerrando o contexto
