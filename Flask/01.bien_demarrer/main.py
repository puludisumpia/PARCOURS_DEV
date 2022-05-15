"""
    Bien demarrer avec flask
    
    1.Les routes

    Une route = decorateur + fonction

    Donc dans ce mondule nous avons 3 routes:
    - index
    - apropos
    - contact
"""

from flask import Flask

app = Flask(__name__)

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