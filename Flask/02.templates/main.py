"""
    Bien demarrer avec flask
    
    1.Les Templates

    un template = fichier HTML + code python

"""

from flask import Flask, render_template

app = Flask(__name__, template_folder="assets/templates")

@app.route("/")
def index():
    return "Hello World"

@app.route("/apropos/")
def apropos():
    return "Qui suis-je?"

@app.route("/contact/")
def contact():
    return "Me contacter"


if __name__ == "__main__":
    app.run(debug=True)