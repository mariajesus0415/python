maior = 0;
menor = 0;

for i in range(0,4):
    numero = int(input("Digite um numero: "))

    if (i == 0):
        maior = numero
        menor = numero
    if(numero > maior):
        maior = numero
    elif (numero < menor):
        menor = numero

print(f"O maior numero é: {maior}"
print(f"O menor numero é: {menor}")
