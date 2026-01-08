from vehicle import Vehicle

class Van(Vehicle):
    def __init__(self,  plate_id: str, model: str, driver_name: str, registration_year: int, status: str, max_load_kg: int, require_special_license: bool) -> None:
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.max_load_kg = max_load_kg
        self.require_special_license = require_special_license

    def vehicle_type(self) -> str:
        return "van"

    def base_cleaning_time(self) -> int:
        return 60

    def wear_level(self):
        return 4