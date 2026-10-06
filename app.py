from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/om")
def om():
    return render_template("om.html")

@app.route("/profil")
def profil():
    return "profil"

@app.route("/prosjekter")
def proskjekter():
    return "proskjekter"

@app.route("/kontakt")
def kontakt():
    return "kontakt"

if __name__ == "__main__":
    app.run(debug=True)