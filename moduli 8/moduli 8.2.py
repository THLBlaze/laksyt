import mysql.connector
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="fortnite06",
    autocommit=True
    )
maa_tunnus = input("syötä tunnus: ")
sql = "select name from airport where iso_country like %s and type = 'small_airport';"
kursori = yhteys.cursor()
kursori.execute(sql,(maa_tunnus,))

tulos = len(kursori.fetchall())
print(tulos)