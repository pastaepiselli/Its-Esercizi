class Vehicle:
    def __init__(self) -> None:
        self.speed = 0

class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__()
    def accelerate(self, delta) -> None:
        self.speed += delta