from flask import Flask

app = Flask(__name__)

@app.route("/helloworld/<luku>")

def helloworld(luku):
    try:
        määrä=int(luku)
        vastaus = "Hello world! " * määrä
        return vastaus
    except:
        return "Virhe: Anna kokonais luku!"

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)
