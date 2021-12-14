'''Escreva um programa que lê um inteiro N e uma seqüência de N números inteiros, e imprime a soma dos números pares da
seqüência lida.'''

soma = 0
n = int(input('Quantos números deseja ler? '))
for valores in range(1,n+1):
    valores = int(input(f'digite o {valores}º valor: '))
    if valores % 2 == 0:
        soma += valores
print(f'Soma dos Pares {soma}')