# Parabéns!
# Você foi contratado para trabalhar no RH de um empresa Multinacional como trainee! Na sua primeira semana, você vai trabalhar no RH.
# Sua primeira demanda é criar um sistema que cumpra os seguintes requisitos:
# - Seu sistema deverá armazenar os registros dos funcionários. Os registros são, no mínimo: Telefone, Nome, Sobrenome, Profissão e Data de nascimento.
# - Seu sistema deve ser capaz de fazer as operações básicas de um banco de dados: Criar, Ler, Atualizar e Deletar, ou seja:
# - Criar: deve ser possível receber novos registros pelo usuario e armazenar no seu sistema.
# - Ler: O usuário deve conseguir encontrar o registro completo, procurando pelo nome ou pela profissão. Sejam apresentados os dados de forma que o nome tenha as primeiras letras maiúsculas. O número deve ser apresentado no formato "(dd)1234-5678". E apresentar de forma mais visual possível.
# - Atualizar: O usuário deve conseguir atualizar o registro, buscando pelo número de telefone.
# - Deletar: O usuário deve conseguir deletar o registro buscando pelo numero do telefone.
# - Cada operação deverá ser chamada por uma função própria.
# - Deverá ser possível chamar uma única função chamada `menu()` que vai permitir ao usuário a chamar as diferentes operações.

data_base = [["1112341234", "pedro", "padilha", "cientista de dados", "13/07/1988"],
             ['1145674567', 'suely', 'fonseca', 'web dev', '15/07/1969'],
             ['1112371237', 'manoela', 'marra', 'back end', '26/08/1991'],
             ['1145684568', 'pedro', 'baptista', 'front end', '01/01/1950'],
             ['1198769876', 'lina', 'costa', 'web dev', '24/01/2000']]

# FUNÇÕES CRUD

def create():
  print("\nVamos CRIAR um novo registro")
  # Entrada do telefone:
  phone = input("Digite seu número de telefone: ")
  remove = ["(", ")", "-", "/", ",", ".", "[", "]", "{", "}", "_", "+", " "]
  for e in remove:
    phone = phone.replace(e, "")
  if phone[0] == "0":
    phone = phone.lstrip(phone[0])
  # Entrada do nome:
  name = input("Digite seu primeiro nome: ").lower().replace(" ", "")
  # Entrada do sobrenome:
  last_name = input("Digite seu sobrenome: ").lower()
  # Entrada da profissão:
  profession = input("Digite sua profissão: ").lower()
  # Data de aniversário:
  day = int(input("Digite o DIA do seu aniversário [1-31]: "))
  while day < 1 or day > 31:
    print("ERRO! DIA inexistente, por gentileza digite o DIA corretamente [1-31]!")
    day = int(input("Digite o DIA do seu aniversário [1-31]: "))
  month = int(input("Digite o MÊS do seu aniversário [1-12]: "))
  while month < 1 or month > 12:
    print("ERRO! MÊS inexistente, por gentileza digite o MÊS corretamente [1-12]!")
    month = int(input("Digite o MÊS do seu aniversário [1-12]: "))
  year = int(input("Digite o ANO do seu aniversário [1900-2023]: "))
  while year < 1900 or year > 2023:
    print("ERRO! ANO inválido, por gentileza coloque o ANO corretamente [1900-2023], ex.: 1976")
    year = int(input("Digite o ANO do seu aniversário [1900-2023]: "))
  birthday = str(day) + "/" + str(month) + "/" + str(year)
  # Adiciona as entradas de dados no banco de dado geral:
  data_base.append([phone, name, last_name, profession, birthday])
  return print(f"\nREGISTRO ADICIONADO:\n Telefone: ({phone[:2]}) {phone[2:6]}-{phone[6:11]}\n Nome: {name.capitalize()}\n Sobrenome: {last_name.capitalize()}\n Profissão: {profession.capitalize()}\n Aniversário: {birthday}")

