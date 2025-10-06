import time

print("Funções básicas!")
time.sleep(0.5)

print("\n------ Entrada e Saída de Informações ------")
nome=(input("\nDigite seu primeiro nome: "))
idade=(input("Digite sua idade: "))

print("Olá,",nome,end="!\n")
print("Você tem ",idade,"anos.")

print("\n------ Calculadora ------")
n1 = int(input("\nDigite um número: "))
n2 = int(input("Digite um segundo número: "))

print("\n| + | - |")
print("| : | x |")

op = (input("\nDigite a operação a ser utilizada: "))

match op:
    case '+':
        soma=n1+n2
        print("\nA soma de", n1,"+", n2,"é igual a", soma)
    case '-':
        subtracao=n1-n2
        print("\nA subtração de", n1,"-", n2,"é igual a", subtracao)
    case 'x':
        multiplicacao=n1*n2
        print("\nA multiplicação de", n1,"*", n2,"é igual a", multiplicacao)
    case ':':
        divisao=n1/n2
        print("\nA divisão de", n1,"/", n2,"é igual a", divisao)
    case _:
        print("\nNúmeros inválidos!")
