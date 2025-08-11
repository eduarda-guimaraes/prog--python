ano = float(input("Digite o ano: "))

if ano % 4 == 0:
    print("O ano é bissexto!")
elif ano % 100 == 0:
    if ano % 400 == 0:
        print("O ano é bissexto!")
    else:
        print("O ano NÃO é bissexto...")
else:
    print("O ano NÃO é bissexto...")