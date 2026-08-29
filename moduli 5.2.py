luvut = str(input("anna luvut: ")) #str koska muuten ei pysty käyttä "" että laittaissi tyhjä
lista = []
while luvut != "":
    lista.append(luvut)
    luvut = str(input("anna luvut: "))
lista.sort(reverse=True) #käänttää lista järjestys

for i in lista:
    print(i)
