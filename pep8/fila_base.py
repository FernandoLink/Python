import abc
from constantes import TAMANHO_PADRAO_MINIMO, TAMANHO_PADRAO_MAXIMO


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: list[str] = []
    clientes_atendidos: list[str] = []
    senhaatual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def inseri_cliente(self):
        self.fila.append(self.senha_atual)

    @abc.abstractmethod
    def gera_senha_atual(self) -> None:
        ...

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    @abc.abstractmethod
    def chama_cliente(self, caixa: int) -> str:
        ...