def read():
  # Busca pelo nome ou profissão:
  read_input = ""
  while read_input != '1' or read_input != '2' or read_input != '9':
    read_input = input("\nDigite o número da opção desejada:\n1- Para busca a partir do NOME\n2- Para busca a partir da PROFISSÃO\n9- Para MENU INICIAL\n")
    if read_input == '1':
      # Achando o elemento no banco de dados - NOME
      result = []
      exist_in_data_base = False
      while exist_in_data_base == False:
        search_name = input("\nDigite o NOME do registro que você quer encontrar? ").lower().replace(" ", "")
        for e in data_base:
          if e[1] == search_name:
            result.append(e)
        if result != []:
          exist_in_data_base = True
          print("\n------ REGISTROS DO CRM DA BRASKEM -------")
          print(f"NOME: {search_name.capitalize()}")
          show(result)
          print("\n------------------ FIM -------------------")
          break
        else:
          print("ERRO! Nome não encontrado nos nossos registro :(")
          break
    elif read_input == '2':
      # Achando o elemento no banco de dados - PROFISSÃO
      result = []
      exist_in_data_base = False
      while exist_in_data_base == False:
        search_profession = input("\nDigite a PROFISSÃO do registro que você quer encontrar? ").lower()
        for e in data_base:
          if e[3] == search_profession:
            result.append(e)
        if result != []:
          exist_in_data_base = True
          print("\n------ REGISTROS DO CRM DA BRASKEM -------")
          print(f"PROFISSÃO: {search_profession.capitalize()}")
          show(result)
          print("\n------------------ FIM -------------------")
          break
        else:
          print("ERRO! Profissão não encontrada nos nossos registro :(")
          break
    elif read_input == '9':
      break
    else:
      print("ERRO! Opção Inválida, tente novamente!")

def update():
  # Entrada do telefone
  exist_in_data_base = False
  while exist_in_data_base == False:
    search_update = input("\nDigite o número do telefone para ATUALIZAR o registro: ")
    remove = ["(", ")", "-", "/", ",", ".", "[", "]", "{", "}", "_", "+", " "]
    for e in remove:
      search_update = search_update.replace(e, "")
    if search_update[0] == "0":
      search_update = search_update.lstrip(search_update[0])
    for e in data_base:
      if e[0] == search_update:
        exist_in_data_base = True
    if exist_in_data_base == False:
      print("ERRO! Número não encontrado nos nossos registro :(")
      break
  # Achando o elemento no banco de dados
  for e in data_base:
    if e[0] == search_update:
      print(f"\nDADOS CADASTRADOS:\n Telefone: ({e[0][:2]}) {e[0][2:6]}-{e[0][6:11]}\n Nome: {e[1].capitalize()}\n Sobrenome: {e[2].capitalize()}\n Profissão: {e[3].capitalize()}\n Aniversário: {e[4]}\n")
      read_input = ""
      while read_input != '1' or read_input != '2' or read_input != '3' or read_input != '4' or read_input != '5' or read_input != '9':
        read_input = input("\nDigite o número da opção para ATUALIZAR o registro:\n1- TELEFONE\n2- NOME\n3- SOBRENOME\n4- PROFISSÃO\n5- DATA DE ANIVERSÁRIO\n9- Retornar ao MENU INICIAL\n")
        if read_input == '1':
          # Atualizando o telefone:
          new_phone = input("ATUALIZE seu número de telefone: ")
          remove = ["(", ")", "-", "/", ",", ".", "[", "]", "{", "}", "_", "+", " "]
          for e1 in remove:
            new_phone = new_phone.replace(e1, "")
          if new_phone[0] == "0":
            new_phone = new_phone.lstrip(new_phone[0])
          e[0] = new_phone
          return print(f"\nTELEFONE atualizado: ({new_phone[:2]}) {new_phone[2:6]}-{new_phone[6:11]}")
        elif read_input == '2':
          # Atualizando o nome:
          new_name = input("ATUALIZE seu primeiro nome: ").lower().replace(" ", "")
          e[1] = new_name
          return print(f"\nNOME atualizado: {new_name.capitalize()}")
        elif read_input == '3':
          # Atualizando o sobrenome:
          new_last_name = input("ATUALIZE seu sobrenome: ").lower()
          e[2] = new_last_name
          return print(f"\nSOBRENOME atualizado: {new_last_name.capitalize()}")
        elif read_input == '4':
          # Atualizando a profissão:
          new_profession = input("ATUALIZE sua profissão: ").lower()
          e[3] = new_profession
          return print(f"\nPROFISSÃO atualizada: {new_profession.capitalize()}")
        elif read_input == '5':
          # Atualizando a data de aniversário:
          new_day = int(input("ATUALIZE o DIA do seu aniversário [1-31]: "))
          while new_day < 1 or new_day > 31:
            print("ERRO! DIA inexistente, por gentileza digite o DIA corretamente [1-31]!")
            new_day = int(input("ATUALIZE o DIA do seu aniversário [1-31]: "))
          new_month = int(input("ATUALIZE o MÊS do seu aniversário [1-12]: "))
          while new_month < 1 or new_month > 12:
            print("ERRO! MÊS inexistente, por gentileza digite o MÊS corretamente [1-12]!")
            new_month = int(input("ATUALIZE o MÊS do seu aniversário [1-12]: "))
          new_year = int(input("ATUALIZE o ANO do seu aniversário [1900-2023]: "))
          while new_year < 1900 or new_year > 2023:
            print("ERRO! ANO inválido, por gentileza coloque o ANO corretamente [1900-2023], ex.: 1976")
            new_year = int(input("ATUALIZE o ANO do seu aniversário [1900-2023]: "))
          new_birthday = str(new_day) + "/" + str(new_month) + "/" + str(new_year)
          e[4] = new_birthday
          return print(f"\nDATA DE ANIVERSÁRIO atualizada: {new_birthday}")
        elif read_input == '9':
          break
        else:
          print("ERRO! Opção Inválida, tente novamente!")

