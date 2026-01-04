from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, id: str, model: str, customer_name: str, purchase_year: int, status: str) -> None:
        self.id = id
        self.model = model
        self.customer_name = customer_name
        self.purchase_year = purchase_year
        self.status = status

    @abstractmethod
    def device_type(self) -> str:
        pass

    @abstractmethod
    def base_diagnosis_time(self) -> int:
        pass

    @abstractmethod
    def repair_complexity(self) -> int:
        pass

    def info(self) -> dict[str, str | int]:
        return  self.__dict__

    def estimated_total_time(self, factor: float=1.0) -> int:
        return int(self.base_diagnosis_time() * factor + self.repair_complexity() * 30)