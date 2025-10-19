from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return f"""<a href={url_for('about')}>About</a>
            <a href={url_for('users')}>Users</a> """

@app.route('/about')
def about() -> str:
    return "<h2>About</h2>"

@app.route('/users')
def users() -> str:
    return "<h2>Pagina degli users</h2>"

@app.route('/users/<string:nome>')
def selected_user(nome: str) -> str:
    return f"<p>Benvenuto {nome}</p>"

