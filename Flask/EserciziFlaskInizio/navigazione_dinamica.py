from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return f"<a href={url_for('users_profile')}>Utenti</a>"


@app.route('/users')
def users_profile() -> str:
    return f"""<a href={url_for('show_user', name= 'Marco')}>Marco</a>
                <a href={url_for('show_user', name= 'Popa')}>Popa</a>
                <a href={url_for('show_user', name= 'Luca')}>Luca</a>"""


@app.route('/users/<string:name>')
def show_user(name: str) -> str:
    return f"<h5>Nome: {name} </h5>"

