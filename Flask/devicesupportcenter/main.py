from flask import Flask, jsonify, request, url_for
from db import repair_center
from laptop import Laptop
from smartphone import Smartphone

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"message": "Welcome to Service Center API",
                    "links": {
                        "list_devices": url_for('get_all_devices'),
                        "sample_device": url_for('get_device', id="s1"),
                        "sample_estimate": url_for('get_estimated_total_time', id="s1", factor=1.5)
                    }}), 200

@app.route('/devices')
def get_all_devices():
    return jsonify(repair_center.list_all()), 200

# get methods
@app.route('/devices/<string:id>')
def get_device(id: str):
    d = repair_center.get(id)
    if d:
        return jsonify(d.info()), 200
    return jsonify({"error": "device not found"}), 404

@app.route('/devices/<string:id>/estimate/<float:factor>')
def get_estimated_total_time(id: str, factor: float = 1.0):
    d = repair_center.get(id)
    if d:
        return jsonify({"id": d.id,
                        "device_type": d.device_type(),
                        "factor": factor,
                        "estimated_total_minutes": d.estimated_total_time(factor)
        }), 200

    return jsonify({"error": "device not found"}), 404

@app.route('/devices', methods=['POST'])
def add_devices():
    json = request.get_json()

    # se null o type non presente
    if not json or "type" not in json:
        return jsonify({"error": "missing type"}), 400

    # requisit laptop
    laptop_req = [
        "id", "model", "customer_name", "purchase_year",
        "status", "has_dedicated_gpu", "screen_size_inches"
    ]

    # requisiti smarthphone
    smartphone_req = [
        "id", "model", "customer_name", "purchase_year",
        "status", "has_protective_case", "storage_gb"
    ]


    if json["type"] == "laptop":
        # itero per le chiavi necessarie
        for k in laptop_req:

            # se non presente returno 400 errore
            if k not in json:
                return jsonify({"error": f"missing field {k}"}), 400

        # creo oggetto
        l = Laptop(
            id=json["id"],
            model=json["model"],
            customer_name=json["customer_name"],
            puchase_year=json["purchase_year"],
            status=json["status"],
            has_dedicated_gpu=json["has_dedicated_gpu"],
            screen_size_inches=json["screen_size_inches"]
        )

        # aggiungo
        repair_center.add(l)

        # ritorno info + 201 (risorsa creata)
        return jsonify(l.info()), 201

    elif json["type"] == "smartphone":
        # controllo che i campi richiesti siano in json
        for k in smartphone_req:
            if k not in json:
                return jsonify({"error": f"missing field {k}"}), 400

        # creo oggetto
        s = Smartphone(
            id=json["id"],
            model=json["model"],
            customer_name=json["customer_name"],
            purchase_year=json["purchase_year"],
            status=json["status"],
            has_protective_case=json["has_protective_case"],
            storage_gb=json["storage_gb"]
        )
        # aggiungo e ritorno
        repair_center.add(s)
        return jsonify(s.info()), 201

    else:
        # se type non e ne laptop ne smarthphone
        return jsonify({"error": f"type {json['type']} is invalid"}), 400

@app.route('/devices/<string:device_id>', methods=['PUT'])
def update_device(device_id: str):
    json = request.get_json()
    d = repair_center.get(device_id)
    if d:
        # se null o type non presente
        if not json or "type" not in json:
            return jsonify({"error": "missing type"}), 400

        # requisit laptop
        laptop_req = [
            "id", "model", "customer_name", "purchase_year",
            "status", "has_dedicated_gpu", "screen_size_inches"
        ]

        # requisiti smarthphone
        smartphone_req = [
            "id", "model", "customer_name", "purchase_year",
            "status", "has_protective_case", "storage_gb"
        ]

        if json["type"] == "laptop":
            # itero per le chiavi necessarie
            for k in laptop_req:

                # se non presente returno 400 errore
                if k not in json:
                    return jsonify({"error": f"missing field {k}"}), 400

            # creo oggetto
            l = Laptop(
                id=json["id"],
                model=json["model"],
                customer_name=json["customer_name"],
                puchase_year=json["purchase_year"],
                status=json["status"],
                has_dedicated_gpu=json["has_dedicated_gpu"],
                screen_size_inches=json["screen_size_inches"]
            )

            # aggiungo
            repair_center.update(device_id, l)

            # ritorno info + 201 (risorsa creata)
            return jsonify(l.info()), 200

        elif json["type"] == "smartphone":
            # controllo che i campi richiesti siano in json
            for k in smartphone_req:
                if k not in json:
                    return jsonify({"error": f"missing field {k}"}), 400

            # creo oggetto
            s = Smartphone(
                id=json["id"],
                model=json["model"],
                customer_name=json["customer_name"],
                purchase_year=json["purchase_year"],
                status=json["status"],
                has_protective_case=json["has_protective_case"],
                storage_gb=json["storage_gb"]
            )
            # aggiungo e ritorno
            repair_center.update(device_id,s)
            return jsonify(s.info()), 200
    return jsonify({"error", "device not found"})

@app.route('/devices/<string:device_id>/status', methods=['PATCH'])
def patch_status(device_id: str):
    d = repair_center.get(device_id)
    json = request.get_json()

    if not json or "status" not in json:
        return jsonify({"error": "missing status"}), 400

    if d:
        repair_center.patch_status(device_id, json["status"])
        return jsonify(d.info()), 200

    return jsonify({"error": "device not found"}), 404

@app.route('/devices/<string:device_id>', methods=['DELETE'])
def delete_device(device_id:str):
    d = repair_center.get(device_id)
    if d:
        repair_center.delete(device_id)
        return jsonify({"deleted": True, "id": device_id}), 200
    return jsonify({"error": "device not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)