from persona import Persona

class Paziente(Persona):

    __idCode: str

    def __init__(self, first_name: str, last_name: str, idCode: str) -> None:
        super().__init__(first_name, last_name)
        self.setIdCode(idCode)

    def setIdCode(self, idCode) -> None:
        self.__idCode = idCode

    def getIdCode(self) -> str: 
        return self.__idCode

    def patientInfo(self) -> None:
        print(f'Paziente: {self.getName()} {self.getLastName()}')
        print(f'ID:{self.getIdCode()}')

if __name__ == '__main__':
    pier = Paziente('Pier', 'Damien', '0204')
    print(pier.getName())
    print(pier.getIdCode())
    pier.patientInfo()