import datetime

class Pagamento():

    __importo: float

    def __init__(self) -> None:
        self.__importo = 0

    def getImporto(self) -> float:
        return self.__importo

    def setImporto(self, importo: float) -> None:
        self.__importo = importo

    def dettagliPagamento(self) -> None:
        print(f'Importo del pagamento: €{round(self.getImporto(), 2)}')


class PagamentoContanti(Pagamento):

    def __init__(self) -> None:
        super().__init__()
    
    def dettagliPagamento(self) -> None:
        print(f'Importo del pagamento in contanti: €{self.getImporto():.2f}')

    def pezziDa(self) -> None:
        importo = self.getImporto()
        pezzi = [
            (500, "banconota"),
            (200, "banconota"),
            (100, "banconota"),
            (50, "banconota"),
            (20, "banconota"),
            (10, "banconota"),
            (5, "banconota"),
            (2, "moneta"),
            (1, "moneta"),
            (0.5, "moneta"),
            (0.2, "moneta"),
            (0.1, "moneta"),
            (0.05, "moneta"),
            (0.01, "moneta"),
        ]
        resto = round(importo, 2)

        for valore, tipo in pezzi:
            conteggio = int(resto // valore)
            if conteggio > 0:
                print(f"{conteggio} {tipo}{'e' if conteggio > 1 else ''} da {valore} euro.")
                resto = round(resto - conteggio * valore, 2)
        
class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, nome_titolare: str, data_scadenza: datetime, num_carta: int):
        super().__init__()
        self.__nome_titolare = nome_titolare
        self.__data_scadenza = data_scadenza
        self.__num_carta = num_carta

    def getNome(self) -> str:
        return self.__nome_titolare

    def getScadenza(self) -> datetime:
        return self.__data_scadenza

    def getNumCarta(self) -> int:
        return self.__num_carta

    def dettagliPagamento(self) -> None:
        print(f'Pagamento di {self.getImporto()} effetuato con la carta di credito')
        print(f'Nome sulla carta:{self.getNome()}')
        print(f'Data di scadenza: {self.getScadenza()}')
        print(f'Numero sulla carta: {self.getNumCarta()}')




if __name__ == '__main__':
    telefono = PagamentoContanti()
    telefono.setImporto(750.50)
    telefono.dettagliPagamento()
    telefono.pezziDa()

    cassaperoni = PagamentoContanti()
    cassaperoni.setImporto(24.50)
    cassaperoni.dettagliPagamento()
    cassaperoni.pezziDa()


    

    

        
