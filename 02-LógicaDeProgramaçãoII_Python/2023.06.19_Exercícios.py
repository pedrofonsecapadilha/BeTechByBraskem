# Exercícios

# Exercício 01
    # Faça uma função que recebe um país e os anos que o país foi campeão do mundo, mostrar o nome do país e os anos dos títulos.

# Opção Pedro
def campeoes(**paises):
  data_base = { "Uruguai": 1930, "Itália": 1934, "Itália": 1938 }
  #data_base.update(paises)
  print(data_base)

campeoes(**{'Uruguai': 1950})
{'Uruguai': 1930, 'Itália': 1938}

# Opção Professor
def campeao(pais, *anos_campeao):
  print(f"País: {pais}")
  print("Campeão:", *anos_campeao[0])

campeao("Brasil", [1958, 1962, 1970, 1994, 2002])

# Exercício 02
    # Modifique a função anterior para incluir um parâmetro opcional indicando o caractere de separação entre as variáveis. Seu valor padrão será 1 espaço em branco.

def campeao(pais, *anos_campeao, sep=' '):
  print(f"País: {pais}")
  print("Campeão:", *anos_campeao[0], sep=sep)

campeao("Brasil", [1958, 1962, 1970, 1994, 2002], sep=" - ")