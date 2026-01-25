from abc import ABC, abstractmethod
class Booking(ABC):
    def __init__(self, booking_id: str, patient_name: str, doctor: str, department: str, date: str, time: str, status: str) -> None:
        self.booking_id = booking_id
        self.patient_name = patient_name
        self.doctor = doctor
        self.department = department
        self.date = date
        self.time = time
        self.status = status

    @abstractmethod
    def booking_type(self) -> str:
        pass

    @abstractmethod
    def base_duration(self) -> int:
        pass

    @abstractmethod
    def priority_level(self) -> int:
        pass

    def info(self) -> dict[str, int | str | bool | float]:
        return self.__dict__

    def estimated_wait(self, factor:float = 1.0) -> int:
        return int(self.base_duration() * factor + self.priority_level() * 5)