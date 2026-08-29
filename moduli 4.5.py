käyttäjä = str(input("käyttäjä: "))
salasana = str(input("salasana: "))
yritykset = 0
käyttäjä1 = "Petri"
salasana1 = "SQL"
while True:
    yritykset += 1
    if käyttäjä == käyttäjä1 and salasana == salasana1:
        print("pääsit sisään")
        break
    elif yritykset == 3:
        print("liian monta yritys")
        break
    else:
        print("yritäuudelleen")
        käyttäjä = str(input("käyttäjä: "))
        salasana = str(input("salasana: "))




