import requests
import json

BASE_URL = "http://localhost:5000"
headers = {
    "Content-type": "application/json",
    "Accept": "application/json"
}

def _show_response(response: requests.Response, n:int = 1):
    print(f"\n\n{"=" * 10} TEST {n} - {response.request.method} {response.url} {"=" * 10}")
    print(f"\nRESPONSE:\n"
          f"- HTTP Status Code: {response.status_code}\n"
          f"- JSON CONTENT:")
    print(json.dumps(response.json(), indent=4))

def test_home():
    response = requests.get(url=BASE_URL, headers=headers)
    _show_response(response, 1)

def test_get_all_bookings():
    response = requests.get(url=BASE_URL + '/bookings', headers=headers)
    _show_response(response, 2)

def test_get_booking(booking_id: str):
    response = requests.get(url=BASE_URL + f'/bookings/{booking_id}', headers=headers)
    _show_response(response, 3)

def test_estimate_time(booking_id: str, factor: float):
    response = requests.get(url=BASE_URL + f'/bookings/{booking_id}/wait/{factor}')
    _show_response(response, 4)

def test_add_booking():
    response = requests.post(url=BASE_URL + '/bookings', headers=headers, json=None)
    _show_response(response, 5)

def test_update_booking(booking_id: str):
    response = requests.put(url=BASE_URL + f'/bookings/{booking_id}', headers=headers, json={
            "type": "visit",
            "booking_id": booking_id,
            "patient_name": "Mario Rossi",
            "doctor": "Dr. Bianchi",
            "department": "Cardiologia",
            "date": "2026-03-01",
            "time": "10:45",
            "status": "checked_in",
            "visit_reason": "Controllo cardiologico",
            "first_time": False
    })
    _show_response(response, 6)

def test_delete(booking_id: str):
    response = requests.delete(url=BASE_URL + f'/bookings/{booking_id}', headers=headers)
    _show_response(response, 7)
if __name__ == "__main__":
    test_home()
    test_get_all_bookings()
    test_get_booking("BK-101")
    test_estimate_time("BK-101", 2.5)
    test_add_booking()
    test_update_booking("BK-102")
    test_delete("BK-102")


