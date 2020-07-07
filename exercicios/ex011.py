print('====== DESAFIO 10 ======')
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
litros = area / 2

print('A area de uma parede com {:.2f} de largura e {:.2f} de altura é de {:.2f}m²'.format(larg,alt,area))
print('Serão necessários {:.2f}L de tinta para pintar a parede por completo'.format(litros))
