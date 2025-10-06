# Desafio 2: Gere uma lista com os números de 1 a 20, mas apenas os múltiplos de 3.

l = []

for i in range (20):
    if i % 3 == 0:
        l.append(i)

print("Números múltiplos de 3, de 1 até 20: ",*l)
