'''Escreva um programa que lê um inteiro N e imprime a soma dos N primeiros números inteiros.'''
n = int(input('digite N: '))
soma = 0
for c in range(1,n+1):
    soma = soma + c
print(f'A soma dos {n} primeiros inteiros é {soma}')