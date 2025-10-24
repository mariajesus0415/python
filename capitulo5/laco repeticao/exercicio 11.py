maior_altura = 0
menor_altura = 0
soma_mulheres = 0
qtd_mulheres = 0
qtd_homens = 0

for i in range(10):
    altura = float(input(f"Digite a altura da {i+1}ª pessoa (em metros): "))
    sexo = input("Digite o sexo (M/F): ").upper()

    if i == 0:
        maior_altura = menor_altura = altura
    else:
        if altura > maior_altura:
            maior_altura = altura
        if altura < menor_altura:
            menor_altura = altura

    if sexo == "F":
        soma_mulheres += altura
        qtd_mulheres += 1
    elif sexo == "M":
        qtd_homens += 1

print(f"\nMaior altura: {maior_altura:.2f} m")
print(f"Menor altura: {menor_altura:.2f} m")

if qtd_mulheres > 0:
    media_mulheres = soma_mulheres / qtd_mulheres
    print(f"Média de altura das mulheres: {media_mulheres:.2f} m")
else:
    print("Não há mulheres no grupo.")

print(f"Número de homens: {qtd_homens}")