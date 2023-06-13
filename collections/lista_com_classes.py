class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'[>>Codigo {self.codigo} Saldo {self.saldo}<<]'
    

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


conta_do_link = ContaCorrente(15)
print(conta_do_link)
conta_do_link.deposita(500)
print(conta_do_link)

conta_da_val = ContaCorrente(47685)
conta_da_val.deposita(1000)
print(conta_da_val)

contas = [conta_do_link, conta_da_val]
print(contas)
for conta in contas:
    print(conta)

deposita_para_todas(contas)
for conta in contas:
    print(conta)

