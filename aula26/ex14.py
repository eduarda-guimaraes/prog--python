# Exercício 14: Conte quantos números pares existem em uma lista.

import random
l = []
pares=0

print("Números atribuídos aleatoriamente!")
for i in range(10):
    aleatorio = random.randint(1,100)
    l.append(aleatorio)
    if aleatorio % 2 == 0:
        pares+=1
    i+1

print("Lista:",*l)
print()
print(f"Há {pares} números pares na lista.")