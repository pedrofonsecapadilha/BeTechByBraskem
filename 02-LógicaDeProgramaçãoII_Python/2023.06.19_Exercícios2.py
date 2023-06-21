# Exercícios

# Exercício 01
    # O programa abaixo apresenta alguns erros de execução. Sem alterar as estruturas de dados originais (lista e dicionário), faça um tratamento adequado dos erros para exibir as médias corretas de cada aluno ou mensagens de erro significativas para o usuário em português, sem permitir que o programa seja interrompido antes de finalizar sua execução.

    # alunos = ['John', 'Paul', 'George', 'Ringo', 'Brian', 'Pete']

    # notas = {
    #     'John':[7.5, 9.0, 8.25, 8.0],
    #     'Paul':[9.0, 8.5, '10.0', 8.5],
    #     'George':[6.0, '7.0', 8.0, 9],
    #     'Ringo':[4.5, 4.0, 6.0, 7.0],
    #     'Pete':[]
    # }

    # for aluno in alunos:
    #     media = sum(notas[aluno])/len(notas[aluno])
    #     print(f'{aluno}:\t{media}')

alunos = ['John', 'Paul', 'George', 'Ringo', 'Brian', 'Pete']

notas = {
    'John':[7.5, 9.0, 8.25, 8.0],
    'Paul':[9.0, 8.5, '10.0', 8.5],
    'George':[6.0, '7.0', 8.0, 9],
    'Ringo':[4.5, 4.0, 6.0, 7.0],
    'Pete':[]
}

for aluno in alunos:
    try:
      media = sum(notas[aluno])/len(notas[aluno])
      print(f'{aluno}:\t{media}')
    except TypeError:
      print(f"Aluno {aluno} com nota em formato errado.")
    except KeyError:
      print(f"Aluno {aluno} não está no banco de dados de notas.")
    except ZeroDivisionError:
      print(f"Aluno {aluno} não tem notas cadastradas.")