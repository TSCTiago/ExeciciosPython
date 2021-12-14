'''Escreva um programa que receba vários números, calcule e mostre:
a) a soma dos números digitados;
b) a quantidade de números digitado;
c) a média dos números digitados;

d) o maior número digitado;
e) o menor número digitado;
f) a média dos números pares.'''

num = int(input('Total de valores: '))
print()
n = []
par = []
for c in range(1,num + 1):
    c = int(input(f'Digite o {c} valor: '))
    n.append(c)
    if c % 2 == 0:
        par.append(c)
print()
print(f'A soma dos valores lidos é {sum(n)}')
print(f'A quantidade de números digitados é : {len(n)}')
print(f'A média dos números digitados é {sum(n) / num}')
print(f'O maior número digitado é {max(n)}')
print(f'O menor número digitado é {min(n)}')
print(F'A média dos números pares é {sum(par) / len(par)}')

