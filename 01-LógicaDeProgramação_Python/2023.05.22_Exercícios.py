# While

# 1. Contagem regressiva: Escreva um programa que solicite ao usuário um número e faça uma contagem regressiva a partir desse número até 0. Use um loop while para executar a contagem regressiva.

num_1 = int(input("Digite um número positivo: "))

if num_1 > 0:
  while num_1 != 0:
    print(num_1)
    num_1 -= 1
else:
  while num_1 != 0:
    print(num_1)
    num_1 += 1
print(0)

# 2. Soma dos dígitos: Escreva um programa que solicite ao usuário um número inteiro positivo e calcule a soma de seus dígitos. Use um loop while para iterar sobre os dígitos do número.

num_2 = int(input("Digite um número inteiro positivo: "))
soma = 0

while num_2 > 0:
  e = num_2 % 10
  soma += e
  num_2 //= 10
print(soma)

# 3. Adivinhe o número: Escreva um programa que escolha aleatoriamente um número entre 1 e 100 e peça ao usuário para adivinhar qual é o número. Forneça dicas indicando se o número é maior ou menor. Use um loop while até que o usuário adivinhe corretamente.

import random
rand = random.randint(0,100)
# print(rand)

num_3 = int(input("Digite um número: "))

while num_3 != rand:
  print("Você Errou :(")
  if num_3 < rand:
    print(f"A resposta é um número MAIOR que {num_3}")
  else:
    print(f"A resposta é um número MENOR que {num_3}")
  num_3 = int(input("\nDigite um número: "))
print("Parabéns, você acertou!!!")

# 4. Tabuada: Escreva um programa que solicite ao usuário um número inteiro e exiba a tabuada desse número de 1 a 10. Use um loop while para calcular e exibir cada multiplicação.

num_4 = int(input("Digite um número inteiro: "))
count = 1

while count <= 10:
  print(f"{num_4} x {count} = {num_4*count}")
  count += 1

# 5. Fatorial: Escreva um programa que solicite ao usuário um número inteiro positivo e calcule o fatorial desse número. Use um loop while para realizar a multiplicação dos fatores.

num_5 = int(input("Digite um número inteiro positivo: "))
fatorial = 1

while num_5 != 0:
  fatorial *= num_5
  num_5 -= 1

print(f"O fatorial é: {fatorial}")

# -------------------------------------------------

# For

# 1. Imprimir números pares: Escreva um programa que imprima todos os números pares de 1 a 20, utilizando o loop for.

for par in range(2, 21, 2):
  print(par)

# 2. Calcular a média: Escreva um programa que solicite ao usuário cinco números e, em seguida, calcule e exiba a média dos números fornecidos.

num_21 = float(input('Digite 1º de 5 números: '))
num_22 = float(input('Digite 2º de 5 números: '))
num_23 = float(input('Digite 3º de 5 números: '))
num_24 = float(input('Digite 4º de 5 números: '))
num_25 = float(input('Digite 5º de 5 números: '))

media_2 = (num_21 + num_22 + num_23 + num_24 + num_25) / 5

print(f'A média dos cinco números digitados é: {round(media_2,1)}')

# 3. Contagem de vogais: Escreva um programa que solicite ao usuário uma palavra e conte quantas vogais existem nessa palavra.

palavra = input("Digite uma palavra: ")

vogais = ['a', 'e', 'i', 'o', 'u']
count = 0

for e in list(palavra.lower()):
  if e in vogais:
    count += 1
  else:
    count += 0

print(f'Exitem {count} vogais na palavra {palavra}')

# 4. Tabela de multiplicação: Escreva um programa que exiba a tabela de multiplicação de 1 a 10, ou seja, para cada número de 1 a 10, exiba sua multiplicação com os números de 1 a 10.

for num_4 in range(1,11):
  for mult in range(1,11):
    print(f'{num_4} x {mult} = {num_4 * mult}')
  print('----------')

# 5. Soma dos elementos: Escreva um programa que receba uma lista de números e calcule a soma de todos os elementos da lista

array_5 = []

num_5 = input('Digite um número [escreva SAIR para encerrar]: ')
while num_5 != 'SAIR':
  array_5.append(float(num_5))
  num_5 = input('Digite um número [escreva SAIR para encerrar]: ')

print(f"A soma dos números digitados é: {sum(array_5)}")

# -------------------------------------------------

# Lista

# 1. Soma dos elementos: Escreva um programa que receba uma lista de números e calcule a soma de todos os elementos da lista.

    # Exercício repetido com FOR 5

# 2. Maior e menor elementos: Escreva um programa que encontre o maior e o menor elemento em uma lista de números.

from numpy import random

rand_arr = random.randint(1000, size=(7))
max = 0
min = 1000

for e in rand_arr:
  if e > max:
    max = e
  elif e < min:
    min = e

print(f"A lista é: {rand_arr}\n")
print(f"O MAIOR elemento da lista é: {max}")
print(f"O MENOR elemento da lista é: {min}")


# 3. Remoção de elementos repetidos: Escreva um programa que remova os elementos duplicados de uma lista.

from numpy import random
rand_arr = list(random.randint(6, size=(20)))

print(f"A lista original é:\n{list(rand_arr)}")
result = []

for e in rand_arr:
  if e in result:
    continue
  else:
    result.append(e)

print(f"A lista sem os elementos duplicados é:\n{result}")

# 4. Números pares: Escreva um programa que receba uma lista de números e crie uma nova lista contendo apenas os números pares da lista original.

from numpy import random
num_arr = random.randint(10, size=(6))

pares = []

for e in num_arr:
  if e % 2 == 0:
    pares.append(e)

print(f"A lista só com o elementos pares é: {pares}")

# 5. Inversão da lista: Escreva um programa que inverta uma lista de elementos.

from numpy import random
some_arr = random.randint(100, size=(10))

print(f"A lista original é: {list(some_arr)}")
print(f"A lista invertida é: {list(reversed(some_arr))}")
