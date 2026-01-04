from device import Device

class ServiceCenter:
    def __init__(self):
        self.devices = {}

    def add(self, device: Device) -> bool:
        if device.id in self.devices:
            return False

        self.devices[device.id] = device
        return True

    def get(self, device_id: str) -> Device | None:
        if device_id in self.devices:
            return self.devices[device_id]
        return None

    # per simulare un put
    def update(self, device_id: str, new_device: Device) -> None:
        if device_id in self.devices:
            del self.devices[device_id]
            self.devices[new_device.id] = new_device

        # capire cosa fare quando nn valido

    def patch_status(self, device_id: str, new_status: str) -> None:
        if device_id in self.devices:
            self.devices[device_id].status = new_status

        # capire cosa fare quando nn valido

    def delete(self, device_id: str) -> bool:
        if device_id in self.devices:
            del self.devices[device_id]
            return True
        return False

    def list_all(self) -> list:
        return [x.info() for x in self.devices.values()]
