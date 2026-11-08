
import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/kenttä/<icao>')
def lentokentta(icao):

    yhteys = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user="root",
        password="fortnite06"
    )

    kursori = yhteys.cursor()

    sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao.upper(),))

    tulos = kursori.fetchone()

    kursori.close()
    yhteys.close()

    if tulos:
        vastaus = {
            "ICAO": tulos[0],
            "Name": tulos[1],
            "Municipality": tulos[2]
        }
        return jsonify(vastaus)

    return jsonify({"error": "Lentokenttää ei löydy"}), 404


if __name__ == '__main__':
    app.run(port=3000)
