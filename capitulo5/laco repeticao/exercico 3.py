# Programa para imprimir os números ímpares entre 1 e 30

for i in range(1, 31):  # percorre de 1 até 30 (31 não é incluído)
    if i % 2 != 0:      # verifica se o número é ímpar
        print(i)