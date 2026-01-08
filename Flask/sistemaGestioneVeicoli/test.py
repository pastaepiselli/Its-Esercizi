import json
import requests

from Flask.sistemaGestioneVeicoli.main import get_vehicles

BASE_URL = "http://localhost:5000"

def print_response(title, response):
    print(f"=== {title} ===")
    print("Status code:", response.status_code)
    try:
        data = response.json()
        print("JSON response:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except ValueError:
        print("Raw response:")
        print(response.text)
    print("=" * 40)

if __name__ == "__main__":
    headers = {
        "Content-type": "application/json",
        "Accept": "application/json"
    }

    # test '/'
    index = requests.get(BASE_URL, headers=headers)
    print_response("index", index)

    # test '/vehicles'
    all_vehicles = requests.get(BASE_URL+"/vehicles", headers=headers)
    print_response("/vehicles", all_vehicles)

    # test '/vehicles/<string:plate_id> (esistente)
    get_vehicle = requests.get(BASE_URL+"/vehicles/BG123AE", headers=headers)
    print_response("/vehicles/BG123AE", get_vehicle)

    # test '/vehicles/YH243UR' (non esistente)
    get_vehicle = requests.get(BASE_URL+"/vehicles/YH243UR")
    print_response("/vehicles/YH243UR", get_vehicle)