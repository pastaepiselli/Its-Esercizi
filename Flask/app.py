from flask import Flask, url_for

# creo un istanza di flask
app = Flask(__name__)

# app run se lascaita vuota prende valodi di default

# se non abbiamo app.run utilizziamo il comando
#flask --app 'nomeapp' run, qui posso modificare cmq debug e host
# app.run(debug=True) # deve sempre stare alla fine del file,

# senno chiamiamo il file app.py 
# e da terminale il comando e flask run, sempre la possibilita di modificare debug, host, port

@app.route('/')  # radice del client   , percorso statico 
def home() -> str:
    return "<h3> Hello world!</h3>"


@app.route('/user/<string:username>/age/<int:age>') # di base questa e una chiamata get
def show_user_profile(username: str, age: int) -> str:
    return f"Profilo di {username}: lunghezza pisello: {age}cm"

@app.route('/post/<int:post_id>')
def show_post_id(post_id: int) -> int:
    return f"Post {post_id}"

with app.test_request_context():
    print(url_for('home'))
    print(url_for('show_user_profile', username='popa', age=45))