preco_combustivel = int(input("Digite o preço do combustível por litro (R$): "))
km_inicio = int(input("Digite a marcação do odômetro no início do dia (Km): "))
km_fim =  int(input("Digite a marcação do odômetro no final do dia (Km): "))
litros_gastos = int(input("Digite a quantidade de litros de combustível gasto: "))
valor_recebido = int(input("Digite o valor total recebido dos passageiros (R$): "))


def calculoConsumo(preco_combustivel, km_inicio, km_fim, litros_gastos, valor_recebido):
    soma_consumo = litros_gastos * (km_inicio / km_fim) * preco_combustivel
    print(f"esse foi o lucro do seu dia:", soma_consumo)


calculoConsumo(preco_combustivel, km_inicio, km_fim, litros_gastos, valor_recebido)


