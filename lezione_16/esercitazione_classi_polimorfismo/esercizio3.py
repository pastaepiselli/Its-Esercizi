class Veicolo:
    
    def __init__(self, marca: str, modello: str, anno: int) -> None:
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrivi_veicolo(self) -> None:
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}')


class Auto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int) -> None:
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

    def descrivi_veicolo(self) -> None:
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}')

class Moto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, tipo: str) -> None:

        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def descrivi_veicolo(self) -> None:
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}')

