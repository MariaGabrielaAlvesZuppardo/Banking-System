# Banking-System

## Descrição
Este é um sistema bancário simples em Python que permite realizar operações básicas de uma conta bancária, incluindo depósitos, saques e visualização do extrato. O sistema armazena um histórico das transações realizadas e o saldo atual da conta.

### Funcionalidades
Depositar: Adiciona um valor ao saldo da conta e registra a transação.
Sacar: Remove um valor do saldo da conta, se houver saldo suficiente, e registra a transação.
Visualizar Extrato: Exibe o histórico das transações e o saldo atual da conta.

### Estrutura do Código
- Classe ContaBancaria
- Método __init__(self, saldo_inicial=0): Inicializa a conta com um saldo inicial e um histórico de transações vazio.

- Método depositar(self, valor):

- Adiciona um valor positivo ao saldo da conta.
- Registra a transação no histórico.
- Método sacar(self, valor):

- Remove um valor positivo do saldo da conta, se houver saldo suficiente.
- Registra a transação no histórico.
- Método visualizar_extrato(self):

Exibe todas as transações realizadas e o saldo atual da conta.
