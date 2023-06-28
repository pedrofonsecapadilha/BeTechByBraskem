# Exercícios

  # Exercício 01
  # Faça uma função que recebe um número exp. Ela deverá retornar uma função que recebe um número base e retorna base elevado a exp.

base = float(input("Digite o número que será a BASE: "))
exp = float(input("Digite o número que será o EXPONENCIAL: "))

exponencial = lambda x, y: x**y
print(exponencial(base, exp))

  # Exercício 02
  # Faça o bom e velho fatorial recursivo.

def fatorial_recursivo(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fatorial_recursivo(n-1)

fatorial_recursivo(5)