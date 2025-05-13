from abc import ABC, abstractmethod
class FormaGenerica(ABC):

    # da questo metodo indichiamo che non ci aspettiamo che forma generica generi qualcosa ma le sottoclassi di essa
    @abstractmethod
    def draw(self) -> None:
        pass

    def setShape(self, shape: str) -> None:

        if shape:

            self.shape = shape

        else:

            print('Shape non puo essere una stringa vuota.')

    def getShape(self) -> str:

        return self.shape
        


