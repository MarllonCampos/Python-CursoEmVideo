print('{:=^26}\n'.format(' Desafio 026 '))

frase = str(input('Insira uma frase: '))
frase = frase.strip().upper()

letraA = frase.count('A')

posi = frase.find('A')

ultima = frase.rfind('A')


print(frase)
print('A letra "A" aparece {} vezes'.format(letraA))
print('A primeira posição que aparece a letra A é: {}'.format(posi))
print('A ultima posição que aparece a letra A é: {}'.format(ultima))


print('{:=^26}\n'.format(' Desafio 026 '))
