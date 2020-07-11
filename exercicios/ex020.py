from random import sample

print('{:=^26}\n'.format(' Desafio 020 '))

a1 = str(input('1º aluno: '))
a2 = str(input('2º aluno: '))
a3 = str(input('3º aluno: '))
a4 = str(input('4º aluno: '))
nomes = sample([a1, a2, a3, a4], 4)

print('A ordem embaralhada ficará {}'.format(nomes))


print('\n{:=^26}'.format(' Desafio 020 '))
