n1 = int(input("Digite um número: "))
n2 = int(input("Digite um segundo número: "))
print("\n[ Selecione uma operação ]")
print("\n| + | - |")
op = input("| * | / |\n\n")

match op:
    case '+':
        soma=n1+n2
        print("\nA soma de", n1,"+", n2,"é igual a", soma)
    case '-':
        subtracao=n1-n2
        print("\nA subtração de", n1,"-", n2,"é igual a", subtracao)
    case '*':
        multiplicacao=n1*n2
        print("\nA multiplicação de", n1,"*", n2,"é igual a", multiplicacao)
    case '/':
        divisao=n1/n2
        print("\nA divisão de", n1,"/", n2,"é igual a", divisao)
    case _:
        print("\nNúmeros inválidos!")

