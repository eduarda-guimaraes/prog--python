# Exercício 10: Peça números ao usuário até que ele digite 0, e então exiba a média dos valores digitados.

num = []

print("Digite 0 para encerrar.")
i=0
numero=1
soma=0
media=0
cont=True

while cont:
    numero = float(input(f"Digite o {i+1}º número: "))
    if numero == 0:
        cont = False
    else:
        num.append(numero)
        i+=1
        soma+=numero


print(num)
media=soma/i
print("A média dos números é igual a",media)

