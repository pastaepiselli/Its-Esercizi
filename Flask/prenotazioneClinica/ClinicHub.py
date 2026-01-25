from Booking import Booking

class ClinicHub:
    def __init__(self):
        self.bookings = {}

    def add(self, booking: Booking) -> bool:
        if booking.booking_id in self.bookings:
            return False
        self.bookings[booking.booking_id] = booking
        return True

    def get(self, booking_id: str) -> Booking | None:
        return self.bookings[booking_id]

    def update(self, booking_id: str, booking: Booking) -> None:
        if booking_id in self.bookings:
            self.bookings[booking_id] = booking

    def patch_status(self, booking_id: str, new_status: str) -> None:
        self.bookings[booking_id].status = new_status

    def delete(self, booking_id: str) -> bool:
        if booking_id in self.bookings:
            del self.bookings[booking_id]
            return True
        return False

    def list_all(self) -> list[dict[str, int | str | bool | float]]:
        return [b.info() for b in self.bookings.values()]
