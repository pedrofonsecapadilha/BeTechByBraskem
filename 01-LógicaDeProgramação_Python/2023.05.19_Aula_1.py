# Input e Operações Aritméticas

# 1. Escreva um programa que peça dois números ao usuário e exiba a soma deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(f'A soma dos números é: {num1 + num2}')

# 2. Crie um programa que solicite o raio de um círculo e calcule a sua área.

raio = float(input("Digite o valor do raio de um círculo: "))
print(f"A área do círculo de raio {raio} é: {3.14 * raio * raio}")

# 3. Faça um programa que leia a temperatura em Celsius e a converta para Fahrenheit.

celsius = float(input("Digite uma temperatura em graus Celsius: "))
print(f'A temperatura em graus Fahrenheit é: {(celsius * 1.8) + 32}')

# 4. Escreva um programa que peça um número ao usuário e exiba o seu dobro.

num_usuario = float(input("Digite um número para obter o seu dobro: "))
print(f"O dobro de {num_usuario} é: {num_usuario * 2}")

# 5. Crie um programa que solicite um valor em metros e o converta para centímetros.

metros = float(input("Digite o valor em metros [m]: "))
print(f"{metros} metros é igual a: {metros * 100} centímetros")

# 6. Faça um programa que peça o valor do salário de uma pessoa e exiba o valor com um aumento de 15%.

salario = int(input("Digite o valor do seu salário [R$]: "))
print(f"Seu novo salário com 15% de aumento é: R$ {salario * 1.15}")

# 7. Escreva um programa que solicite o peso e a altura de uma pessoa e calcule o seu índice de massa corporal (IMC).

peso = float(input("Qual é o seu peso [kg]? "))
altura = float(input("Qual é a sua altura [m]? "))
imc = peso/(altura ** 2)
print(f"Seu IMC é: {round(imc, 2)}")

# -------------------------------------------------

# Condicionais

# 8. Crie um programa que peça um número inteiro ao usuário e verifique se ele é par ou ímpar.

num_int = int(input("Digite um número inteiro: "))
if num_int % 2 == 0:
  print(f"O número é PAR")
else:
  print(f"O número é ÍMPAR")

# 9. Faça um programa que solicite a idade de uma pessoa e verifique se ela é maior de idade (18 anos ou mais).

idade = int(input("Digite sua idade: "))
if idade >= 18:
  print("Você é MAIOR de idade ;)")
else:
  print("Você ainda é de MENOR :(")

# 10. Escreva um programa que peça três notas de um aluno, calcule a média aritmética e exiba se ele foi aprovado (média igual ou superior a 7) ou reprovado.
# Bonus: Se quiser, pode fazer media ponderada também

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media_ari = (nota_1 + nota_2 + nota_3) / 3
# Considerando a nota_1 com peso 1, nota_2 com peso 2 e nota_3 com peso 3
media_pond = ((nota_1 * 1) + (nota_2 * 2) + (nota_3 * 3)) / (1 + 2 + 3)

print(f"\nMÉDIA ARITMÉTICA: {round(media_ari,2)}")
if media_ari >= 7:
  print("Parabéns, você foi Aprovado")
else:
  print("Infelizmente você foi reprovado :(")

print(f"\nMÉDIA PONDERADA: {round(media_pond,2)}")
if media_pond >= 7:
  print("Parabéns, você foi Aprovado")
else:
  print("Infelizmente você foi reprovado :(")

# 11. Escreva um programa que peça a idade de uma pessoa e exiba se ela é criança (0 a 12 anos), adolescente (13 a 17 anos) ou adulta (18 anos ou mais).

idade = int(input("Qual sua idade? "))

if idade >= 0 and idade <= 12:
  print(f"Você é uma CRIANÇA!")
elif idade >= 13 and idade <= 17:
  print(f"Você é uma ADOLESCENTE!")
elif idade >= 18:
  print(f"Você é uma ADULTA!")

# 12. Crie um programa que solicite um número ao usuário e verifique se ele é positivo, negativo ou zero.

numero = float(input("Digite um número: "))

if numero < 0:
  print("O número é NEGATIVO")
elif numero > 0:
  print("O número é POSITIVO")
else:
  print("O número é ZERO")

# 13. Faça um programa que peça o ano de nascimento de uma pessoa e verifique se ela é maior de idade ou menor de idade considerando o ano atual.

ano = int(input("Em qual ano você nasceu? "))

if (2023 - ano) >= 18:
  print("Você é MAIOR de idade ;)")
else:
  print("Você é MENOR de idade !!!")

# 14. Escreva um programa que solicite dois números ao usuário e exiba o maior deles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 == num2:
  print(f"Os números são iguais!!!")
elif num1 > num2:
  print(f"O maior número é: {num1}")
else:
  print(f"O maior número é: {num2}")

# 15. Crie um programa que peça um número inteiro e verifique se ele é divisível por 3 e por 5 ao mesmo tempo.

num = int(input("Digite um número inteiro: "))

div3 = num % 3 == 0
div5 = num % 5 == 0

if div3 == True and div5 == True:
  print("O número é divisível por 3 e 5")
else:
  print("O número NÃO é divisível por 3 e 5")
