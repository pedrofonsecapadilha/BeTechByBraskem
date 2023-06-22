# Exercícios

# Parte 1 - arquivos de texto simples
# Nesta etapa, não utilize as bibliotecas csv nem json.

# Exercício 01
    # Escreva um programa que lê um arquivo de texto contendo uma série de números separados por quebra de linha ('\n') e os adiciona a uma lista. Imprima a lista na tela.

arquivo = open('Ex1.txt', 'w')
arquivo.write("456\n321\n789\n555\n468\n7")
arquivo.close()

arquivo = open('Ex1.txt', 'r')
conteudo = arquivo.read()
print(conteudo.split('\n'))
arquivo.close()

# Exercício 02
    # Escreva um programa que lê um arquivo de texto contendo uma série de números separados por quebra de linha (\n) e escreva na tela o somatório dos números.

arquivo = open('Ex2.txt', 'w')
arquivo.write("456\n321\n789\n555\n468\n7\n19")
arquivo.close()

arquivo = open('Ex2.txt', 'r')
conteudo = arquivo.read()
result = conteudo.split('\n')
soma = 0
for e in result:
  soma += int(e)
print(soma)
arquivo.close()

# Exercício 03
    # Escreva um programa que lê um arquivo de texto contendo uma série de números separados por quebra de linha (\n). Crie um novo arquivo onde você irá escrever "primo" ou "não-primo" na linha correspondente a cada número.
    # Lembrete: um número primo é divisível apenas por 1 e por ele mesmo.

arquivo_data = open('Ex3.txt', 'w')
arquivo_data.write("456\n321\n789\n7\n19")
arquivo_data.close()

arquivo = open('Ex3.txt', 'r')
conteudo = list(map(int, arquivo.read().split('\n')))
arquivo.close()

arquivo_resp = open('Ex3_Resp.txt', 'w')
result = ""
for e in conteudo:
  check = 0
  for num in range(1, e+1):
    if e % num == 0:
      check += 1
  if check == 2:
    result += "primo\n"
  else:
    result += "não-primo\n"
arquivo_resp.write(result)
arquivo_resp.close()

# Parte 2
# Use o módulo csv recém-estudado para fazer os próximos exercícios.

# Exercício 04
    # Faça um programa que pede para o usuário digitar a quantidade de provas aplicadas, a quantidade de alunos em uma turma e cada uma das notas. O seu programa deverá salvar as notas digitadas em um arquivo CSV onde cada linha representa um aluno e cada coluna representa uma prova.

qtd_alunos = float(input("Qual o número de estudantes? "))
qtd_provas = float(input("Quantas provas foram aplicadas? "))

dados = []
for al in range(1, qtd_alunos+1):
  notas_al = []
  for nota in range(1, qtd_provas+1):
    notas_al.append(float(input(f"Aluno {al} - Digite quanto tirou na prova {nota}: ")))
  dados.append(notas_al)

import csv

arquivo = open('Ex4.csv', 'w')
escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')
escritor.writerows(dados)
arquivo.close()

# Exercício 05
    # Faça um programa que carrega um arquivo CSV de notas (como o gerado pelo exercício anterior) e pede para o usuário digitar a nota mínima para aprovação. Ele deverá gerar um novo arquivo contendo as notas originais e 2 colunas adicionais: a média de cada aluno na primeira (com, no máximo, 2 casas decimais) e "APR" ou "REP" na segunda, indicando se a média atingiu o valor mínimo ou não.

import csv

arquivo = open('Ex4.csv', 'r')
planilha = csv.reader(arquivo, delimiter=',', lineterminator='\n')
data = []
for linha in planilha:
  dados_linha = []
  for e in linha:
    dados_linha.append(float(e))
  data.append(dados_linha)
arquivo.close()

nota_min = float(input("Digite o valor de nota mínima para aprovação: "))

for e in data:
  e.append(round(sum(e)/len(e), 2))

for e in data:
  if e[-1] >= nota_min:
    e.append("APR")
  else:
    e.append("REP")

arquivo = open('Ex5.csv', 'w')
escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')
escritor.writerows(data)
arquivo.close()