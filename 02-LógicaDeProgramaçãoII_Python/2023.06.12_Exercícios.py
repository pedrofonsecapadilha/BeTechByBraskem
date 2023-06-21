# Exercícios

# Exercício 01
    # Crie um dicionário cujas chaves são os meses do ano e os valores são a duração (em dias) de cada mês.

cal_2023 = {"Janeiro": 31,"Fevereiro": 28,"Março": 31,"Abril": 30,"Maio": 31,"Junho": 30,"Julho": 31,"Agosto": 31,"Setembro": 30,"Outubro": 31,"Novembro": 30,"Dezembro": 31}
print(cal_2023)

# Exercício 02
    # Imprima as chaves seguidas dos seus valores para dicionário criado no exercício 1. Exemplo:
    # Janeiro - 31
    # Fevereiro - 28
    # Março - 31
    # ...

for chave, valor in cal_2023.items():
  print(f"{chave} - {valor}")

# Exercício 03
    # Crie uma função que receba os valores do nome, idade e e-mail de uma pessoa e guarde-os em um dicionário com as chaves ‘nome’, ‘idade’ e ‘email’, respectivamente. Sua função deve retornar esse dicionário.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
email = input("Digite seu e-mail: ")

cadastro = {}

cadastro['nome'] = nome
cadastro['idade'] = idade
cadastro['email'] = email

print(cadastro)

# Exercício 04
    # Faça um programa que fique pedindo uma resposta do usuário, entre 1, 2 e 3. Se o usuário digitar 1, o programa deve cadastrar um novo usuário nos moldes do exercício anterior e guardar esse cadastro num dicionário cuja chave será o CPF da pessoa. Quando o usuário digitar 2, o programa deve imprimir os usuários cadastrados; e se o usuário digitar 3, o programa deve fechar. Exemplo do dicionário:
    # {
    #  '987.654.321-00': {'nome': Maria, 'idade': 20, 'email': maria@gmail.com}
    # }

def exibir_menu():
  print('''\nEscolha uma opção:
1. Cadastrar um usuário
2. Imprimir usuários cadastrados
3. Procurar por CPF
4. Sair
        ''')

def cadastrar(usuarios):
  cpf = input("Digite seu CPF: ")
  nome = input("Digite seu nome: ")
  idade = int(input("Digite sua idade: "))
  email = input("Digite seu e-mail: ")
  cadastro = {}
  cadastro['nome'] = nome
  cadastro['idade'] = idade
  cadastro['email'] = email
  usuarios[cpf] = cadastro

def listar(usuarios):
  for chave, valor in usuarios.items():
    print(f"{chave}: {valor}")

def procurar(usuarios):
  cpf = input("Digite o CPF para busca: ")

def main():
  usuarios = {}
  while True:
    exibir_menu()
    opcao = int(input("Opção: "))
    if opcao == 1:
      cadastrar(usuarios)
    elif opcao == 2:
      listar(usuarios)
    elif opcao == 3:
      procurar(usuarios)
    elif opcao == 4:
      break
    else:
      print("Opção inválida!")

main()

# Exercício 05
    # Implemente um sistema de busca para o programa do exercício anterior, isso é, se o usuário digitar 4, procure um determinado usuário pelo seu CPF.
    # Resolvido no código anterior.