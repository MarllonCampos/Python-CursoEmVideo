#Transformação

frase= "   Aprenda Python  "


#Função split remove espaços em brancos no começo e final da string pro exemplo:
#frase.strip()
print('Original era: {}'.format(frase))
print('Agora é: {}'.format(frase.strip()))
print('\n')


#Função rsplit parecida com a função strip
#Mas remove apenas os espaços em branco do lado direito
print('Original era: {}'.format(frase))
print('Agora é: {}'.format(frase.rstrip()))
print('\n')



#Função lsplit parecida com a função rstrip
#Mas remove apenas os espaços do lado esquerdo
print('Original era: {}'.format(frase))
print('Agora é: {}'.format(frase.lstrip()))


