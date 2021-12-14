'''Escreva um programa que imprima os N primeiros números naturais ímpares.'''
n = int(input('Digite quantos naturais impáres deseja ver: '))
for c in range(1,n+1):
    if c % 2 == 1:
        print(c)