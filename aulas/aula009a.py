#Análise de Strings

frase = "Curso em Vídeo Python"

#Metódo len é pra metir a quantiade de espaços que existe na lista
print(len(frase))
print('\n')



#Método.count('LETRA') é utilizado para contar a ocorrencia da letra
print(frase.count('o'))
print('\n')



#Para implementar ainda mais .count('LETRA',0,13) da para contar fatiando a string, ou seja
#Contar a partir de 0 até 13 a quantidade de o
print(frase.count('o',0,13))
print('\n')



#Método.find('caracteres') Retorna onde começa a ocorrencia da primeira letra de caracteres
print('Apareceu a primeira ocorrencia de "deo" na posição {}'.format(frase.find('deo')))
print('\n')




#Se o método find não encontrar a string passada significa que não existe na seguinte string
print("""Apareceu a primeira ocorrencia de "Android" na posição {}"""
.format(frase.find('Android')))


#Operador in 'String' in variavel
print('Existe Curso em {} :  {}'.format(frase,('Curso' in frase)))