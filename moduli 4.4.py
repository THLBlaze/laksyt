import random
arpo_luku = random.randint(1, 10)
arvaus_viesti = int(input("arvaa arpo luku: "))
while arvaus_viesti != arpo_luku:
    if arvaus_viesti > arpo_luku:
        print(f" {arvaus_viesti} on liian suuri arvaus")
        arvaus_viesti = int(input("arvaa arpo luku: "))
    else:
        print(f" {arvaus_viesti} on liian pieni arvaus")
        arvaus_viesti = int(input("arvaa arpo luku: "))
print("vastasit oikea")
