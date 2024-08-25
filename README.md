# Sistema Bancário em Python

## Descrição do Projeto

Este projeto implementa um sistema bancário básico em Python, que permite a criação de usuários, gerenciamento de contas bancárias, realização de transações (depósitos e saques), e visualização de extratos. O sistema foi desenvolvido utilizando conceitos de orientação a objetos e boas práticas de programação.

## Funcionalidades

- **Cadastro de Usuários:** Criação de novos usuários com os seguintes dados:
  - Nome
  - Data de nascimento
  - CPF (apenas números)
  - Endereço (no formato: "logradouro, nro - bairro - cidade sigla estado")

- **Gerenciamento de Contas:** Cada usuário pode ter uma ou mais contas bancárias, que incluem:
  - Número da agência (fixo: "0001")
  - Número da conta (sequencial, começando em 1)
  - Saldo inicial

- **Operações Bancárias:**
  - Depósitos em conta
  - Saques de conta (respeitando o saldo disponível)
  - Limite de transações diárias

- **Visualização de Extratos:** Mostra todas as transações realizadas em uma conta específica e o saldo atual.

## Requisitos

- Python 3.x

## Instalação

Clone o repositório para o seu ambiente local:

```bash
git clone <URL_DO_SEU_REPOSITORIO>

Navegue até o diretório do projeto:

bash

cd <NOME_DO_DIRETORIO_DO_PROJETO>

Como Usar

    Executar o programa principal:

    Para rodar o sistema bancário, execute o arquivo principal do projeto:

    bash

python <nome_do_arquivo_principal>.py

Cadastro de Usuários:

Use a função criar_usuario() para cadastrar um novo usuário no sistema, fornecendo nome, data de nascimento, CPF e endereço.

Criação de Contas:

Utilize a função criar_conta_corrente_por_cpf() passando o CPF do usuário para criar uma nova conta bancária vinculada ao usuário.

Operações Bancárias:

    Para realizar depósitos, use a função realizar_deposito().
    Para saques, utilize realizar_saque().
    Para visualizar o extrato, use exibir_extrato().
