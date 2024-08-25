from datetime import datetime
from typing import List, Union

# Classe para Transação
class Transacao:
    def __init__(self, tipo: str, valor: float):
        self.tipo = tipo
        self.valor = valor
        self.data_hora = datetime.now()

    def __str__(self):
        return f"{self.data_hora.strftime('%Y-%m-%d %H:%M:%S')} - {self.tipo}: R${self.valor:.2f}"

# Classe para Histórico de Transações
class Historico:
    def __init__(self):
        self.transacoes: List[Transacao] = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)

    def __str__(self):
        return "\n".join(str(transacao) for transacao in self.transacoes)

# Classe para Conta Bancária
class Conta:
    LIMITE_TRANSACOES_DIARIAS = 10
    NUMERO_AGENCIA = "0001"

    numero_conta_sequencial = 1  # Atributo de classe para gerar números de conta sequenciais

    def __init__(self, cliente: 'Cliente', saldo_inicial: float, numero: int):
        self.agencia = Conta.NUMERO_AGENCIA
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo_inicial
        self.historico = Historico()
        self.transacoes_diarias = {}

    def _registrar_transacao(self, tipo: str, valor: float):
        transacao = Transacao(tipo, valor)
        self.historico.adicionar_transacao(transacao)

        data_atual = datetime.now().strftime("%Y-%m-%d")
        if data_atual not in self.transacoes_diarias:
            self.transacoes_diarias[data_atual] = 0
        
        self.transacoes_diarias[data_atual] += 1

    def _verificar_limite_transacoes(self):
        data_atual = datetime.now().strftime("%Y-%m-%d")
        return self.transacoes_diarias.get(data_atual, 0) < self.LIMITE_TRANSACOES_DIARIAS

    def depositar(self, valor: float):
        if self._verificar_limite_transacoes():
            if valor > 0:
                self.saldo += valor
                self._registrar_transacao("Depósito", valor)
                return f"Depósito de R${valor:.2f} realizado com sucesso."
            else:
                return "O valor do depósito deve ser positivo."
        else:
            return "Você excedeu o número de transações permitidas para hoje."

    def sacar(self, valor: float):
        if self._verificar_limite_transacoes():
            if valor > 0:
                if valor <= self.saldo:
                    self.saldo -= valor
                    self._registrar_transacao("Saque", valor)
                    return f"Saque de R${valor:.2f} realizado com sucesso."
                else:
                    return "Saldo insuficiente para realizar o saque."
            else:
                return "O valor do saque deve ser positivo."
        else:
            return "Você excedeu o número de transações permitidas para hoje."

    def visualizar_extrato(self):
        return f"\nExtrato da Conta:\n{self.historico}\nSaldo atual: R${self.saldo:.2f}"

    def __str__(self):
        return f"Agência: {self.agencia}, Conta: {self.numero}, Cliente: {self.cliente.nome}, Saldo: R${self.saldo:.2f}"

# Classe para Cliente
class Cliente:
    def __init__(self, nome: str, data_nascimento: datetime, endereco: str):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas: List[Conta] = []

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

    def listar_contas(self):
        return [str(conta) for conta in self.contas]

    def __str__(self):
        return f"Cliente: {self.nome}, Endereço: {self.endereco}"

# Classe para Pessoa Física (subclasse de Cliente)
class PessoaFisica(Cliente):
    def __init__(self, nome: str, data_nascimento: datetime, cpf: str, endereco: str):
        super().__init__(nome, data_nascimento, endereco)
        self.cpf = ''.join(filter(str.isdigit, cpf))  # Armazenar apenas os números do CPF

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"

# Classe para Banco
class Banco:
    def __init__(self):
        self.clientes: List[Cliente] = []
        self.contas: List[Conta] = []

    def cadastrar_cliente(self, nome: str, data_nascimento: datetime, cpf: str, endereco: str) -> Union[Cliente, None]:
        if self.buscar_cliente_por_cpf(cpf):
            print(f"Erro: Já existe um cliente cadastrado com o CPF {cpf}.")
            return None

        cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso.")
        return cliente

    def buscar_cliente_por_cpf(self, cpf: str) -> Union[Cliente, None]:
        cpf_numeros = ''.join(filter(str.isdigit, cpf))
        for cliente in self.clientes:
            if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf_numeros:
                return cliente
        return None

    def criar_conta_corrente_por_cpf(self, cpf: str, saldo_inicial: float) -> Union[Conta, None]:
        cliente = self.buscar_cliente_por_cpf(cpf)
        if not cliente:
            print(f"Erro: Não foi encontrado nenhum cliente com o CPF {cpf}.")
            return None

        conta = Conta(cliente, saldo_inicial, Conta.numero_conta_sequencial)
        Conta.numero_conta_sequencial += 1  # Incrementar o número sequencial para a próxima conta
        cliente.adicionar_conta(conta)
        self.contas.append(conta)
        print(f"Conta corrente criada para {cliente.nome} com saldo inicial de R${saldo_inicial:.2f}.")
        return conta

