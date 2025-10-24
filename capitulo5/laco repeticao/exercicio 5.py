contador = 0

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    if num % 3 == 0:
        contador += 1

print(f"\nQuantidade de números divisíveis por 3: {contador}")