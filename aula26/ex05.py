# Exercício 5: Peça um número inteiro e verifique se ele é positivo, negativo ou zero.

print("O número é positivo, negativo ou zero?")
num=int(input("Digite um número inteiro: "))
if num == 0:
    print("O número é zero.")
elif num > 0:
    print(f"O número {num} é positivo!")
else:
    print(f"O número {num} é negativo.")