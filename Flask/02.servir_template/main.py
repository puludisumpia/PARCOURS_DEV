"""
    Bien demarrer avec flask
    
    2.Les Templates

    un template = fichier HTML + code python

    On importe render_template depuis flask et
    on definit le lien vers le dossier templates
    via la variable "template_folder" dans l'initialisation
    de l'app comme ceci: app = Flask(__name__, template_folder="assets/templates")

"""

from flask import Flask, render_template

app = Flask(__name__, template_folder="assets/templates")

@app.route("/")
def index():
    return render_template("index.html", title="Bienvenu")

@app.route("/apropos/")
def apropos():
    return render_template("apropos.html", title ="Qui suis-je?")

@app.route("/contact/")
def contact():
    return render_template("contact.html", title="Me contacter")


if __name__ == "__main__":
    app.run(debug=True)