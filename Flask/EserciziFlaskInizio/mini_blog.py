from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def home() -> str:
    return "<h1>Home<h1>"

@app.route('/post/<int:id>')
def post(id: int) -> str:
    return "<p>Ad aranova si lamentano di boooo</p>"

@app.route('/posts')
def posts() -> str:
    return f"""<a href={url_for('post', id=1)}>Articolo 1</a>
    <a href={url_for('post', id=2)}>Articolo 2</a>
    <a href={url_for('post', id=3)}>Articolo 3</a>"""