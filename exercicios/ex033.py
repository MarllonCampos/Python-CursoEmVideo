print('{:=^26}\n'.format(' Desafio 033 '))
n1 = int(input('Digite o  1º número: '))
n2 = int(input('Digite o  2º número: '))
n3 = int(input('Digite o  3º número: '))

maior = n1

# Verificar maior
if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3


print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))


print('{:=^26}\n'.format(' Desafio 033 '))
