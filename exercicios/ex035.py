print('{:=^26}\n'.format(' Desafio 035 '))
ladoa = float(input('Primeiro segmento:'))
ladob = float(input('Segundo segmento:'))
ladoc = float(input('Terceiro segmento:'))

if ladoa < ladob + ladoc and ladob < ladoa + ladoc and ladoc < ladoa + ladob:
    triangulo = "podem formar um triângulo"
else:
    triangulo = "não podem formar um triângulo"



print('Os segmentos {}'.format(triangulo))


print('{:=^26}\n'.format(' Desafio 035 '))
