# Sistema Bancário em Python

Este projeto implementa um sistema bancário básico em Python utilizando princípios de Orientação a Objetos. O sistema permite o gerenciamento de clientes e contas bancárias, incluindo a criação de clientes, abertura de contas e a realização de transações como depósitos e saques.

## Funcionalidades

- **Cadastro de Clientes**: Permite a criação de novos clientes com informações como nome, data de nascimento, CPF e endereço.
- **Criação de Contas Bancárias**: Cria contas bancárias associadas a clientes existentes. O número da conta é gerado sequencialmente.
- **Realização de Transações**: Permite realizar depósitos e saques em contas bancárias, com um limite diário de transações.
- **Visualização de Extrato**: Exibe o histórico de transações e o saldo atual de uma conta.

## Estrutura das Classes

### `Transacao`
Representa uma transação bancária com tipo (depósito ou saque) e valor. Inclui a data e hora da transação.

### `Historico`
Gerencia as transações realizadas em uma conta. Armazena um histórico completo de todas as transações.

### `Conta`
Representa uma conta bancária com saldo, número da conta, agência fixa e histórico de transações. Permite depósitos, saques e visualização do extrato. Controla o limite diário de transações.

### `Cliente`
Base para clientes do sistema. Armazena informações pessoais e uma lista de contas associadas.

### `PessoaFisica`
Subclasse de `Cliente`, representa clientes individuais com CPF. Armazena o CPF como uma string numérica.

### `Banco`
Gerencia clientes e contas bancárias. Permite o cadastro de novos clientes, criação de contas e busca de clientes por CPF.

## Funcionalidades de Menu

O menu interativo permite ao usuário:

1. **Criar Cliente**: Adiciona um novo cliente ao banco.
2. **Criar Conta Corrente**: Abre uma nova conta para um cliente existente.
3. **Realizar Depósito**: Adiciona fundos à conta bancária.
4. **Realizar Saque**: Retira fundos da conta bancária.
5. **Exibir Extrato**: Mostra o extrato e o saldo atual da conta.
6. **Sair**: Encerra o programa.

## Uso

Para executar o sistema, execute o script principal:

```bash
python main.py
