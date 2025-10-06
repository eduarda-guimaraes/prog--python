# Exercício 15: Peça uma lista de nomes e diga quantos começam com a letra 'M'.

import random
tamanhoLista = random.randint(1,10)
l = []
comecamM = 0

print("Uma lista de nomes!\n")
print("O tamanho da lista é",tamanhoLista)

for i in range(tamanhoLista):
    nome = input(f"Digite o {i+1}º nome: ")
    l.append(nome)
    if nome.startswith("M") or nome.startswith("m"):
        comecamM+=1
    i+1
print(comecamM,"nomes começam com letra M.")