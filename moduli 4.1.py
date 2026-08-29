aloitus_luku = 3
lasku = 0
while aloitus_luku < 1000:
    if lasku > 1000:
        break
    lasku = aloitus_luku * 3
    aloitus_luku += 1

    print(lasku)

