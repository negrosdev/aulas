from flask import Blueprint, render_template

home = Blueprint('home', __name__, url_prefix='/pagina-principal')

@home.get('/')
def index():
    return render_template("index.html")
