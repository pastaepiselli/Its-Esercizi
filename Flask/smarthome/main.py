from flask import Flask, jsonify, url_for, request
from SecurityCamera import SecurityCamera
from SmartBulb import SmartBulb
from db import hub

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Smart Home Hub API",
                    "links": {
                        "device_list": url_for('get_all_devices'),
                        "device_sample": url_for('get_device', serial_number="CAM123456"),
                        "estimate_sample": url_for('get_diagnostic_time', serial_number="CAM123456", factor=1.5)
                    }})

@app.route('/devices')
def get_all_devices():
    return jsonify(hub.list_all()), 200


@app.route('/devices/<string:serial_number>')
def get_device(serial_number: str):
    d = hub.get(serial_number)
    if d is None:
        return jsonify({"error": f"device with serial number {serial_number} not found"}), 404
    return jsonify(d.info()), 200

@app.route('/devices/<string:serial_number>/diagnostic/<float:factor>', methods=['GET'])
def get_diagnostic_time(serial_number: str, factor: float):
    d = hub.get(serial_number)

    if d is None:
        return jsonify({"error": f"serial_number {serial_number} not found"}), 404
    return jsonify({"id": serial_number,
                    "device_type": d.device_type(),
                    "factor": factor,
                    "diagnostic_seconds": d.diagnostic_time(factor)}), 200

@app.route('/devices', methods=['POST'])
def add_device():
    json = request.get_json()

    if json is None:
        return jsonify({"error": "empty payload"}), 400
    if "type" not in json:
        return jsonify({"error": "missing type"}), 400
    if json["type"] not in ("bulb", "camera"):
        return jsonify({"error": "type not valid"}), 400

    common_key = ["serial_number", "brand", "room", "installation_year", "status"]

    if json["type"] == "bulb":
        specific_key = ["brightness_lumens", "color_capability"]
    else:
        specific_key = ["resolution", "night_vision"]

    for k in common_key + specific_key:
        if k not in json:
            return {"error": f"missing field {k}"}, 400

    if json["type"] == "bulb":
        device: SmartBulb = SmartBulb(serial_number=json["serial_number"],
                           brand=json["brand"],
                           room=json["room"],
                           installation_year=json["installation_year"],
                           status=json["status"],
                           brightness_lumens=json["brightness_lumens"],
                           color_capability=json["color_capability"])
    else:
        device: SecurityCamera = SecurityCamera(serial_number=json["serial_number"],
                                                brand=json["brand"],
                                                room=json["room"],
                                                installation_year=json["installation_year"],
                                                status=json["status"],
                                                resolution=json["resolution"],
                                                night_vision=json["night_vision"])
    if hub.add(device):
        return jsonify(device.info()), 201
    return jsonify({"error": "device already exists"}), 409 # conflitto di risorse

@app.route('/devices/<string:serial_number>', methods=['PUT'])
def update_device(serial_number: str):
    d = hub.get(serial_number)
    json = request.get_json()
    if d is None:
        return jsonify({"error": "device not found"}), 404
    if json is None:
        return jsonify({"error": "payload is empty"}), 400
    if "type" not in json:
        return jsonify({"error": "missing type"}), 400
    if json["type"] not in ("bulb", "camera"):
        return jsonify({"error": "invalid type"}), 400

    common_key = ["serial_number", "brand", "room", "installation_year", "status"]

    if json["type"] == "bulb":
        specific_key = ["brightness_lumens", "color_capability"]
    else:
        specific_key = ["resolution", "night_vision"]

    for k in common_key + specific_key:
        if k not in json:
            return jsonify({"error": f"missing field: {k}"}), 400

    # controllo serial_number deve essere uguale
    if json["serial_number"] != d.serial_number:
        return jsonify({"error": "serial_number in body must match url"}), 400

    if json["type"] == "bulb":
        device: SmartBulb = SmartBulb(serial_number=json["serial_number"],
                                      brand=json["brand"],
                                      room=json["room"],
                                      installation_year=json["installation_year"],
                                      status=json["status"],
                                      brightness_lumens=json["brightness_lumens"],
                                      color_capability=json["color_capability"])
    else:
        device: SecurityCamera = SecurityCamera(serial_number=json["serial_number"],
                                      brand=json["brand"],
                                      room=json["room"],
                                      installation_year=json["installation_year"],
                                      status=json["status"],
                                      resolution=json["resolution"],
                                      night_vision=json["night_vision"])
    hub.update(serial_number, device)
    return jsonify(device.info()), 200

@app.route('/devices/<string:serial_number>/status', methods=['PATCH'])
def patch_status(serial_number: str):
    d = hub.get(serial_number)
    json = request.get_json()

    if d is None:
        return jsonify({"error": "device not found"}), 404
    if json is None:
        return jsonify({"error": "payload is empty"}), 400
    if "status" not in json:
        return jsonify({"error": "status must be in json"}), 400
    if json["status"] not in ("online", "offline", "updating", "error"):
        return jsonify({"error": f"status {json["status"]} not valid"}), 400

    hub.patch_status(serial_number, json["status"])
    return jsonify(d.info())

@app.route('/devices/<string:serial_number>', methods=['DELETE'])
def delete_device(serial_number: str):
    d = hub.get(serial_number)
    if d is None:
        return jsonify({"error": "device not found"}), 404

    hub.delete(serial_number)
    return jsonify({"deleted": True, "serial_number": serial_number}), 200



if __name__ == "__main__":
    app.run(debug=True)