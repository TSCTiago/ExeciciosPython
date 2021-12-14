'''Escreva um programa que lê um inteiro N e imprime os N primeiros inteiros negativos.'''
n = int(input('digite N: '))
for c in range(1,n + 1):
    print(c * (-1))