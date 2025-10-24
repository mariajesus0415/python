mais_gordo = ""
mais_magro = ""
peso_maior = 0
peso_menor = 0

for i in range(5):
    nome = input("Nome: ")
    peso = float(input("Peso: "))

    if i == 0:
        mais_gordo = mais_magro = nome
        peso_maior = peso_menor = peso
    else:
        if peso > peso_maior:
            mais_gordo = nome
            peso_maior = peso
        if peso < peso_menor:
            mais_magro = nome
            peso_menor = peso

print(f"Mais gordo: {mais_gordo} ({peso_maior} kg)")
print(f"Mais magro: {mais_magro} ({peso_menor} kg)")