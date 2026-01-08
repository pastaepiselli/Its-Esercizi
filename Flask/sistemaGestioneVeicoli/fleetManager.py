from vehicle import Vehicle

class FleetManager:
    def __init__(self) -> None:
        self.vehicles = {}

    def add(self, vehicle: Vehicle) -> bool:
        if vehicle.plate_id in self.vehicles:
            return False

        self.vehicles[vehicle.plate_id] = vehicle
        return True

    def get(self, plate_id: str) -> Vehicle | None:
        if plate_id in self.vehicles:
            return self.vehicles[plate_id]
        return None

    def update(self, plate_id: str, new_vehicle: Vehicle) -> None:
        if plate_id in self.vehicles:
            del self.vehicles[plate_id]
            self.vehicles[new_vehicle.plate_id] = new_vehicle
        else:
            self.vehicles[new_vehicle.plate_id] = new_vehicle

    def patch_status(self, plate_id: str, new_status: str) -> None:
        if plate_id in self.vehicles:
            self.vehicles[plate_id].setStatus(new_status)

    def delete(self, plate_id: str) -> bool:
        if plate_id in self.vehicles:
            del self.vehicles[plate_id]
            return True
        return False

    def list_all(self):
        return [x.info() for x in self.vehicles.values()]

