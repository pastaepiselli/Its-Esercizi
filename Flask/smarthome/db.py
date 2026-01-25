from IoTHub import IoTHub
from SecurityCamera import SecurityCamera
from SmartBulb import SmartBulb

hub: IoTHub = IoTHub()

camera = SecurityCamera(
    serial_number="CAM123456",
    brand="Hikvision",
    room="Ingresso",
    installation_year=2023,
    status="active",
    resolution="4K",
    night_vision=True
)

bulb = SmartBulb(
    serial_number="BULB987654",
    brand="Philips",
    room="Soggiorno",
    installation_year=2024,
    status="on",
    brightness_lumens=800,
    color_capability=True
)

hub.add(camera)
hub.add(bulb)

