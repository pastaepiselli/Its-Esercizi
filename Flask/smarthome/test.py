import requests
import json


headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }



URL = 'http://localhost:5000'

def _show_response(response: requests.Response, n:int = 1):
    print(f"\n\n{"=" * 10} TEST {n} - {response.request.method} {response.url} {"=" * 10}")
    print(f"\nRESPONSE:\n"
          f"- HTTP Status Code: {response.status_code}\n"
          f"- JSON CONTENT:")
    print(json.dumps(response.json(), indent=4))

def test_home():
    response = requests.get(url=URL, headers=headers)
    _show_response(response, 1)

def test_get_all_devices():
    response = requests.get(url=URL + '/devices', headers=headers)
    _show_response(response, 2)

def test_get_device(serial_number: str):
    response = requests.get(url=URL + f'/devices/{serial_number}', headers=headers)
    _show_response(response, 3)

def test_diagnostic_time(serial_number: str, factor: float):
    response = requests.get(url=URL + f'/devices/{serial_number}/diagnostic/{factor}')
    _show_response(response, 4)

def test_add_device():
    response = requests.post(url=URL + '/devices', headers=headers, json={
  "type": "camera",
  "serial_number": "SN-3e67",
  "brand": "Philips",
  "room": "Living Room",
  "installation_year": 2022,
  "status": "online",
  "resolution": 3,
  "night_vision": True
})
    _show_response(response, 5)

def test_update_device(serial_number: str):
    response = requests.put(url=URL + f'/devices/{serial_number}', headers=headers, json={
    "type": "bulb",
    "serial_number": serial_number,
    "brand": "IKEA",
    "room": "Camera da letto",
    "installation_year": 2021,
    "status": "off",
    "brightness_lumens": 470,
    "color_capability": False
})
    _show_response(response, 6)

def test_patch_status(serial_number: str):
    response = requests.patch(url=URL + f'/devices/{serial_number}/status', headers=headers, json={
        "status": "online"
    })
    _show_response(response, 7)

def test_delete(serial_number: str):
    response = requests.delete(url=URL + f'/devices/{serial_number}', headers=headers)
    _show_response(response, 8)
if __name__ == "__main__":
    test_home()
    test_get_all_devices()
    test_get_device("BULB987654")
    test_diagnostic_time("BULB987654", 1.5)
    test_add_device()
    test_update_device("BULB987654")
    test_patch_status("BULB987654")
    test_delete("CAM123456")