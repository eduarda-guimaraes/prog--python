# Exercício 2: Leia a idade de uma pessoa e informe se ela é menor de idade, adulta ou idosa (>= 60).

print("Você é de menor, adulto ou idoso?")

idade=int(input("Digite sua idade: "))
if idade < 18 and idade >= 0:
    print("Você é menor de idade!")
elif idade >=60:
    print("Você idoso (a)!")
elif idade >=18 and idade < 60:
    print("Você é maior de idade!")
else:
    print("Idade inválida!")
