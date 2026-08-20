luokka = str(input("mikä lippu luokka: "))
if luokka == "LUX":
    print(luokka , "on parvekkeellinen hytti yläkannella.")
elif luokka == "A" or luokka == "B" or luokka == "C":
    print(luokka , "on ikkkunaton hytti autokannen yläpuolella")
else:
    print("luokka ovat LUX,A,B ja C")