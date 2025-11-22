from flask import Flask, jsonify
from db.utils import load_data_from_db

app = Flask(__name__)

@app.route('/')
def initial_message():
    return jsonify({"response":'Questo è il messaggio di benvenuto'})

@app.route('/nazioni', methods=['GET'])
def get_nazioni():
    data = load_data_from_db()
    nazioni = data['Nazione']
    return jsonify(nazioni), 200

if __name__ == "__main__":
    app.run(debug=True)