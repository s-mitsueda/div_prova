"""
Elabore um programa que leia um número que o usuário digitar.
Dependendo do número informado, das frases abaixo,
o sistema imprimirá somente as que forem verdadeiras.
    O número é menor que 10.
    O número é par.
    O número está entre 8 e 16.
    O número é 51 ou 80.
"""

n = int(input())

if n < 10:
    print("O número é menor que 10.")
if (n % 2) == 0:
    print("O número é par.")
if (n > 8 and
    n < 16):
    print("O número está entre 8 e 16.")
if (n == 51 or
    n == 80):
    print("O número é 51 ou 80.")
