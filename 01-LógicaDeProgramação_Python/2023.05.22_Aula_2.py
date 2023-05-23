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

