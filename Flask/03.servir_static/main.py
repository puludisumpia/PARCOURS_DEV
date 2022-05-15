"""
    Bien demarrer avec flask
    
    2.Les Statiques

    un static = images, js, css, font

    
    On definit le lien vers le dossier static
    via la variable "static_folder" dans l'initialisation
    de l'app comme ceci: app = Flask(__name__, static_folder="assets/static")

"""

from flask import Flask, render_template

app = Flask(__name__, 
    template_folder="assets/templates",
    static_folder="assets/static"
)

@app.route("/")
def index():
    '''
        On va servir ici, les:
        - fichiers css
        - fichiers js
        - images 
    '''
    return render_template("index.html", title="Bienvenu à tous")

if __name__ == "__main__":
    app.run(debug=True)