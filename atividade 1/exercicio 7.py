# Programa: cálculo de rendimento de táxi

# Entrada de dados
preco_combustivel = float(input("Digite o preço do combustível (R$/L): "))
km_inicio = float(input("Digite a marcação do odômetro no início do dia (Km): "))
km_fim = float(input("Digite a marcação do odômetro no final do dia (Km): "))
litros_gastos = float(input("Digite o número de litros de combustível gasto: "))
valor_recebido = float(input("Digite o valor total recebido dos passageiros (R$): "))

# Cálculos
km_percorridos = km_fim - km_inicio
media_consumo = km_percorridos / litros_gastos
gasto_combustivel = litros_gastos * preco_combustivel
lucro = valor_recebido - gasto_combustivel

# Saída de resultados
print("\n--- RELATÓRIO DO DIA ---")
print(f"Km percorridos: {km_percorridos:.2f} Km")
print(f"Média de consumo: {media_consumo:.2f} Km/L")
print(f"Gasto com combustível: R$ {gasto_combustivel:.2f}")
print(f"Lucro do dia: R$ {lucro:.2f}")
