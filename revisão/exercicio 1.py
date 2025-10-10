def ApresentaJogadores(opçao):
    match opçao:
        case 1:
            print(f"jogador 1: Bento.")
        case 2:
            print(f"jogador 2: Vitin.")
        case 3:
            print(f"jogador 3: Gabriel.")
        case 4:
            print(f"jogador 4: Militão.")
        case 5:
            print(f"jogador 5: Casimiro.")
        case 6:
            print(f"jogador 6: Douglas Santos.")
        case 7:
            print(f"jogador 7: Vinicius Junior .")
        case 8:
            print(f"jogador 8: Bruno Guimarães.")
        case 9:
            print(f"jogador 9: Richarlison.")
        case 10:
            print(f"jogador 10: Rodrygo.")
        case 11:
            print(f"jogador 11: Paquetá.")
        case _:
            print(f"Jogador {opçao} não encontrado,")

def main():
    print("digite um numero de camisa de 1 até 11:")
    opcao = int(input())
    ApresentaJogadores(opcao)
if __name__ == '__main__':
    main()