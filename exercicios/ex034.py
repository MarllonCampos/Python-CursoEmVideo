print('{:=^26}\n'.format(' Desafio 034 '))
sal = float(input('Qual é o salario do funcionário? R$'))

if sal > 1250:
    novoSal = sal * 1.1
else:
    novoSal = sal * 1.15

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(
    sal, novoSal))
print('{:=^26}\n'.format(' Desafio 034 '))
