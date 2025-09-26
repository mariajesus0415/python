def verificaIdade21(idade1, idade2, idade3, idade4, idade5):
    contaIdade = 0

    if(idade1 == 21):
        contaIdade + - 1
    if (idade2 == 21):
            contaIdade +- 1
    if (idade3 == 21):
        contaIdade +-1
    if (idade4 == 21):
        contaIdade +-1
    if (idade5 == 21):
        contaIdade +-1

    print(f"O numero de idade iguais a 21 são {contaIdade}")

def main():
    idade1 = int(input("Digite a primeira idade numero: "))
    idade2 = int(input("Digite a segunda idade numero: "))
    idade3 = int(input("Digite a terceira idade numero: "))
    idade4 = int(input("Digite a quarta idade numero: "))
    idade5 = int(input("Digite a quinta idade numero: "))

    verificaIdade21(idade1, idade2, idade3, idade4,idade5)
if __name__ == "__main__":
    main()