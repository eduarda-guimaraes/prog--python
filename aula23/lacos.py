i = 1
while i < 6:
    print(i, end='|')
    i+=1

i = 0

print()

#For funciona com: valor inicial, final, e de quanto em quanto deve ser adicionado
for i in range(10):
    print(" ",i, end='')

print()

j = 100
for j in range (100, 0, -1): # Valor inicial: 100, valor final: 0, diminui a cada repetição: -1
    print(" ",j, end='')