from device import Device

class Laptop(Device):
    def __init__(self, id: str, model: str, customer_name: str , puchase_year: int, status: str, has_dedicated_gpu: bool, screen_size_inches: float) -> None:
        super().__init__(id, model, customer_name, puchase_year, status)
        self.has_dedicated_gpu = has_dedicated_gpu
        self.screen_size_inches = screen_size_inches

    def device_type(self) -> str:
        return "laptop"

    def base_diagnosis_time(self) -> int:
        return 40

    def repair_complexity(self) -> int:
        return 7
    

