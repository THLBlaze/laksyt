import random
heitto_määrä = int(input("kuinka monta kertaa heitetään noppa: ")) #kyysyy että monta kerta heitetään noppa
noppa_tulo = [] #rankentaa lista
Heitto = 0 #lopetus numero

while Heitto != heitto_määrä: #eli jos Heitto ei ole sama kuin määrä niin laskee
    tulos = random.randint(1,6) #tulostaa random numero 1-6
    noppa_tulo.append(tulos) #listalle lisätään tulos eli noin numerot
    Heitto += 1 #heitto lisääntyy ja jos se menee samaksi kuin heitto määrä niin ohjelma lopettaa
for i in noppa_tulo: # tulostaa lista alas päin
    print(i)
print("eli noppa tulo on ", sum(noppa_tulo)) #sum koodi plussaa listasta numerot yhteen