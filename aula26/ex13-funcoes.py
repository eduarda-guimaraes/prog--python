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
    i+1

print("")
print("Lista:",*l)
print("O maior número da lista é",max(l)) # utilização da função pronta max()
print("O menor número da lista é",min(l)) # utilização da função pronta min()
    