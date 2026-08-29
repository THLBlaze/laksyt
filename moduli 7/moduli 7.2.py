nimet = set()
nimi = input("anna nimi: ")
while nimi != "":
    if nimi not in nimet:
        print("uusi nimi")
    elif nimi in nimet:
        print("aiemmin syötetty")
    nimet.add(nimi)
    nimi = input("anna nimi: ")
print(nimet)

