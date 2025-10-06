# Exercício 11: Crie uma lista com 5 números digitados pelo usuário e imprima a lista.

l = []
print("Lista de números digitados!")
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    l.append(num)
print(*l) # * serve para tirar os [] da lista!