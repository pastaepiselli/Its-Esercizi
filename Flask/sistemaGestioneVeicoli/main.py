
from db import rental
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to Rent Service Api"}), 200

@app.route('/vehicles')
def get_all_vehicles():
    return jsonify(rental.list_all()), 200

@app.route('/vehicles/<string:plate_id>')
def get_vehicles(plate_id: str):
    if plate_id in rental.vehicles:
        return jsonify(rental.get(plate_id).info()), 200
    return jsonify({"error": "plate does not exist"}), 404

if __name__ == "__main__":
    app.run(debug=True)

