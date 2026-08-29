lista = []
kysymys = 0
while kysymys != 5:
    kaupunki = str(input("anna kaupunki: "))
    lista.append(kaupunki)
    kysymys += 1
for i in lista:
    print(i)