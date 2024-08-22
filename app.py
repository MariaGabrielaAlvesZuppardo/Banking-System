from datetime import datetime

class ContaBancaria:
    LIMITE_TRANSACOES_DIARIAS = 10

    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.transacoes = []
        self.transacoes_diarias = {}

    def _registrar_transacao(self, tipo, valor):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transacoes.append(f"{data_hora} - {tipo}: R${valor:.2f}")
        
        data_atual = datetime.now().strftime("%Y-%m-%d")
        if data_atual not in self.transacoes_diarias:
            self.transacoes_diarias[data_atual] = 0
        
        self.transacoes_diarias[data_atual] += 1

    def _verificar_limite_transacoes(self):
        data_atual = datetime.now().strftime("%Y-%m-%d")
        if data_atual in self.transacoes_diarias:
            return self.transacoes_diarias[data_atual] < self.LIMITE_TRANSACOES_DIARIAS
        return True

    def depositar(self, valor):
        if self._verificar_limite_transacoes():
            if valor > 0:
                self.saldo += valor
                self._registrar_transacao("Depósito", valor)
                print(f"Depósito de R${valor:.2f} realizado com sucesso.")
            else:
                print("O valor do depósito deve ser positivo.")
        else:
            print("Você excedeu o número de transações permitidas para hoje.")

    def sacar(self, valor):
        if self._verificar_limite_transacoes():
            if valor > 0:
                if valor <= self.saldo:
                    self.saldo -= valor
                    self._registrar_transacao("Saque", valor)
                    print(f"Saque de R${valor:.2f} realizado com sucesso.")
                else:
                    print("Saldo insuficiente para realizar o saque.")
            else:
                print("O valor do saque deve ser positivo.")
        else:
            print("Você excedeu o número de transações permitidas para hoje.")

    def visualizar_extrato(self):
        print("\nExtrato da Conta:")
        for transacao in self.transacoes:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}")

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}"

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def cadastrar_cliente(self, nome, cpf):
        cliente = Cliente(nome, cpf)
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso.")
        return cliente

    def cadastrar_conta_bancaria(self, cliente, saldo_inicial=0):
        conta = ContaBancaria(saldo_inicial)
        cliente.adicionar_conta(conta)
        self.contas.append(conta)
        print(f"Conta bancária criada com saldo inicial de R${saldo_inicial:.2f}.")
        return conta

# Exemplo de uso
if __name__ == "__main__":
    banco = Banco()

    # Cadastrar cliente
    cliente = banco.cadastrar_cliente("Maria Alves", "123.456.789-00")

    # Cadastrar conta bancária
    conta = banco.cadastrar_conta_bancaria(cliente, 1000)

    # Realizar operações
    conta.depositar(500)
    conta.sacar(200)
    conta.visualizar_extrato()
