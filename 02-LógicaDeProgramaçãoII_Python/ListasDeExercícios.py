# 1. Concatene as tuplas “frutas” e “numeros” em uma nova tupla chamada “combinado”.

frutas = ("Morango", "Abacate", "Banana", "Jaca")
numeros = (1, 2, 3, 4)
combinado = frutas + numeros
print(combinado)

# 2. Verifique se o elemento “maçã” está presente na tupla “combinado”.

"maçã" in combinado

# 3. Acesse os três últimos elementos da tupla “combinado”.

combinado[-3:]

# 4. Crie uma tupla chamada “repeticao” com três elementos repetidos de sua escolha.

repeticao = (1, 1, 1)

# 5. Converta a tupla “repeticao” em uma lista.

list(repeticao)

# 6. Crie uma nova tupla chamada “invertida” que contenha os elementos da tupla “combinado” em ordem inversa.

combinado_inv = combinado[-1::-1]
print(combinado_inv)

# 7. Crie uma tupla chamada "alunos" com cinco elementos, onde cada elemento é uma tupla contendo o nome e a nota de um aluno.

alunos = (("Jorge", 5.5), ("Amanda", 8.8), ("Matias", 4.3), ("Ana", 7.0), ("Lis", 6.0))
print(alunos)
print(type(alunos))

# 8. Crie uma função chamada "media_turma" que receba a tupla "alunos" como argumento e retorne a média das notas da turma.

soma = 0
for al in alunos:
  soma += al[1]
media_turma = soma / (len(alunos))
print(media_turma)

# 9. Crie um dicionário vazio chamado "pessoa" e adicione as chaves "nome" e "idade" com os valores correspondentes.

pessoa = {}
pessoa["nome"] = ["Pedro", "Larissa", "Jobson", "Monique"]
pessoa["idade"] = [34, 27, 43, 61]
print(pessoa)

# 10. Escreva um programa que conte a frequência de cada letra em uma palavra. O programa deve solicitar ao usuário uma palavra e exibir o resultado em um dicionário, onde as chaves são as letras e os valores são as contagens.

palavra = input("Digite a palavra a ser analisada: ").upper()
resultado = {}
for e in list(palavra):
  if e in list(palavra):
    resultado[e] = list(palavra).count(e)
print(resultado)

# 11. Crie um dicionário chamado "estoque" com os seguintes itens: "maçãs" (10), "bananas" (5) e "laranjas" (15). Em seguida, escreva um programa que permita ao usuário atualizar a quantidade de um determinado item e exiba o estoque atualizado.

estoque = {"maçãs": 10, "bananas": 5, "laranjas": 15}
while True:
  print("\nA seguir os itens do seu estoque:")
  for chave in estoque:
    print(f" -> {chave} = {estoque[chave]} un.")
  info = int(input("\nQual opção deseja executar?\n(0) Para sair\n(1) Para atualizar estoque\n"))
  if info == 0:
    break
  elif info == 1:
    elemento = (input("\nEscreva qual item você deseja atualizar: "))
    while elemento not in estoque:
      print("Item não existente, tente novamente.")
      elemento = (input("\nEscreva qual item você deseja atualizar: "))
    nova_quantidade = int(input(f"Digite a nova quantidade de {elemento.upper()} do estoque: "))
    while nova_quantidade < 0:
      print("A quantidade deve ser maior ou igual a 0")
      nova_quantidade = int(input(f"\nDigite a nova quantidade de {elemento.upper()} do estoque: "))
    estoque[elemento] = nova_quantidade
  else:
    print("Opção inválida, tente novamente.")

# 12. Escreva um programa que leia um texto fornecido pelo usuário e conte a ocorrência de cada palavra. O programa deve exibir o resultado em um dicionário, onde as chaves são as palavras e os valores são as contagens.

texto = input("Digite o texto para análise:\n").lower()
texto_sep = texto.split(" ")
resultado = {}
for palavra in texto_sep:
  if palavra in texto_sep:
    resultado[palavra] = texto_sep.count(palavra)
print(resultado)

# 13. Crie um dicionário chamado "agenda" que armazene contatos. Cada contato deve ter um nome como chave e um número de telefone como valor. Escreva um programa que permita ao usuário adicionar novos contatos, remover contatos existentes e exibir todos os contatos da agenda.

agenda = {"PEDRO": 987654321, "SUELY": 123456789, "FLAVIO": 123654789, "CLAUDIA": 789654123}

def create():
  print("\nVamos ADICIONAR um novo contato")
  name = input("Digite o NOME para salvar na agenda: ").upper()
  phone = input(f"Digite telefone do(a) {name}: ")
  agenda[name] = phone

def delete():
  contact = input("Digite o NOME do contato que deseja remover: ").upper()
  if contact in agenda:
    print(f"Você deseja remover o contato a seguir?\n !!!!! {contact} -> {agenda[contact]} !!!!!")
    ans = int(input("Digite 99 para REMOVER o contato: "))
    if ans == 99:
      agenda.pop(contact)
    else:
      print("O contato NÃO foi removido!")
  else:
    print("Desculpe, o nome do contato não encontrado :(")

def show(elemento):
  print("\nA seguir todos os dados salvos na agenda:")
  for chave in agenda:
    print(f" -> {chave}: {agenda[chave]}")

def menu():
  print("\n--- BEM VINDO A SUA AGENDA ---")
  input_exist = False
  while input_exist == False:
    user_input = input("\nDigite o número da opção desejada:\n1- Para EXIBIR todos contatos\n2- Para ADICIONAR um novo contato\n3- Para REMOVER um contato\n9- Para SAIR do programa\n")
    if user_input == '1':
      show(agenda)
    elif user_input == '2':
      create()
    elif user_input == '3':
      delete()
    elif user_input == '9':
      print("\nAté breve ;)")
      break
    else:
      print("ERRO! Opção Inválida, tente novamente!")

menu()

# 14. Escreva uma função geradora chamada "contador" que recebe um número inteiro como parâmetro e gera uma sequência de números de 1 até o número fornecido.

contador = (x for x in range(1, 21))
for elemento in contador:
    print(elemento)

# 15. Implemente uma função geradora chamada "letras_maiusculas" que recebe uma string como parâmetro e gera as letras maiúsculas dessa string, uma por vez.

def letras_maiusculas(s):
  up = s.upper()
  for letter in up:
    print(letter)

letras_maiusculas("idênticos")

# 16. Escreva uma função geradora chamada "pares" que recebe um número inteiro como parâmetro e gera uma sequência de números pares a partir de 0 até o número fornecido.

pares = (x for x in range(31) if x % 2 == 0)

for e in pares:
  print(e)

def pares(n):
  for e in range(n+1):
    if e % 2 == 0:
      print(e)

pares(31)

# 17. Escreva um iterador chamado "Contador" que gera uma sequência de números a partir de 1 até um número fornecido pelo usuário.

class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.valor_atual = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.valor_atual <= self.limite:
            valor = self.valor_atual
            self.valor_atual += 1
            return valor
        else:
            raise StopIteration

# Exemplo de uso
limite = int(input("Digite o número limite: "))
contador = Contador(limite)

for numero in contador:
    print(numero)

# 18. Implemente um iterador chamado "Multiplos" que recebe um número inteiro e um limite como parâmetros, e gera os múltiplos desse número até o limite fornecido.

class Multiplos:
    def __init__(self, numero, limite):
        self.numero = numero
        self.limite = limite
        self.atual = numero

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual > self.limite:
            raise StopIteration
        resultado = self.atual
        self.atual += self.numero
        return resultado

iterador = Multiplos(3, 20)

for numero in iterador:
    print(numero)