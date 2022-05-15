"""
    Bien demarrer avec flask
    
    4.Language de Gabarit

    un template = fichier HTML + code python
"""
from datetime import datetime
import dateutil.parser

from flask import Flask, render_template


app = Flask(__name__, 
    template_folder="assets/templates",
    static_folder="assets/static"
)

@app.template_filter("strftime")
def _jinja2_filter_datetime(date, fmt=None):
    date = dateutil.parser.parse(date)
    native = date.replace(tzinfo=None)
    format='%d %b %Y'
    return native.strftime(format) 

@app.route("/")
def index():
    fruits = ["Mangue", "Papaye", "Orange"]
    posts = [
        {"id": 1, "title": "Aventures de tintin"},
        {"id": 2, "title": "Le shell pour tous"},
        {"id": 3, "title": "Les essais de Mpia"}
    ]
    identite = "Mpia Mimpiya"

    return render_template(
        "index.html",
        fruits=fruits,
        posts=posts,
        identite=identite,
        date=str(datetime.utcnow())
    )

if __name__ == "__main__":
    app.run(debug=True)