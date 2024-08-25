from datetime import datetime

class ContaBancaria:
    LIMITE_TRANSACOES_DIARIAS = 10
    NUMERO_AGENCIA = "0001"
    numero_conta_sequencial = 1  # Atributo de classe para gerar números de conta sequenciais

    def __init__(self, usuario, saldo_inicial=0):
        self.agencia = ContaBancaria.NUMERO_AGENCIA
        self.numero_conta = ContaBancaria.numero_conta_sequencial
        ContaBancaria.numero_conta_sequencial += 1  # Incrementar o número sequencial para a próxima conta
        self.usuario = usuario
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

    def __str__(self):
        return f"Agência: {self.agencia}, Conta: {self.numero_conta}, Usuário: {self.usuario.nome}, Saldo: R${self.saldo:.2f}"

class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = ''.join(filter(str.isdigit, cpf))  # Armazenar apenas os números do CPF
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_contas(self):
        return [str(conta) for conta in self.contas]

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def cadastrar_cliente(self, nome, data_nascimento, cpf, endereco):
        if self.buscar_cliente_por_cpf(cpf):
            print(f"Erro: Já existe um cliente cadastrado com o CPF {cpf}.")
            return None

        cliente = Cliente(nome, data_nascimento, cpf, endereco)
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso.")
        return cliente

    def buscar_cliente_por_cpf(self, cpf):
        cpf_numeros = ''.join(filter(str.isdigit, cpf))
        for cliente in self.clientes:
            if cliente.cpf == cpf_numeros:
                return cliente
        return None

    def criar_conta_corrente(self, cliente, saldo_inicial=0):
        if not isinstance(cliente, Cliente):
            print("Cliente inválido. Deve ser um objeto da classe Cliente.")
            return None
        conta = ContaBancaria(cliente, saldo_inicial)
        cliente.adicionar_conta(conta)
        self.contas.append(conta)
        print(f"Conta corrente criada para {cliente.nome} com saldo inicial de R${saldo_inicial:.2f}.")
        return conta

# Funções para operações bancárias

def criar_usuario(banco, nome, data_nascimento, cpf, endereco):
    if not isinstance(nome, str) or not nome:
        print("Nome inválido. Deve ser uma string não vazia.")
        return None
    if not isinstance(cpf, str) or not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido. Deve ser uma string numérica de 11 dígitos.")
        return None

    cliente = banco.cadastrar_cliente(nome, data_nascimento, cpf, endereco)
    return cliente

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

    # Criar usuários
    cliente1 = criar_usuario(banco, "Maria Alves", "01/01/1980", "12345678900", "Rua A, 123 - Bairro B - Cidade C SP")
    cliente2 = criar_usuario(banco, "João Silva", "15/03/1990", "98765432100", "Avenida X, 456 - Bairro Y - Cidade Z RJ")

    # Criar contas correntes
    if cliente1:
        conta1 = banco.criar_conta_corrente(cliente1, 1000)

    if cliente2:
        conta2 = banco.criar_conta_corrente(cliente2, 500)

    # Listar contas do cliente
    if cliente1:
        listar_contas(cliente1)

    # Realizar operações
    if conta1:
        realizar_deposito(conta1, 300)
        realizar_saque(conta1, 100)
        exibir_extrato(conta1)
