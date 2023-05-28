# Escreva uma função que recebe dois números como parâmetros e retorna a soma deles.

def soma(a, b):
  return (a + b)

soma(3, 10)

# Crie uma função que recebe uma lista de números e retorna o maior valor presente na lista.

def maior(lista: list) -> list:
  """ Retorna o maior valor da lista """
  return max(lista)

?maior
maior([5, 3, 21, 10])

# Faça uma função que recebe uma string e retorna a mesma string invertida.

def reverso(texto: str) -> str:
  return texto[::-1]

reverso("pedro")

# Implemente uma função que recebe uma lista de palavras e retorna uma nova lista contendo apenas as palavras com mais de cinco letras.

def more_than_five(array):
  result = []
  for i in array:
    if len(i) > 5:
      result.append(i)
  return result

more_than_five(["Pedro", "Ok", "Gesticulando", "Não"])

# Escreva uma função que recebe uma lista de números e retorna a média dos valores.

def media(lista):
  soma = sum(lista)
  tamanho = len(lista)
  return (soma / tamanho)

media([12, 34, 56, 12])

# Crie uma função que verifica se um número é primo e retorna True ou False.

def primo(number):
  count = 0
  for i in range(1, (number+1)):
    if number % i == 0:
      count += 1
  if count == 2:
    return True
  else:
    return False

primo(23)

# Faça uma função que recebe uma lista de números e retorna uma nova lista contendo apenas os números pares.

def pares(lista):
  result = []
  for e in lista:
    if e % 2 == 0:
      result.append(e)
  return result

pares([5, 10, 16, 17, 20, 21])

# Implemente uma função que recebe uma lista de strings e retorna o número total de caracteres em todas as strings.

def soma_caracteres(lista):
  return len("".join(lista))

soma_caracteres(["Pedro", "P", "e", "d", "r", "o"])

# Escreva uma função que recebe uma lista de números e retorna o produto de todos os valores.

def soma_de_tudo(lista):
  total = 0
  for e in lista:
    total += e
  return total

soma_de_tudo([5, 7, 8, 10])

# Crie uma função que recebe uma lista de nomes e retorna uma nova lista com os nomes em ordem alfabética.

def ordenado(lista):
  return sorted(lista)

ordenado(["Pedro", "Adriana", "Leonardo", "Sabrina"])

# Faça uma função que recebe uma lista de números e retorna uma nova lista com os valores duplicados removidos.

def num_unicos(lista):
  result = []
  for e in lista:
    if e not in result:
      result.append(e)
  return result

num_unicos([2, 3, 7, 2, 5, 7, 3])

# Implemente uma função que recebe uma string e retorna o número de vogais presentes nela.

def count_vogais(string):
  vogais = ["a", "e", "i", "o", "u"]
  result = 0
  for e in string.lower():
    if e in vogais:
      result += 1
  return result

count_vogais("ParalelePIPEDO")

# Escreva uma função que recebe uma lista de números e retorna uma nova lista contendo apenas os números ímpares.

def impares(lista):
  result = []
  for e in lista:
    if e % 2 != 0:
      result.append(e)
  return result

impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Crie uma função que recebe um número inteiro e retorna True se ele for um número perfeito, ou False caso contrário.
# * Um número perfeito é aquele que é igual à soma de seus divisores próprios.

def perfeito(inteiro):
  div = []
  for num in range(1,(inteiro)):
    if inteiro % num == 0:
      div.append(num)
  if sum(div) == inteiro:
    return True
  else:
    return False

perfeito(33550336)

# Faça uma função que recebe uma lista de strings e retorna uma nova lista contendo apenas as strings que começam com a letra 'A' (maiúscula ou minúscula).

def inicio_a(lista):
  result = []
  for e in lista:
    if e.lower()[0] == 'a':
      result.append(e)
  return result

inicio_a(["Amora", "Jambo", "Arroz", "melancia", "abacate", "anchoVA"])
