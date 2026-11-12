###############################################################
#   Näyttää oudolta ehkä otettu osia peliprojektin koodista   #    
###############################################################
# ja salasana poistettu yhteystiedoista
from flask import Flask #
import mysql.connector
YHTEYS_TIEDOT = {
    "host": "127.0.0.1",
    "port": 3306,
    "database": "flight_game",
    "user": "atte",
    "password": "******",
    "autocommit": True,
    "collation": "utf8mb4_general_ci",
}

def avaa_yhteys():
    """Avaa yhteyden tietokantaan ja palauttaa yhteysolion."""
    return mysql.connector.connect(**YHTEYS_TIEDOT)

app = Flask(__name__)#

@app.route("/kenttä/<icao>")#

def hae_kentta_tiedot(icao):
    icao = icao.upper()
    yhteys = avaa_yhteys()
    kursori = yhteys.cursor(dictionary=True)
    sql = """SELECT ident, name, municipality
         FROM airport
         WHERE ident = %s"""
    kursori.execute(sql, (icao,))
    rivi = kursori.fetchone()
    kursori.close()
    yhteys.close()
    vastaus = {#
        "ICAO":rivi["ident"],
        "Name":rivi["name"],
        "Municipality":rivi["municipality"]
    }
    return vastaus

if __name__ == "__main__":#
    app.run(use_reloader=True, host="127.0.0.1", port=3000)
