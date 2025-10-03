def maiorNumero(numero1, numero2, numero3):
    if(numero1 > numero2):
        if(numero1 > numero3):
            print(f"O primeiro numero é o maior numero.")

    elif(numero2 > numero3):
        print(f"O segundo numero é o maior numero")
    else:
        print("O terceiro numero é o maior numero")

numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))
numero3 = int(input("digite o terceito numero: "))

maiorNumero(numero1, numero2, numero3)