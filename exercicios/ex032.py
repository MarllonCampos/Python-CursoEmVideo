from datetime import date
print('{:=^26}\n'.format(' Desafio 032 '))

ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year

if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    bis = 'Bissexto'
else:
    bis = 'Não é Bissexto'


print('O ano {} é {}'.format(ano, bis))


print('{:=^26}\n'.format(' Desafio 032 '))
