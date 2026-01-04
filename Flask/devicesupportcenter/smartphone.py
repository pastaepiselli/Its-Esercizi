from device import Device

class Smartphone(Device):
    def __init__(self, id: str, model: str, customer_name: str, purchase_year: int, status: str, has_protective_case: bool, storage_gb: int):
        super().__init__(id, model, customer_name, purchase_year, status)
        self.has_protective_case = has_protective_case
        self.storage_gb = storage_gb

    def device_type(self) -> str:
        return "smartphone"

    def base_diagnosis_time(self) -> int:
        return 20

    def repair_complexity(self) -> int:
        return 2

    