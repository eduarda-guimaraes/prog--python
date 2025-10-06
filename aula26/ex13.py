# Exercício 13: Encontre o maior e o menor valor de uma lista.

import random
aleatorioLista = random.randint(1,10)
l = []
num=0

tamanho = int(input("Qual é o tamanho de sua lista? Digite: "))
if tamanho < 0 or tamanho > 10:
    tamanho = aleatorioLista

for i in range (tamanho):
    num=float(input(f"Digite o {i+1}º número: "))
    l.append(num)
    if i == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    i+1

print("")
print("Lista:",*l)
print("O maior número da lista é",maior)
print("O menor número da lista é",menor)
    