from re import L
from flask import Flask
from blueprints.home_blueprint import home


app = Flask(__name__)
app.register_blueprint(home)

app.run()