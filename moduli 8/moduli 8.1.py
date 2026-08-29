import mysql.connector
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="fortnite06",
    autocommit=True
    )
icoa_koodi = input("anna icao koodi: ")
sql = "select municipality, name from airport where ident like %s "
kursori = yhteys.cursor()
kursori.execute(sql,(icoa_koodi,))

tulos = kursori.fetchall()
for rivi in tulos:
    print(rivi)