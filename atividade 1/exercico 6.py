primeira = int(input("qual e a primeira nota"))
segunda = int(input("qual e a segunda nota"))
bimestral = int(input("qual e a nota da bimestral"))

def mediaBimestral(primeira, segunda, bimestral):
    mediaFormativas = (primeira + segunda) / 2
    notaBimestral = bimestral
    total = (mediaFormativas * 0.3) + (notaBimestral * 0.7)
    print(f"a media bimestral será de:", total)


mediaBimestral(primeira, segunda, bimestral)