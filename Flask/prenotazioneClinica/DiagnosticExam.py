from Booking import Booking
class DiagnosticExam(Booking):
    def __init__(self,  booking_id: str, patient_name: str, doctor: str, department: str, date: str, time: str, status: str, exam_type: str, requires_fasting: bool) -> None:
        super().__init__(booking_id, patient_name, doctor, department, date, time, status)
        self.exam_type = exam_type
        self.requires_fasting = requires_fasting

    def booking_type(self) -> str:
        return "exam"

    def base_duration(self) -> int:
        return 15

    def priority_level(self) -> int:
        et = (self.exam_type or "").strip().lower()
        if et in ["rmn", "mri", "tac", "ct"]:
            return 8
        return 7