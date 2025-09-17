from persona import Persona

class Dottore(Persona):
    __first_name: str
    __last_name: str
    __age: int
    __specialization: str
    __parcel: float
    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float) -> None:
        super().__init__(first_name, last_name)
        self.setSpecialization(specialization)
        self.setParcel(parcel)

    def setSpecialization(self, specialization: str) -> None:
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            self.__specialization = None
            print("La specializzazione inserita non è una stringa!")

    def setParcel(self, parcel: float) -> None:
        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            self.__parcel = None
            print("La parcella inserita non è un float!")

    def getSpecialiaziation(self) -> str:
        return self.__specialization

    def getParcel(self) -> float:
        return self.__parcel

    def isAValidDoctor(self) -> bool:
        if self.getAge() > 30:
            print(f'Doctor {self.getName()} {self.getLastName()} is valid!')
            return True
        print(f'Doctor {self.getName()} {self.getLastName()} is not valid!')
        return False

    def doctorGreet(self) -> None:
        self.greet()
        print(f'Sono un medico {self.getSpecialiaziation()}')

if __name__ == '__main__':
    coleman = Dottore('Alessandro', 'Colella', 'Pediatra', 124.70)
    print(coleman.getAge())
    coleman.isAValidDoctor()
    coleman.setAge(31)
    coleman.isAValidDoctor()
    coleman.doctorGreet()