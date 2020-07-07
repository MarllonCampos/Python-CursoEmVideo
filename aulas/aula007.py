# Operadores aritméticos
# + = soma
# - = subtração
# * = multiplicação
# / = divisão
# ** = potência
# // = divisão inteira
# % = modulo (resto da divisão)
#
# Ordem de precedencia:
#   Parenteses
#   **
#   * / // % (Quem aparecer primeiro da esquerda para a direita)
#   + -

print('Operadores aritméticos')
print('5 + 2 = ', 5 + 2)
print('5 - 2 = ', 5 - 2)
print('5 * 2 = ', 5 * 2)
print('5 / 2 = ', 5 / 2)
print('5 ** 2 = ', 5 ** 2)
print('5 // 2 = ', 5 // 2)
print('5 % 2 = ', 5 % 2)



# Oi * 5 executa o Oi 5 vezes ficando:
#   Oi
#   Oi
#   Oi
#   Oi


#Se colocar {:20} A string que será escrita no terminal será escrito em 20 espaços e alinhado a esquerda
#Se colocar {:>20} A string que sera escrita no terminal será escrito em 20 espaços e alinhado a direita
#Se colocar {:^20} A string que será escreita no terminal será escrita em 20 espaços e alinhado ao centro
#Se colocar {:=>20} Qualquer caractere antes do alinhamento esse caractere se repetira quantidade x de vezes para alinhar de forma desejada


n1 = int(input('\n\nUm valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, O produto é {} e a divisão {:.3f}'.format(s,m,d), end=" ==\==\n")
print('Divisão inteira {} e potência {}'.format(di,e))