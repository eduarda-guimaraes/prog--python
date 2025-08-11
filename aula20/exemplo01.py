#Código em Python

nota_um = float(input('Digite a primeira nota: '))
nota_dois = float(input('Digite a segunda nota: '))
media = (nota_um+nota_dois)/2

# formatado com dois números após a vírgula
print(f"\nA média é {media:.2f}")
# não formatado
print("A média é", media,"\n")
#imprimir as notas na tela
print(f"Nota 1: {nota_um:.2f} \nNota 2: {nota_dois:.2f}\n")

if media >= 6:
    print("Você foi aprovado!\n")
elif media > 10 or media < 0:
    print("Número inválido!")
else:
    print("Você foi reprovado :(")