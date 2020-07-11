print('====== DESAFIO 15 ======')
dias = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos km foram rodados: '))
precoDia = dias * 60
precoKm = km * 0.15
precoTotal = precoDia + precoKm

print('O total a pagar é de R${:.2f}'.format(precoTotal))