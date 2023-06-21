# Exercícios
# Dica de estudo: mesmo que você conheça ou prefira outras soluções, tente explorar ao máximo técnicas como slicing, unpacking, zip e enumerate.

# Exercício 1
    # Faça um programa que leia as coordenadas de dois vetores a partir do teclado e armazene-as em listas. Exemplo:
    # vetor1 = [1, 4, 7]
    # vetor2 = [2, 3, 4]
    # O seu programa deverá realizar a soma vetorial. No exemplo acima, ela é dada por:

    # soma = [1+2, 4+3, 7+4] = [3, 7, 11]

    # Dica: note que os valores a serem somados entre si possuem o mesmo índice em listas diferentes.

quantidade = int(input("Digite a quantidade de valores dos vetores: "))

vetor1 = [int(input(f"Digite o {num+1} valor do primeiro vetor: ")) for num in range(quantidade)]
vetor2 = [int(input(f"Digite o {num+1} valor do segundo vetor: ")) for num in range(quantidade)]

vetor_result = [vetor1 + vetor2 for vetor1, vetor2 in zip(vetor1, vetor2)]

print(vetor_result)

# Exercício 2
    # Um polinômio é uma expressão matemática formada pela soma de diversos termos. Cada termo é o produto de uma constante conhecida e uma incógnita (tipicamente elevada a diferentes expoentes). Por exemplo:
    # y = 2x³ - 5x² + 3x + 4

    # Podemos representar computacionalmente um polinômio usando uma lista ou tupla. Salvamos os coeficientes na posição cujo índice represente o expoente do x. O polinômio do exemplo acima ficaria:

    # coeficientes = (4, 3, -5, 2)

    # Note que o número "livre" é considerado um produto de x elevado a 0. Caso algum expoente esteja ausente, considere seu coeficiente como 0. Exemplo:

    # y = 6x² - 2

    # O termo com expoente 1 está ausente, logo:

    # coeficientes = (-2, 0, 6)

    # Faça uma função que recebe dois parâmetros: uma coleção de coeficientes e um valor de x, e retorna o valor do polinômio para o valor de x dado.

quantidade = int(input(f"Qual será o tamanho do polinômio? "))
coeficientes = [float(input(f"Digite o coeficiente {num+1}: ")) for num in range(quantidade)]
x = float(input(f"Qual será o valor de X? "))
y = 0

for i, e in enumerate(coeficientes):
  y = y + e * x ** i

print(y)

# Exercício 3
    # Faça uma função que recebe como parâmetro um número indicando a quantidade de provas que um aluno fez.
    # A função deverá pedir para o usuário digitar todas as suas notas e retornar uma tupla contendo todas as notas na ordem em que foram digitadas.

    # Faça uma função que recebe como parâmetros uma coleção (lista ou tupla) de notas.

    # O programa deverá retornar uma tupla nova contendo todas as notas antigas, e, na última posição, a média das notas.

qtdade = int(input(f"Quantas provas você realizou? "))
notas = [float(input(f"Digite a nota da prova {num+1}: ")) for num in range(qtdade)]
media = sum(notas) / len(notas)
notas.append(media)
print(tuple(notas))