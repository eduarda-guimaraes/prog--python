l = []
l = [1,2,3,4,5]
print(l)

i = 0
print("Usando while:")
while i <= len(l):
    print(i,end='')
    i+=1

print("Usando for:")

for i in l:
    print(i, end = "")


print("\nAdicionando um valor à lista:")
l.append(10)
print(l)

a = [5, 6, 7, 8]
# l.append(a)
# print(l)
l.extend(a)
print(l)