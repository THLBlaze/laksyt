leiviskä = float(input("Anna leiviskät"))
nauha = float(input("Anna naulat"))
luoti = float(input("anna luodit"))
luku1 = (leiviskä * 20)
luku2 = (luku1 + nauha) * 32
luku3 = (luku2 + luoti) * 13.3
kg = luku3/1000
gra = int(kg)
kunnon = int((kg - gra) * 1000)
print(f"kilon on {gra} kg ja gramma on {kunnon} g")
