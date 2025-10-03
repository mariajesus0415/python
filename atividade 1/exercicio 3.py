# definir o resultado da soma dos quatro numeros
def calculaSoma(num1, num2, num3, num4):
   soma = (num1 + num2 + num3 + num4) - 10
   print(f"A soma dos 4 numeros é:", soma)

#pedir os numeros
num1 = int(input("Digite o primeiro valor inteiro: "))
num2 = int(input("Digite o segundo valor inteiro: "))
num3 = int(input("Digite o terceiro valor inteiro: "))
num4 = int(input("Digite o quarto valor inteiro: "))


#argumento
calculaSoma(num1, num2, num3, num4)