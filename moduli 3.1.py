kuha = float(input("kuhan pituus: "))
if kuha < 37:
    puuttuu = 37 - kuha
    print(f"kalasi puuttuu {puuttuu} cm pituus niin pitää laittaa takaisin veteen")
else:
    print("kala saa syödä")
