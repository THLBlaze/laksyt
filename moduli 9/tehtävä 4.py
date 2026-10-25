import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = self.nopeus + muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + self.nopeus * tunnit


autot = []

for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    rekisteritunnus = "ABC-" + str(i)

    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


kilpailu_jatkuu = True

while kilpailu_jatkuu:

    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_jatkuu = False


print("Rekisteri   Huippunopeus   Nopeus   Matka")

for auto in autot:
    print(
        auto.rekisteritunnus,
        auto.huippunopeus,
        auto.nopeus,
        auto.kuljettu_matka
    )
