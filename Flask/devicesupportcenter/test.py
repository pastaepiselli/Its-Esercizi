import requests
# va installato con 'pip install requests'

import json

headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }

URL = "http://localhost:5000/"

# funzione per formattazione carina
def _show_response(response: requests.Response, n:int = 1):
    print(f"\n\n{"=" * 10} TEST {n} - {response.request.method} {response.url} {"=" * 10}")
    print(f"\nRESPONSE:\n"
          f"- HTTP Status Code: {response.status_code}\n"
          f"- JSON CONTENT:")
    print(json.dumps(response.json(), indent=4))


# inizio test
def test_home():
    response = requests.get(URL, headers=headers)
    _show_response(response, 1)
def test_get_all_devices():
    response = requests.get(url=URL + '/devices', headers=headers)
    _show_response(response, 2)

def test_get_device(device_id: str):
    response = requests.get(url=URL + f'/devices/{device_id}', headers=headers)
    _show_response(response, 3)

def test_get_estimated_time_device(device_id: str, factor: float = 1.0):
    response = requests.get(url=URL + f'/devices/{device_id}/estimate/{factor}', headers=headers)
    _show_response(response, 4)

# post

def test_add_device():
    response = requests.post(URL + '/devices', headers=headers, json={
  "type": "smartphone",
  "id": "d3",
  "model": "Galaxy S21",
  "customer_name": "Mario Rossi",
  "purchase_year": 2021,
  "status": "received",
  "has_protective_case": True,
  "storage_gb": 128
})
    _show_response(response, 5)


# put

def test_put_device(device_id: str):
    response = requests.put(url=URL + f'/devices/{device_id}', json={
  "type": "laptop",
  "id": "LAP123",
  "model": "Dell XPS 15",
  "customer_name": "Mario Rossi",
  "purchase_year": 2021,
  "status": "in_repair",
  "has_dedicated_gpu": True,
  "screen_size_inches": 15.6
})
    _show_response(response, 6)

def test_patch_status(device_id: str):
    response = requests.patch(URL + f'/devices/{device_id}/status', headers=headers, json={
        "status": "repairing"
    })
    _show_response(response, 7)

def test_delete(device_id: str):
    response = requests.delete(url=URL + f'/devices/{device_id}', headers=headers)
    _show_response(response, 7)

if __name__ == "__main__":
    test_home()
    test_get_all_devices()
    test_get_device('s1')
    test_get_estimated_time_device("s1", 40.0)
    test_add_device()
    test_put_device('s1')
    test_get_device('s1')
    test_patch_status('l1')
    test_delete('l1')



