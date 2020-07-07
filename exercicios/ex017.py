from math import hypot

print('{:=^26}'.format(' Desafio 017 '))
print('\n')

co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))

hip = hypot(co, ca)

print('O comprimento da hipotenusa é {:.2f}'.format(hip))

print('\n')

print('{:=^26}'.format(' Desafio 017 '))
