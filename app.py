from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    alder = 17
    return render_template("index.html", alder=alder)

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

@app.route("/fag")
def fag():
    fagliste = ["Python","Flask","HTML","CSS"]
    return render_template("fag.html", fag=fagliste)

@app.route("/film")
def film():
    filmliste = ["movie1","movie2","movie3","movie4","moive5"]
    return render_template("film.html", film=filmliste)

# @app.route("/registrering", methods=["GET","POST"])
# def registrering():

#     if request.method == "POST":
#         navn = request.form["navn"]
#         return f"hei {navn}"

#     return render_template("registrerings.html")

@app.route("/registrerings", methods=["GET","POST"])

def registrerings():
    if request.method == "POST":
        navn = request.form["navn"]
        fag = request.form["fag"]

        return render_template(
            "resultat.html",
            navn=navn,
            fag=fag
        )
    return render_template("registrerings.html")

@app.route("/kurs")
def kurs():
    kursliste = ["Python","Flask","Javascript","Linux"]
    return render_template("kurs.html", kursliste=kursliste)

if __name__ == "__main__":
    app.run(debug=True)