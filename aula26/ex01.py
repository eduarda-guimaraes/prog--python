# Exercício 1: Peça ao usuário um número e diga se ele é par ou ímpar.

print("Números pares e ímpares!")

num = int(input("Digite um número: "))

if num % 2 == 0:
    print(f"O número {num} é par!")
elif num < 0:
    print(f"O número {num} é negativo!")
else:
    print(f"O número {num} é ímpar!")