from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self,  plate_id: str, model: str, driver_name: str, registration_year: int, status: str, doors: int, is_cabrio: bool) -> None:
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.doors = doors
        self.is_cabrio = is_cabrio

    def vehicle_type(self) -> str:
        return "car"

    def base_cleaning_time(self) -> int:
        return 30

    def wear_level(self):
        return 2

