from Animal import Animal

class Shelter:
    def __init__(self):
        self.animals = {}
        self.adoptions = {}

    def add(self, animal: Animal) -> bool:
        if animal.id in self.animals:
            # animale gia presente
            return False

        self.animals[animal.id] = animal
        return True

    def get(self, animal_id: str) -> Animal | None:
        if animal_id in self.animals:
            return self.animals[animal_id]
        return  None

    def list_all(self):
        # restitusce un a lista con tutti gli oggetti Animal
        return [a for a in self.animals.values()]

    def is_adopted(self, animal_id: str) -> None:
        if animal_id in self.adoptions:
            return True
        return False

    def set_adopted(self, animal_id: str, adopter_name: str) -> None:
        self.adoptions[animal_id] = adopter_name
