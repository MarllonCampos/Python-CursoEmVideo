print('{:=^26}\n'.format(' Desafio 023 '))

numero = str(input('Digite um número de 0 a 9999: '))

unidade = numero[::-1]

dezena = unidade[1:2]

centena = unidade[2:3]

milhar = unidade[3:4]

unidade = unidade[0:1]


print(""" 
    Unidade = {:4}
    Dezena = {:4}
    Centena = {:4}
    Milhar = {:4}
""".format(unidade, dezena, centena, milhar))


print('{:=^26}\n'.format(' Desafio 023 '))
