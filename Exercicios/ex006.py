'''Escreva um programa que lê um número não determinados de valores a, todos inteiros e positivos, um de cada vez, e
calcule e escreva a média aritmética dos valores lidos, a quantidade de valores pares, a quantidade de valores ímpares, a
percentagem de valores pares e a percentagem de valores ímpares.'''

num = int(input('Total de valores: '))
soma = 0
media  = 0
vp = 0
vi = 0
ppar = 0
pimpar = 0
for c in range(1,num + 1):
    c = int(input(f'Digite o {c}º valor: '))
    soma += c
    if c % 2 == 0:
        vp += 1
    elif c % 2 == 1:
        vi +=1

print(f'A média aritmética entre os calores lidos é: {soma / num}')
print(f'A quantidade de Pares: {vp}')
print(f'A quantidade de Impares: {vi}')
print(f'A porcentagem de valore pares é {(vp / num)*100} %')
print(f'A porcentagem de valore impares é {(vi / num)*100} %')