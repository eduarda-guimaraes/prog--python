# Exercício 9: Peça 5 números ao usuário e diga qual é o maior.

print("Qual é o número maior?")

num = []

for i in range (5):
    numero=int(input(f"Digite o {i+1}º número inteiro: "))
    num.append(numero)
maior= max(num)
print(f"\nO maior número digitado é {maior}.")