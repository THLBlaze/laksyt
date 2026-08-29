while True:
    tuumia_määrä = int(input("lisää tuuma määrä: "))
    if tuumia_määrä < 0:
        print("laitoit negatiivinen numero")
        break
    tuumia_sentimetri = tuumia_määrä * 2.54
    print(f" {tuumia_määrä} tuuma = {tuumia_sentimetri:.3} cm ")