def delete():
  # Entrada do telefone
  exist_in_data_base = False
  while exist_in_data_base == False:
    search_delete = input("\nDigite o número do telefone para REMOVER o registro: ")
    remove = ["(", ")", "-", "/", ",", ".", "[", "]", "{", "}", "_", "+", " "]
    for e in remove:
      search_delete = search_delete.replace(e, "")
    if search_delete[0] == "0":
      search_delete = search_delete.lstrip(search_delete[0])
    for e in data_base:
      if e[0] == search_delete:
        exist_in_data_base = True
    if exist_in_data_base == False:
      print("ERRO! Número não encontrado nos nossos registro :(")
      break
  # Achando o elemento no banco de dados
  for i, e in enumerate(data_base):
    if e[0] == search_delete:
      print(f"\nDADOS CADASTRADOS:\n Telefone: ({e[0][:2]}) {e[0][2:6]}-{e[0][6:11]}\n Nome: {e[1].capitalize()}\n Sobrenome: {e[2].capitalize()}\n Profissão: {e[3].capitalize()}\n Aniversário: {e[4]}")
      delete_input = input("\nDeseja REMOVER esse registro?\n9- Cancelar (retornar para MENU PRINCIPAL)\n100- SIM (!!! REMOVER REGISTRO !!!)\n")
      # Deletando o elemento do banco de dados
      if delete_input == '100':
        # Deletar o elemento
        data_base.pop(i)
        return print("\nREGISTRO REMOVIDO !!!")

# OUTRAS FUNÇÕES

def show(lista):
  for e in lista:
    if len(e) == 5:
      print(f"\nTelefone: ({e[0][:2]}) {e[0][2:6]}-{e[0][6:11]}\nNome: {e[1].capitalize()}\nSobrenome: {e[2].capitalize()}\nProfissão: {e[3].capitalize()}\nAniversário: {e[4]} <Faltam {birth_day(e[4])} dias para o aniversário!>")
    elif len(e) == 6:
      print(f"\nTelefone: ({e[0][:2]}) {e[0][2:6]}-{e[0][6:11]}\nNome: {e[1].capitalize()}\nSobrenome: {e[2].capitalize()}\nProfissão: {e[3].capitalize()}\nAniversário: {e[4]} <Faltam {birth_day(e[4])} dias para o aniversário!>\nEndereço: {e[5]}")

