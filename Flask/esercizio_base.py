from flask import Flask

app = Flask(__name__)


@app.route('/')
def home() -> str:
    return "<p>Home</p>"

@app.route('/about')
def about() -> str:
    return "<p>Descrizione app, autore Lorenzo Rossi</p>"

