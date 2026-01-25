from colorsys import hsv_to_rgb

from flask import Flask, url_for, request, jsonify

from DiagnosticExam import DiagnosticExam
from MedicalVisit import MedicalVisit
from db import ch

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return jsonify({"message": "Clinic Booking Hub Api",
                    "links": {
                        "booking_list": url_for('get_all_bookings'),
                        "booking_sample": url_for('get_booking', booking_id="BK-101"),
                    }})

@app.route('/bookings', methods=["GET"])
def get_all_bookings():
    return jsonify(ch.list_all()), 200

@app.route('/bookings/<string:booking_id>')
def get_booking(booking_id: str):
    b = ch.get(booking_id)
    if b is None:
        return jsonify({"error": "booking not found"}), 404
    return jsonify(b.info()), 200

@app.route('/bookings/<string:booking_id>/wait/<float:factor>', methods=["GET"])
def get_estimated_wait(booking_id: str, factor: float):
    b = ch.get(booking_id)
    if b is None:
        return jsonify({"error": "booking not found"}), 404
    return jsonify({"booking_id": booking_id,
                    "booking_type": b.booking_type(),
                    "factor": factor,
                    "estimated_wait_minutes": b.estimated_wait(factor)}), 200

@app.route('/bookings', methods=["POST"])
def add_booking():
    json = request.get_json(silent=True)

    if json is None:
        return jsonify({"error": "payload empty"}), 400

    if "type" not in json:
        return jsonify({"error": "missing type"}), 400

    if json["type"] not in ("visit", "exam"):
        return jsonify({"error": f"type: {json['type']} not valid"}), 400

    common_keys = [
        "booking_id", "patient_name", "doctor", "department", "date", "time", "status"
    ]

    if json["type"] == "visit":
        specific_keys = [
            "visit_reason", "first_time"
        ]
    else:
        specific_keys = [
            "exam_type", "requires_fasting"
        ]

    for k in common_keys + specific_keys:
        if k not in json:
            return jsonify({"error": f"missing field {k}"}), 400

    if json["type"] == "visit":
        booking: MedicalVisit = MedicalVisit(
            booking_id=json["booking_id"],
            patient_name=json["patient_name"],
            doctor=json["doctor"],
            department=json["department"],
            date=json["date"],
            time=json["time"],
            status=json["status"],
            visit_reason=json["visit_reason"],
            first_time=json["first_time"]
        )
    else:
        booking: DiagnosticExam = DiagnosticExam(
            booking_id=json["booking_id"],
            patient_name=json["patient_name"],
            doctor=json["doctor"],
            department=json["department"],
            date=json["date"],
            time=json["time"],
            status=json["status"],
            exam_type=json["exam_type"],
            requires_fasting=json["requires_fasting"]
        )

    if ch.add(booking):
        return jsonify(booking.info()), 201
    return jsonify({"error": "booking already exits"}), 409

@app.route('/bookings/<string:booking_id>', methods=["PUT"])
def update_booking(booking_id: str):
    b = ch.get(booking_id)
    data = request.get_json()

    if b is None:
        return jsonify({"error": "booking not found"}), 404

    if data is None:
        return jsonify({"error": "payload is empty"}), 400

    if data["booking_id"] != booking_id:
        return jsonify({"error": "booking_id must be equal to url"}), 400

    if "type" not in data:
        return jsonify({"error": "missing field type"}), 400

    if data["type"] not in ("visit", "exam"):
        return jsonify({"error": f"type: {data['type']} not valid"}), 400

    common_keys = [
        "booking_id", "patient_name", "doctor", "department", "date", "time", "status"
    ]

    if data["type"] == "visit":
        specific_keys = [
            "visit_reason", "first_time"
        ]
    else:
        specific_keys = [
            "exam_type", "requires_fasting"
        ]

    for k in common_keys + specific_keys:
        if k not in data:
            return jsonify({"error": f"missing field {k}"}), 400

    if data["type"] == "visit":
        booking: MedicalVisit = MedicalVisit(
            booking_id=data["booking_id"],
            patient_name=data["patient_name"],
            doctor=data["doctor"],
            department=data["department"],
            date=data["date"],
            time=data["time"],
            status=data["status"],
            visit_reason=data["visit_reason"],
            first_time=data["first_time"]
        )
    else:
        booking: DiagnosticExam = DiagnosticExam(
            booking_id=data["booking_id"],
            patient_name=data["patient_name"],
            doctor=data["doctor"],
            department=data["department"],
            date=data["date"],
            time=data["time"],
            status=data["status"],
            exam_type=data["exam_type"],
            requires_fasting=data["requires_fasting"]
        )

    ch.update(booking_id, booking)
    return jsonify(booking.info()), 200

@app.route('/bookings/<string:booking_id>/status', methods=["PATCH"])
def patch_status(booking_id: str):
    data = request.get_json()
    d = ch.get(booking_id)
    if d is None:
        return jsonify({"error": "booking not found"}), 404
    if data is None:
        return jsonify({"error": "payload is empty"}), 400
    if "status" not in data:
        return jsonify({"error": "status must appear in payload"})

    if data["status"] not in ("scheduled", "checked_in", "completed", "canceled", "no_show"):
        return jsonify({"error": f"status can not be {data['status']}"}), 400

    ch.patch_status(booking_id, data["status"])
    return jsonify(d.info()), 200

@app.route('/bookings/<string:booking_id>', methods=["DELETE"])
def delete_booking(booking_id: str):
    b = ch.get(booking_id)
    if b is None:
        return jsonify({"error": "booking not found"}), 404
    ch.delete(booking_id)
    return jsonify({"deleted": True, "booking_id": booking_id})

if __name__ == '__main__':
    app.run(debug=True)