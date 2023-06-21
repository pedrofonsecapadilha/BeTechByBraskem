# Exercícios

# Exercício 01
    # Faça uma função que recebe uma lista de números e retorna uma lista contendo os cubos dos números pares.

# numeros = [1, 9, 4, 7, 6, 2]
qtd = int(input(f"Quantos números você quer digitar? "))
numeros = [float(input(f"Digite o número {num+1}: ")) for num in range(qtd)]
cubo_pares = [n**3 for n in numeros if n % 2 == 0]
print(cubo_pares)

# Exerciício 02
    # Faça uma função que recebe uma lista de números e retorna uma lista contendo os cubos dos números positivos e o quadrado dos números negativos.

# numeros = [-1, 9, -4, 7, -6, 2]
qtd = int(input(f"Quantos números você quer digitar? "))
numeros = [float(input(f"Digite o número {num+1}: ")) for num in range(qtd)]
resultado = [n**3 if n > 0 else n**2 for n in numeros]
print(resultado)

# Exercício 03
    # Faça uma função que recebe uma lista de nomes, uma lista de médias e a nota mínima para aprovação. Ela deverá retornar uma lista com os nomes dos alunos reprovados.

alunos = ["Pedro", "Amanda", "Lara"]
medias = [7.5, 5.0, 9.9]
apr = 6
reprovados = [alunos[i] for i in range(len(alunos)) if medias[i] < apr]
print(reprovados)

# Exercício 04
    # Faça uma função que recebe uma lista de nomes, uma lista de médias e a nota mínima para aprovação. Ela deverá retornar um dicionário contendo os nomes dos alunos e "APR" ou "REP" indicando a situação de cada um deles.

alunos = ["Pedro", "Amanda", "Lara"]
medias = [7.5, 5.0, 9.9]
apr = 6
situacao = {alunos:'APR' if medias >= apr else 'REP' for alunos, medias in zip(alunos, medias)}
print(situacao)