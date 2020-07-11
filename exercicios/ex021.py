from pygame import mixer

print('{:=^26}\n'.format(' Desafio 021 '))

mixer.init()
mixer.music.load('turn4what.mp3')
mixer.music.play()
input('Pressione qualquer tecla para parar de tocar...')

print('\n{:=^26}'.format(' Desafio 021 '))
