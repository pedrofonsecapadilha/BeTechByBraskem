# Exercício 1
'''
    Você deverá fazer uma calculadora que funcione da seguinte forma:

    - Você ou o usuário informa qual operação ela deverá fazer;
    - Informa quais são os numeros que serão envolvidos na operação;
    - Ela retorna o resultado da operação.

    - As operações que essa calculadora deverá fazer são: adição, subtração, multiplicação, divisão e média dos valores

    - A calculadora deverá poder ser chamada pela função `calculadora()`. Podendo receber parâmetros ou não.
    - cada operação deverá ter sua propria função.
    - deve ser usado o type hint e docstring

    Faça o exercício em duas etapas:
    - primeiro apenas para 2 numeros;
    - depois ele deverá **receber mais numeros** e conseguir calcular o somatório, produtório e a média de n numeros. No caso de subtração e divisão, ela deve validar que só terão 2 numeros
'''
# PRIMEIRA PARTE
def calculadora():
  operacao = input("Digite a operação que será realizada [+, -, *, /, media]: ")
  num_1 = float(input("Digite o primeiro número da conta: "))
  num_2 = float(input("Digite o segundo número da conta: "))

  if operacao == "+":
    return print(f"O resultado da conta é: {(num_1 + num_2)}")
  elif operacao == "-":
    return print(f"O resultado da conta é: {(num_1 - num_2)}")
  elif operacao == "*":
    return print(f"O resultado da conta é: {(num_1 * num_2)}")
  elif operacao == "/":
    return print(f"O resultado da conta é: {(num_1 / num_2)}")
  elif operacao == "media":
    return print(f"O resultado da conta é: {(num_1 + num_2) / 2}")

calculadora()

# SEGUNDA PARTE
def calculadora():
  operacao = input("Digite a operação que será realizada [+, -, *, /, media]: ")
  numeros = eval('[' + input("Digite os números para realizar a operação [separá-los por vígulas]: ") + ']')

  if operacao == "+":
    soma = 0
    for e in numeros:
      soma += e
    return print(f"O resultado da conta é: {(soma)}")
  elif operacao == "*":
    mult = 1
    for e in numeros:
      mult *= e
    return print(f"O resultado da conta é: {(mult)}")
  elif operacao == "media":
    soma = 0
    for e in numeros:
      soma += e
    return print(f"O resultado da conta é: {(soma) / len(numeros)}")
  elif operacao == "-":
    if len(numeros) != 2:
      raise Exception("Essa operação é válida apenas para 2 números!")
    else:
      return print(f"O resultado da conta é: {(numeros[0] - numeros[1])}")
  elif operacao == "/":
    if len(numeros) != 2:
      raise Exception("Essa operação é válida apenas para 2 números!")
    else:
      if numeros[1] == 0:
        raise Exception("Não é possível fazer uma divisão por 0")
      else:
        return print(f"O resultado da conta é: {(numeros[0] / numeros[1])}")

calculadora()
