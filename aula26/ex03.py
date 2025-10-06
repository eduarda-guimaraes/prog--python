# Exercício 3: Peça duas notas e calcule a média. Diga se o aluno está aprovado (média >= 7).

print("Notas e sua média!")

nota1=float(input("Digite sua 1ª nota: "))
nota2=float(input("Digite sua 2ª nota: "))
media=(nota1+nota2)/2
print(f"A média das notas {nota1}, {nota2} é {media}")

if media >= 7:
    print("Você está aprovado (a)!")
elif media < 0 or media > 10:
    print("A média é inválida.")
else:
    print("Você NÃO está aprovado (a) :(")