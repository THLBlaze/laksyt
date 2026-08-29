import random
N = int(input("montako pistettä arvotaan? "))
n = 0

for i in range(N):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1) # .uniform antaa random desimaali lukuja -1, 1 väliltä

    if x**2 + y**2 < 1: # ** tarkoittaa potenssi lasku eli x potensi 2
        n += 1
pi = 4 * n / N
print("piin likiarvo on", pi)

