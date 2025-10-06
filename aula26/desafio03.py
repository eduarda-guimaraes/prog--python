# Desafio 3: Peça ao usuário 10 números e exiba quais são primos.

def eh_primo(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

primos = []
print("Digite 10 números!\n")
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: ")) 
    
    if eh_primo(num):
        primos.append(num)

print("Números primos digitados:", primos)
