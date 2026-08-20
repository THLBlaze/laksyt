
sukupuoli = input("Anna biologinen sukupuolesi (nainen tai mies): ")
hemoglobiini = float(input("Anna hemoglobiiniarvosi (g/l): "))
if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobiini > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")

elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobiini > 195:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")

else:
    print("Anna vain 'nainen' tai 'mies'.")


