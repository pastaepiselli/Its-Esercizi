class Persona:

    __first_name: str
    __last_name: str
    __age: int

    def __init__(self, first_name: str, last_name: str) -> None:
        self.setName(first_name)
        self.setLastName(last_name)

        # se first_name e last_name non sono due stringhe, allora assegnare None all'età.
        if self.__first_name == None and self.__last_name == None:
            self.__age = None
        else:
            self.__age = 0
    
    def setName(self, first_name: str) -> None:
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            self.__first_name = None
            print("Il nome inserito non è una stringa!")

    def setLastName(self, last_name: str) -> None:
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            self.__last_name = None
            print("Il cognome inserito non è una stringa!")

    def setAge(self, age: int) -> None:
        if isinstance(age, int):
            self.__age = age
        else:
            print("L'età deve essere un numero intero!")

    def getName(self) -> str:
        return self.__first_name

    def getLastName(self) -> str:
        return self.__last_name

    def getAge(self) -> int:
        return self.__age

    def greet(self) -> None:
        print(f'Ciao, sono {self.getName()} {self.getLastName()}! Ho {self.getAge()} anni!')


popa = Persona('Alessando', 'Popa')
if __name__ == '__main__':
    print(popa.getName())
    print(popa.getLastName())
    print(popa.getAge())
    popa.setAge(21)
    print(popa.getAge())
    popa.setName(5)
    popa.setLastName(6)
    print(popa.getAge())
            


