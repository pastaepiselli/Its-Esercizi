from SmartDevice import SmartDevice
class SmartBulb(SmartDevice):
    def __init__(self, serial_number: str, brand: str, room: str, installation_year: int, status: str, brightness_lumens: int, color_capability: bool) -> None:
        super().__init__(serial_number, brand, room, installation_year, status)
        self.brightness_lumens = brightness_lumens
        self.color_capability = color_capability

    def device_type(self) -> str:
        return "bulb"

    def energy_consumption(self) -> float | int:
        return 10

    def connection_quality(self) -> int:
        return 2
