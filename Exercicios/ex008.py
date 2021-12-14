'''Escreva um programa que leia uma seqüência de números inteiros terminada por –1 e imprima na tela a soma e a média
aritmética destes números.
Obs: o valor –1 é somente um terminador e não deve ser considerado nos cálculos.'''
n = 0
soma = 0
media = 0
valores = []
while n != -1:
    n = int(input('digite um número: '))
    valores.append(n) 
valores.remove(-1)
print(f'A soma dos valores digitados é {sum(valores)}')
print(f'A média dos valores digitados é {(sum(valores))/(len(valores))}')

