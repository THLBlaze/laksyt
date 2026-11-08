from flask import Flask, jsonify
import math

app = Flask(__name__)


def on_alkuluku(luku):
    if luku < 2:
        return False

    for i in range(2, math.isqrt(luku) + 1):
        if luku % i == 0:
            return False

    return True


@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    tulos = on_alkuluku(luku)

    return jsonify({
        "Number": luku,
        "isPrime": tulos
    })


if __name__ == '__main__':
    app.run(port=3000)
