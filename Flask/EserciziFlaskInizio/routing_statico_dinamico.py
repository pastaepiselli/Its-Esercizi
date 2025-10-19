from flask import Flask

app = Flask(__name__)


@app.route('/')
def home() -> str:
    return "<h1>Home</h1>"

@app.route('/user/<string:nome>')
def user(nome: str) -> str:
    return f"<h2>Benvenuto {nome}</h2>!"

@app.route('/square/<int:n>')
def square(n: int) -> int:
    return f"<h2>{pow(n, 2)}</h2>"

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int) -> str:
    return f"<h2>{a + b}</h2>"