print('{:=^26}\n'.format(' Desafio 022 '))

nome = str(input('Digite o seu nome completo: ')).strip()


print(nome.upper())

print(nome.lower())

print('Seu nome ao todo tem {} letras'.format(len(''.join(nome.split()))))


print('O seu primeiro nome é {} e ele tem {} letras'.format(
    nome.split()[0], len(nome.split()[0])))


print('\n{:=^26}\n'.format(' Desafio 022 '))
