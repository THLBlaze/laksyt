lentokenttä = {}
print("kirjotta vaihto ehdot")
print("uusi lentokenttä")
print("hae lentokenttä")
print("lopettaa")
valinnat = input("syötä: ")
while valinnat != "lopettaa":
    if valinnat == "uusi lentokenttä":
        ICAO_koodi = input("lisää uusi ICAO koodi: "))
        lentokenttä_nimi = input("lisää uusi lentokenttä nimi: ")
        lentokenttä[ICAO_koodi] = lentokenttä_nimi
    elif valinnat == "hae lentokenttä":
        ICAO_koodi_etsiminen = input("anna ICAO koodi: "))
        if ICAO_koodi_etsiminen in lentokenttä:
            print(lentokenttä[ICAO_koodi_etsiminen])
        else:
            print("ICAO koodi ei ole olemassa")
    valinnat = input("syötä uudelleen komennot: ")

