import random
noppa = random.randint(1,6)
noppa2 = random.randint(1,6)
halu = str(input("haluatko heittää noppa: "))
if halu == "joo":
    print(f"enka numero on {noppa} ")
    print(f"toka numero on {noppa2} ")
else:
    print("ens kerral")