def input_endereco():
  # Entrada do telefone
  exist_in_data_base = False
  while exist_in_data_base == False:
    search_adress = input("\nDigite o número do telefone para ADICIONAR O ENDEREÇO no registro: ")
    remove = ["(", ")", "-", "/", ",", ".", "[", "]", "{", "}", "_", "+", " "]
    for e in remove:
      search_adress = search_adress.replace(e, "")
    if search_adress[0] == "0":
      search_adress = search_adress.lstrip(search_adress[0])
    for e in data_base:
      if e[0] == search_adress:
        exist_in_data_base = True
    if exist_in_data_base == False:
      print("ERRO! Número não encontrado nos nossos registro :(")
      break
  # Achando o elemento no banco de dados
  for i, e in enumerate(data_base):
    if e[0] == search_adress:
      print(f"\nDADOS CADASTRADOS:\n Telefone: ({e[0][:2]}) {e[0][2:6]}-{e[0][6:11]}\n Nome: {e[1].capitalize()}\n Sobrenome: {e[2].capitalize()}\n Profissão: {e[3].capitalize()}\n Aniversário: {e[4]}")
      cep_input = input("\nDigite o CEP do endereço a ser registrado: ")
      # Adicionando o endereço no registro selecionado
      adress = recebe_cep_retorna_endereco(cep_input)
      e.append(adress)
      return print(f"Endereço adicionado no registro: {adress}")

def menu():
  print("\n------ BEM VINDO AO CRM DA BRASKEM -------")
  input_exist = False
  while input_exist == False:
    user_input = input("\nDigite o número da opção desejada:\n0- Para EXIBIR todos registros\n1- Para CRIAR um novo registro\n2- Para PESQUISAR um registro\n3- Para ATUALIZAR um registro\n4- Para REMOVER um registro\n5- Para adicionar o ENDEREÇO no registro\n9- Para SAIR do programa\n")
    if user_input == '0':
      print("\n-- TODOS OS REGISTROS DO CRM DA BRASKEM --")
      print(f"TOTAL: {len(data_base)} registros")
      show(data_base)
      print("\n------------------ FIM -------------------")
    elif user_input == '1':
      create()
    elif user_input == '2':
      read()
    elif user_input == '3':
      update()
    elif user_input == '4':
      delete()
    elif user_input == '5':
      input_endereco()
    elif user_input == '9':
      print("\nGrato por utilizar o CRM DA BRASKEM, até breve ;)")
      break
    else:
      print("ERRO! Opção Inválida, tente novamente!")

menu()

show(data_base)

# POSSÍVEIS MELHORIAS
# TO DO LIST
  # - PODE RETIRAR ALGUMAS LINHAS DE CÓDIGO REPETIDAS E FAZER FUNÇÃO, EX.: TRATAMENTO DA ENTRADA DOS DADOS DE TELEFONE.
  # - CONDIÇÃO PARA O TELEFONE TER ENTRE 10 E 11 CARACTERES, AÍ DÁ PARA MELHORAR A FORMATAÇÃO
  # - RETIRAR TODOS OS ACENTOS E SINAIS ESPECIAIS DOS NOMES, SIMPLIFICAR TUDO PARA O BANCO DE DADOS

# Bonus 1
# Quando for chamada a operação de leitura, mostrar quantos dias faltam para o aniversário pro colaborador daquele registro. Dica: use a lib `datetime`

def birth_day(elemento):
  from datetime import datetime
  date = elemento.split('/')
  a = datetime(int(date[2]),int(date[1]),int(date[0]))
  b = datetime.today()
  this_year = datetime(b.year, a.month, a.day)
  next_year = datetime(b.year+1, a.month, a.day)
  if this_year > b:
    return (this_year-b).days
  else:
    return (next_year-b).days

# Bonus 2
# Receber o CEP do colaborador e armazenar seu endereço.

def recebe_cep_retorna_endereco(cep:str) -> list:
  import requests
  cep = cep.replace("-", "").replace(".", "").replace(" ", "")
  if len(cep) == 8:
      link = f'https://viacep.com.br/ws/{cep}/json/'
      requisicao = requests.get(link)
      dic_requisicao = requisicao.json()
      uf = dic_requisicao['uf']
      cidade = dic_requisicao['localidade']
      bairro = dic_requisicao['bairro']
      logradouro = dic_requisicao['logradouro']
      return([uf, cidade, bairro, logradouro])
  else:
      raise Exception('CEP Inválido')

recebe_cep_retorna_endereco("30.441-152")
