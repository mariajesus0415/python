def tabuada (numero):
    for i in range(0,11):
      print(f"{numero}*{i} = {(numero * i)}")

def main():
    numero =  int(input("Digite um numero"))
    tabuada(numero)

if __name__ == "__main__":
 main()