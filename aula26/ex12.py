# Exercício 12: Some todos os elementos de uma lista.

import random

l = []
aleatorio = random.randint(1,10)
print("Soma de números em uma lista!")
n = int(input("Qual vai ser o tamanho da lista? "))
if n < 0:
    print("Valor inválido! Atribuindo um valor automático à lista...")
    n = aleatorio
print(f"A lista vai se repetir {n} vezes.")

for i in range (n):
    soma = float(input(f"Digite o {i+1}º número: "))
    l.append(soma)

print(f"Valores atribuidos à lista: {l}")
soma = sum(l)
print(f"A soma dos valores da lista é igual a: {soma}.")