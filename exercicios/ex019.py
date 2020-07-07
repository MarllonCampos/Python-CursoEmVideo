from random import choice

print('{:=^26}'.format(' Desafio 019 '))
print('\n')
a1 = str(input('Digite o nome do aluno: '))
a2 = str(input('Digite o nome do aluno: '))
a3 = str(input('Digite o nome do aluno: '))
a4 = str(input('Digite o nome do aluno: '))

alunos = [a1, a2, a3, a4]
alunoEscolhido = choice(alunos)

print('\nO aluno selecionado foi {}\n'.format(alunoEscolhido))


print('{:=^26}'.format(' Desafio 019 '))
