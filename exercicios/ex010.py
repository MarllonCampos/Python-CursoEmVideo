print('====== DESAFIO 10 ======')
reais = float(input('Insira o dinheiro contido sua carteira? R$'))
dol = reais / 5.35
dolAust = reais / 3.73
dolCan = reais / 3.95
dolNew = reais / 3.49
euro = reais / 6.05
bit = reais / 49462.11
iene = reais * 20.04


print('Com R$ {:.2f} você consegue comprar U${:.2f} Dolares Americanos'.format(reais, dol))

print('Com R${:.2f} você consegue comprar A${:.2f} Dolares Australianos'.format(reais,dolAust))

print('Com R${:.2f} você consegue comprar C${:.2f} Dolares Canadenses'.format(reais,dolCan))

print('Com R${:.2f} você consegue comprar ${:.2f} Dolares Neozelandês'.format(reais,dolNew))

print('Com R${:.2f} você consegue comprar €{:.2f} Euros'.format(reais,euro))

print('Com R${:.2f} você consegue comprar ₿{:.6f} Bitcoins'.format(reais,bit))

print('Com R${:.2f} você consegue comprar ‎¥{:.2f} Ienes'.format(reais,iene))

