from car import Car
from db import rental
from flask import Flask, jsonify, request, url_for

from van import Van

app = Flask(__name__)

# metodi get
@app.route('/')
def index():
    return jsonify({"message": "Welcome to Rent Service Api",
                    "links": {
                        "vehicles_list": url_for('get_all_vehicles'),
                        "vehicle_sample": url_for('get_vehicle', plate_id="BG123AE"),
                        "estimate_sample": url_for('get_estimated_prep_time', plate_id="BG123AE", factor=1.5)
                    }}), 200

@app.route('/vehicles')
def get_all_vehicles():
    return jsonify(rental.list_all()), 200

@app.route('/vehicles/<string:plate_id>')
def get_vehicle(plate_id: str):
    if plate_id in rental.vehicles:
        return jsonify(rental.get(plate_id).info()), 200
    return jsonify({"error": "plate does not exist"}), 404

@app.route('/vehicles/<string:plate_id>/prep-time/<float:factor>')
def get_estimated_prep_time(plate_id: str, factor: float = 1.0):
    v = rental.get(plate_id)
    if v:
        return jsonify({"id": plate_id,
                        "device_type": v.vehicle_type(),
                        "factor": factor,
                        "estimated_total_minutes": v.estimated_prep_time(factor)})
    return jsonify({"error": "plate does not exist"})

@app.route('/vehicles', methods=['POST'])
def add_vehicles():
    # ottengo il payload
    json = request.get_json()

    # se e vuoto errore
    if json is None:
        return jsonify({"error": "payload empty"}), 400

    # se non e presente type
    if "type" not in json:
        return jsonify({"error": "missing key: type"}), 400

    # campi in comune
    common_key = [
        "plate_id", "model", "driver_name", "registration_year", "status",
    ]
    # controllo tipo per aggiunta campi specifici
    if json["type"] == "car":
        specific_key = ["doors", "is_cabrio"]
    elif json["type"] == "van":
        specific_key = ["max_load_kg", "require_special_license"]
    else:
        return jsonify({"error": "type can be van or car"}), 400
    # controllo chiavi payload
    for k in (common_key + specific_key):
        if k not in json:
            return jsonify({"error": f"missing field: {k}"})

    # istanzio le classi
    if json["type"] == "car":
        vehicle: Car = Car(plate_id=json["plate_id"],
                     model=json["model"],
                     driver_name=json["driver_name"],
                     registration_year=json["registration_year"],
                     status=json["status"],
                     doors=json["doors"],
                     is_cabrio=json["is_cabrio"])
    else:
        vehicle: Van = Van(plate_id=json["plate_id"],
                     model=json["model"],
                     driver_name=json["driver_name"],
                     registration_year=json["registration_year"],
                     status=json["status"],
                     max_load_kg=json["max_load_kg"],
                     require_special_license=json["require_special_license"])
    # controllo se plate id esiste
    if rental.add(vehicle):
        return jsonify(vehicle.info()), 201
    return jsonify({"error": f"vehicle plate_id: {vehicle.plate_id} already exists"})

@app.route('/vehicles/<string:plate_id>', methods=["PUT"])
def update_vehicle(plate_id: str):
    # ottengo payload
    json = request.get_json()

    # controllo se vuoto
    if json is None:
        return jsonify({"error": "payload is empty"}), 400

    # controllo se esite la risorsa da restituire
    if rental.get(plate_id) is None:
        return jsonify({"error": "vehicle not found"}), 404

    # controllo se plate_id e uguale a quello nell'uri
    if json["plate_id"] != plate_id:
        return  jsonify({"error": "plate_id does not match"}), 400

    # stesso discorso della post
    common_key = [
        "plate_id", "model", "driver_name", "registration_year", "status",
    ]

    if json["type"] == "car":
        specific_key = ["doors", "is_cabrio"]
    elif json["type"] == "van":
        specific_key = ["max_load_kg", "require_special_license"]
    else:
        return jsonify({"error": "type can be van or car"}), 400
    for k in (common_key + specific_key):
        if k not in json:
            return jsonify({"error": f"missing field: {k}"}), 400

    if json["type"] == "car":
        vehicle: Car = Car(plate_id=json["plate_id"],
                           model=json["model"],
                           driver_name=json["driver_name"],
                           registration_year=json["registration_year"],
                           status=json["status"],
                           doors=json["doors"],
                           is_cabrio=json["is_cabrio"])
    else:
        vehicle: Van = Van(plate_id=json["plate_id"],
                           model=json["model"],
                           driver_name=json["driver_name"],
                           registration_year=json["registration_year"],
                           status=json["status"],
                           max_load_kg=json["max_load_kg"],
                           require_special_license=json["require_special_license"])

    # in questo caso aggiono la risora
    rental.update(plate_id, vehicle)
    return jsonify(vehicle.info()), 200

@app.route('/vehicles/<string:plate_id>/status', methods=['PATCH'])
def patch_status(plate_id: str):
    # ottengo payload
    json = request.get_json()

    # controllo se json e vuoto
    if json is None:
        return jsonify({"error": "payload is empty"}), 400

    # controllo se la risorsa esiste
    if rental.get(plate_id) is None:
        return jsonify({"error", "plate_id does not exists"}), 404

    # cotrolli validita del payoload
    if "status" not in json:
        return jsonify({"error": "status in required"}), 400
    if json["status"] not in ("available", "rented", "maintenance", "cleaning", "retired"):
        return jsonify({"error": f"status cannot be {json["status"]}"})

    # modifico status
    rental.patch_status(plate_id, json["status"])
    return jsonify(rental.get(plate_id).info()), 200

@app.route('/vehicles/<string:plate_id>', methods=["DELETE"])
def delete_vehicle(plate_id: str):
    v = rental.get(plate_id)
    # se esiste elimino
    if v:
        rental.delete(plate_id)
        return jsonify({"deleted": True, "plate_id": plate_id}), 200

    return jsonify({"error": "plate_id not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

