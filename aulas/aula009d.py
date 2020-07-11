#Divisão de Strings
frase = 'Curso em Vídeo Python'


#Função split() por padrão divide a string em seus espaços
#Transformando onde foi separado em novas listas
print('Original era: {}'.format(frase))
print('Agora é: {} '.format(frase.split()))
print('\n')



#Junção de Strings

#Metodo join é utilizado para juntar strings
# '-'.join(frase) junta as diferentes listas separando por -
print('Original era: {}'.format(frase))
print('Com novas listas geradas fica: {}'.format(frase.split()))
print('Utilizando o metodo join fica: {}'.format('****'.join(frase.split())))
