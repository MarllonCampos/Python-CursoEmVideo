print('====== DESAFIO 08 ======')
metros = float(input('Insira o valor em metros: '))
kilo = metros / 1000
hect = metros / 100
dam = metros /10
dm = metros*10
cent = metros * 100
mili = metros * 1000

print('A medida de {:.2f}m corresponde a'.format(metros))
print('{}km'.format(kilo))
print('{}hm'.format(hect))
print('{}dam'.format(dam))
print('{}m'.format(metros))
print('{}dm'.format(dm))
print('{}cm'.format(cent))
print('{}mm'.format(mili))

