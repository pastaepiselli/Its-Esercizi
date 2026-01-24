import requests
import json

URL = "http://localhost:5000"

headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }

def _show_response(response: requests.Response, n:int = 1):
    print(f"\n\n{"=" * 10} TEST {n} - {response.request.method} {response.url} {"=" * 10}")
    print(f"\nRESPONSE:\n"
          f"- HTTP Status Code: {response.status_code}\n"
          f"- JSON CONTENT:")
    print(json.dumps(response.json(), indent=4))


def test_get_index():
    response = requests.get(url=URL, headers=headers)
    _show_response(response, 1)

def test_get_all_vehicles():
    response = requests.get(url=URL + '/vehicles', headers=headers)
    _show_response(response, 2)

def test_get_vehicle(plate_id: str):
    response = requests.get(url=URL + f'/vehicles/{plate_id}', headers=headers)
    _show_response(response, 3)

def test_estimated_prep_time(plate_id: str, factor: float = 1.0):
    response = requests.get(url=URL + f'/vehicles/{plate_id}/prep-time/{factor}')
    _show_response(response, 4)

def test_add_vehicle():
    response= requests.post(url=URL + '/vehicles', headers=headers, json={
  "type": "car",
  "plate_id": "XX999YY",
  "model": "Fiat 500 Cabrio",
  "driver_name": "Mario Rossi",
  "registration_year": 2022,
  "status": "available",
  "doors": 3,
  "is_cabrio": True
})
    _show_response(response, 5)

def test_update_vehicle(plate_id: str):
    response = requests.put(url=URL + f'/vehicles/{plate_id}', headers=headers, json={
  "plate_id": plate_id,
  "type": "van",
  "model": "Ford Transit",
  "driver_name": "Luigi Bianchi",
  "registration_year": 2018,
  "status": "active",
  "max_load_kg": 1200,
  "require_special_license": True
}
)
    _show_response(response, 6)

def test_update_status(plate_id: str):
    response = requests.patch(url=URL + f'/vehicles/{plate_id}/status', headers=headers, json={
        "status": "cleaning"
    })
    _show_response(response, 7)

def test_delete_vehicle(plate_id: str):
    response = requests.delete(url=URL + f'/vehicles/{plate_id}', headers=headers)
    _show_response(response, 8)
if __name__ == "__main__":
    test_get_index()
    test_get_all_vehicles()
    test_get_vehicle("BG123AE")
    test_estimated_prep_time("BG123AE", 1.0)
    test_add_vehicle()
    test_update_vehicle("PR234BJ")
    test_update_status("BG123AE")
    test_delete_vehicle("BG123AE")
