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
        if valor > 0:
            self.saldo += valor
            self._registrar_transacao("Depósito", valor)
            return f"Depósito de R${valor:.2f} realizado com sucesso."
        else:
            return "O valor do depósito deve ser positivo."

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                self._registrar_transacao("Saque", valor)
                return f"Saque de R${valor:.2f} realizado com sucesso."
            else:
                return "Saldo insuficiente para realizar o saque."
        else:
            return "O valor do saque deve ser positivo."

    def visualizar_extrato(self):
        extrato = "\nExtrato da Conta:\n"
        for transacao in self.transacoes:
            extrato += f"{transacao}\n"
        extrato += f"Saldo atual: R${self.saldo:.2f}"
        return extrato

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_contas(self):
        return [str(conta) for conta in self.contas]

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}"

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def cadastrar_cliente(self, nome, cpf):
        cliente = Cliente(nome, cpf)
        self.clientes.append(cliente)
        return cliente

    def cadastrar_conta_bancaria(self, cliente, saldo_inicial=0):
        conta = ContaBancaria(saldo_inicial)
        cliente.adicionar_conta(conta)
        self.contas.append(conta)
        return conta

# Funções para operações bancárias

def criar_usuario(banco, nome, cpf):
    if not isinstance(nome, str) or not nome:
        print("Nome inválido. Deve ser uma string não vazia.")
        return None
    if not isinstance(cpf, str) or not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido. Deve ser uma string numérica de 11 dígitos.")
        return None

    cliente = banco.cadastrar_cliente(nome, cpf)
    print(f"Cliente {nome} cadastrado com sucesso.")
    return cliente

def criar_conta_corrente(banco, cliente, saldo_inicial=0):
    if not isinstance(cliente, Cliente):
        print("Cliente inválido. Deve ser um objeto da classe Cliente.")
        return None
    if not isinstance(saldo_inicial, (int, float)) or saldo_inicial < 0:
        print("Saldo inicial inválido. Deve ser um número positivo ou zero.")
        return None

    conta = banco.cadastrar_conta_bancaria(cliente, saldo_inicial)
    print(f"Conta corrente criada com saldo inicial de R${saldo_inicial:.2f}.")
    return conta

def listar_contas(cliente):
    if not isinstance(cliente, Cliente):
        print("Cliente inválido. Deve ser um objeto da classe Cliente.")
        return

    contas = cliente.listar_contas()
    print(f"Contas do cliente {cliente.nome}:")
    for i, conta in enumerate(contas, 1):
        print(f"Conta {i}: {conta}")

def realizar_deposito(conta, valor):
    if not isinstance(conta, ContaBancaria):
        print("Conta inválida. Deve ser um objeto da classe ContaBancaria.")
        return
    if not isinstance(valor, (int, float)) or valor <= 0:
        print("Valor de depósito inválido. Deve ser um número positivo.")
        return

    mensagem = conta.depositar(valor)
    print(mensagem)

def realizar_saque(conta, valor):
    if not isinstance(conta, ContaBancaria):
        print("Conta inválida. Deve ser um objeto da classe ContaBancaria.")
        return
    if not isinstance(valor, (int, float)) or valor <= 0:
        print("Valor de saque inválido. Deve ser um número positivo.")
        return

    mensagem = conta.sacar(valor)
    print(mensagem)

def exibir_extrato(conta):
    if not isinstance(conta, ContaBancaria):
        print("Conta inválida. Deve ser um objeto da classe ContaBancaria.")
        return

    extrato = conta.visualizar_extrato()
    print(extrato)

# Exemplo de uso
if __name__ == "__main__":
    banco = Banco()

    # Criar usuário
    cliente = criar_usuario(banco, "Maria Alves", "12345678900")

    # Criar conta corrente
    conta1 = criar_conta_corrente(banco, cliente, 1000)
    conta2 = criar_conta_corrente(banco, cliente, 500)

    # Listar contas do cliente
    listar_contas(cliente)

    # Realizar operações
    realizar_deposito(conta1, 500)
    realizar_saque(conta1, 200)
    exibir_extrato(conta1)

