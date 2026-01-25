from Booking import Booking
class MedicalVisit(Booking):
    def __init__(self,  booking_id: str, patient_name: str, doctor: str, department: str, date: str, time: str, status: str, visit_reason: str, first_time: bool) -> None:
        super().__init__(booking_id, patient_name, doctor, department, date, time, status)
        self.visit_reason = visit_reason
        self.first_time = first_time

    def booking_type(self) -> str:
        return "visit"

    def base_duration(self) -> int:
        return 20

    def priority_level(self) -> int:
        reason = (self.visit_reason or "").lower()
        keywords = ["urgente", "dolore", "acuto", "svenimento"]
        for k in keywords:
            if k in reason:
                return 7
        return 5
    