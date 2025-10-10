def verificaFeriado(mes, dia):
    match mes:
        case 9:
            match dia:
                case 7  :
                    print(f"dia {dia} e dia das crianças")
                case _:
                    print("este dia nao existe")
        case 10:
            match dia:
                case 12:
                    print(f"dia {dia} é dia das crianças")
                case _:
                    print("este dia nao existe")
        case _:
            print("esse mes nao existe")

def main():
    dia = int(input("digite o dia do mes"))
    mes = int(input("digite o mes"))



if __name__ == "__main__":
    main()
