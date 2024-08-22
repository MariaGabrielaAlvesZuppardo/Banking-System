class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.transacoes = []  

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                self.transacoes.append(f"Saque: R${valor:.2f}")
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def visualizar_extrato(self):
        print("\nExtrato da Conta:")
        for transacao in self.transacoes:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}")

