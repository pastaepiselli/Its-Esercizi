from flask import Flask, jsonify, request
from db import s


app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Animal Shelter API"}), 200

@app.route('/animals')
def get_all_animals():
    # d = {}
    # for a in s.animals:
    #     d[a.id] = a.info()
    # return  jsonify(d)

    return jsonify({k: v.info() for k, v in s.animals.items()}), 200

@app.route('/animals/<string:id>')
def get_animal(id: str):
    # ricerca
    if id in s.animals:
        # accedo alla classe e chiamo .info(), necessario dizionario
        return  jsonify(s.animals[id].info()), 200
    # non trovo ritorno errore + 404 status code
    return jsonify({"error": "animal not found"}), 404

@app.route('/animals/<string:id>/food')
def get_daily_food(id: str):
    if id in s.animals:
        return jsonify({"id": id, "daily_food_grams": s.animals[id].daily_food_grams()}), 200

    return jsonify({"error": "animal not found"}), 404

@app.route('/animals/<string:id>/adoptions')
def adoption_state(id: str):
    if s.is_adopted(id):
        return jsonify({"id": id, "adopted": True, "adopter_name": s.adoptions[id]}), 200

    return jsonify({"id": id, "adopted": False}), 404

@app.route('/animals/add', methods=['POST'])
def add_animal():
    payload = request.get_json()


if __name__ == "__main__":
    app.run(debug=True)