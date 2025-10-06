# Desafio 1: Peça ao usuário uma quantidade de alunos e, para cada um, o nome e duas notas. 
# Armazene em listas e exiba a média de cada aluno.

lNome = []
lNotas = []
lMedias = []

quant = int(input("Digite a quantidade de alunos: "))

for i in range(quant):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    lNome.append(nome)
    
    notas_aluno = []  # lista temporária para as notas do aluno
    for j in range(2):
        nota = float(input(f"Digite a {j+1}ª nota de {nome}: "))
        notas_aluno.append(nota)
    
    lNotas.append(notas_aluno)  # adiciona as notas desse aluno na lista geral
    media = sum(notas_aluno) / len(notas_aluno)  # calcula a média
    lMedias.append(media)

# Exibir resultados
for i in range(quant):
    print(f"Aluno: {lNome[i]} - Notas: {lNotas[i]} - Média: {lMedias[i]:.2f}")