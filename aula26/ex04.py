# Exercício 4: Solicite o nome de uma pessoa e diga se ele começa com a letra 'A'.

print("Seu nome começa com A?")

nome=input("Digite seu nome: ")
if nome.startswith("A") or nome.startswith("a"):
    print('Sim! Seu nome começa com "A".')
else:
    print('Não! Seu nome não começa com "A".')