from flask import Flask

app = Flask(__name__)

@app.route("/alkuluku/<luku>")

def alkuluku(luku):
    luku = int(luku)
    jako = 0

    for i in range(1, luku ):
        if luku % i == 0:
            jako += 1  

    if jako == 1:
        on_alkuluku = True
    else:
        on_alkuluku = False

    vastaus = {"Number": luku , "isPrime": on_alkuluku}
    return vastaus

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)
