from math import cos, sin, tan, radians

print('{:=^26}'.format(' Desafio 018 '))
print('\n')

ang = float(input('Insira o valor de um angulo: '))

cosseno = cos(radians(ang))
seno = sin(radians(ang))
tangente = tan(radians(ang))


print('\nO seno do angulo {:.2f} é {:.2f}'.format(ang, seno))
print('O cosseno do angulo {:.2f} é {:.2f}'.format(ang, cosseno))
print('A tangente do angulo {:.2f} é {:.2f}'.format(ang, tangente))
print('\n')

print('{:=^26}'.format(' Desafio 018 '))