# Funções para operações bancárias

def criar_usuario(banco: Banco, nome: str, data_nascimento: datetime, cpf: str, endereco: str) -> Union[Cliente, None]:
    if not isinstance(nome, str) or not nome:
        print("Nome inválido. Deve ser uma string não vazia.")
        return None
    if not isinstance(cpf, str) or not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido. Deve ser uma string numérica de 11 dígitos.")
        return None

    cliente = banco.cadastrar_cliente(nome, data_nascimento, cpf, endereco)
    return cliente

def listar_contas(cliente: Cliente):
    if not isinstance(cliente, Cliente):
        print("Cliente inválido. Deve ser um objeto da classe Cliente.")
        return

    contas = cliente.listar_contas()
    print(f"Contas do cliente {cliente.nome}:")
    for i, conta in enumerate(contas, 1):
        print(f"Conta {i}: {conta}")

def realizar_deposito(conta: Conta, valor: float):
    if not isinstance(conta, Conta):
        print("Conta inválida. Deve ser um objeto da classe Conta.")
        return
    if not isinstance(valor, (int, float)) or valor <= 0:
        print("Valor de depósito inválido. Deve ser um número positivo.")
        return

    mensagem = conta.depositar(valor)
    print(mensagem)

def realizar_saque(conta: Conta, valor: float):
    if not isinstance(conta, Conta):
        print("Conta inválida. Deve ser um objeto da classe Conta.")
        return
    if not isinstance(valor, (int, float)) or valor <= 0:
        print("Valor de saque inválido. Deve ser um número positivo.")
        return

    mensagem = conta.sacar(valor)
    print(mensagem)

def exibir_extrato(conta: Conta):
    if not isinstance(conta, Conta):
        print("Conta inválida. Deve ser um objeto da classe Conta.")
        return

    extrato = conta.visualizar_extrato()
    print(extrato)

# Funções de Menu

def criar_cliente(banco: Banco):
    nome = input("Nome do cliente: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    cpf = input("CPF (apenas números): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade sigla estado): ")

    try:
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    except ValueError:
        print("Data de nascimento inválida. Utilize o formato dd/mm/aaaa.")
        return

    cliente = criar_usuario(banco, nome, data_nascimento, cpf, endereco)
    if cliente:
        print(f"Cliente {cliente.nome} cadastrado com sucesso.")

def criar_conta(banco: Banco):
    cpf = input("CPF do cliente para criar a conta (apenas números): ")
    saldo_inicial = input("Saldo inicial da conta: ")
    
    try:
        saldo_inicial = float(saldo_inicial)
    except ValueError:
        print("Saldo inicial inválido. Deve ser um número.")
        return

    conta = banco.criar_conta_corrente_por_cpf(cpf, saldo_inicial)
    if conta:
        print(f"Conta criada com sucesso. Número da conta: {conta.numero}")

def realizar_transacao(conta: Conta, tipo_transacao: str):
    valor = input(f"Valor do {tipo_transacao.lower()}: ")

    try:
        valor = float(valor)
    except ValueError:
        print("Valor inválido. Deve ser um número.")
        return

    if tipo_transacao.lower() == "depósito":
        mensagem = conta.depositar(valor)
    elif tipo_transacao.lower() == "saque":
        mensagem = conta.sacar(valor)
    else:
        print("Tipo de transação inválido.")
        return

    print(mensagem)

def exibir_extrato(conta: Conta):
    print(conta.visualizar_extrato())

def main():
    banco = Banco()

    while True:
        print("\nMenu:")
        print("1. Criar cliente")
        print("2. Criar conta corrente")
        print("3. Realizar depósito")
        print("4. Realizar saque")
        print("5. Exibir extrato")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_cliente(banco)
        elif opcao == "2":
            criar_conta(banco)
        elif opcao == "3":
            cpf = input("CPF do cliente (apenas números): ")
            conta = banco.buscar_cliente_por_cpf(cpf)
            if conta:
                realizar_transacao(conta, "Depósito")
            else:
                print("Cliente não encontrado.")
        elif opcao == "4":
            cpf = input("CPF do cliente (apenas números): ")
            conta = banco.buscar_cliente_por_cpf(cpf)
            if conta:
                realizar_transacao(conta, "Saque")
            else:
                print("Cliente não encontrado.")
        elif opcao == "5":
            cpf = input("CPF do cliente (apenas números): ")
            conta = banco.buscar_cliente_por_cpf(cpf)
            if conta:
                exibir_extrato(conta)
            else:
                print("Cliente não encontrado.")
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
