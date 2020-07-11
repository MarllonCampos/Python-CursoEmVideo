print('{:=^26}\n'.format(' Desafio 031 '))
dist = int(input('Qual a distancia da sua viagem: '))
if dist > 200:
    preco = float(dist * 0.45)
    print('O preço da sua viagem será de {:.2f}'.format(preco))
else:
    preco = float(dist * 0.50)
    print('O preço da sua viagem será de R${:.2f}'.format(preco))

print('{:=^26}\n'.format(' Desafio 031 '))
