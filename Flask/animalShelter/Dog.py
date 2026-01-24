from Animal import Animal

class Dog(Animal):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, breed: str, is_trained: bool) -> None:
        super().__init__(id, name, age_years, weight_kg)
        self.breed = breed
        self.is_trained = is_trained

    def species(self) -> str:
        return "dog"

    def daily_food_grams(self) -> int:
        return 200 + self.age_years * 50
