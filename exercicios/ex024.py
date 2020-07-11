print('{:=^26}\n'.format(' Desafio 024 '))

cidade = str(input('Insira o nome de uma cidade: ')).strip()

santo = cidade.upper().split()
santo = santo[0]


print("A cidade {} tem SANTO no seu primeiro nome? {}".format(
    cidade, ('SANTO' in santo)))

print('{:=^26}\n'.format(' Desafio 024 '))
