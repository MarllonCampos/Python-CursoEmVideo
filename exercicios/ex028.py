from random import randint as ri

print('{:=^26}\n'.format(' Desafio 028 '))

aleat = ri(0, 5)
num = int(input('Insira um número: '))

if num == aleat:
    print('Parabéns você acertou o número')
else:
    print('Você errou o número tente novamente!')
    print('O número era: {}'.format(aleat))


print('\n{:=^26}\n'.format(' Desafio 028 '))
