import string

class Documento:

    text: str

    def __init__(self, text: str) -> None:
        
        self.setText(text)

    def getText(self) -> str:
        return self.text

    def setText(self, text) -> None:
        self.text = text

    def isInText(self, word: str) -> bool:
        # creo un transaltore con maketrans, e dico di sostituire con spazi tutta la punteggiatura
        translator = str.maketrans('', '', string.punctuation)

        # salvo il testo senza punteggiatura
        no_puntc_text = self.getText().translate(translator)

        if word in no_puntc_text.split():
            return True

        return False



class Email(Documento):

    mittente: str
    destinatario: str
    titolo_messaggio: str

    def __init__(self, text: str, mittente: str, destinatario: str, titolo_messaggio: str) -> None:

        super().__init__(text)
        self.setMittente(mittente)
        self.setDestinatario(destinatario)
        self.setTitolo(titolo_messaggio)

    # ridefinisco il metodo getText

    def getText(self) -> str:
        return f'Da: {self.getMittente()}\nTitolo: {self.getTitolo()}\nMessaggio: {super().getText()}'
    
    # MITTENTE

    def getMittente(self) -> str:
        return self.mittente

    def setMittente(self, mittente: str) -> None:
        self.mittente = mittente
    
    # DESTINATARIO

    def getDestinatario(self) -> str:
        return self.destinatario

    def setDestinatario(self, destinatario: str) -> None:
        self.destinatario = destinatario
    
    # TITOLO_MESSAGGIO

    def getTitolo(self) -> str:
        return self.titolo_messaggio
    
    def setTitolo(self, titolo_messaggio: str) -> None:
        self.titolo_messaggio = titolo_messaggio

    def writeToFile(self,percorso: str) -> None:

        try:
            with open(percorso, 'w') as f:
                f.write(self.getText())
        except FileExistsError:
            print('Il file e gia esistente')



class File(Documento):

    nome_percorso: str
    text: str

    def __init__(self, nome_percorso: str) -> None:
        self.nome_percorso = nome_percorso
        super().__init__(text=self.leggiTestoDaFile())
       

    def leggiTestoDaFile(self) -> str:
        with open(self.getNomePercorso(), 'r') as f:
            testo = f.read()

        return testo
    
    def getNomePercorso(self) -> str:
        return self.nome_percorso

    def getText(self) -> str:
        return f'Percorso: {self.getNomePercorso()}\nContenuto: {super().getText()}'
              
if __name__ == '__main__':

    # Email: Viene creato un oggetto Email con mittente, destinatario, oggetto e corpo del messaggio.
    popa: Email = Email(mittente='alessando', destinatario='lorenzo', titolo_messaggio='LA MIA GITA A TORINO', text='ciao sto a torino e mi diverto dobbiamo incontrarci')

    # File: Viene creato un oggetto File specificando il percorso di un file esistente.
    popa_file: File = File(nome_percorso='lezione_21/testi_digitali/document.txt')

    # Stampa del testo dell'email: Viene stampato il testo del messaggio dell'email utilizzando il metodo getText().

    print(popa.getText())

    # Stampa del testo del file: Viene stampato il contenuto del file utilizzando il metodo getText().
    
    print(popa_file.getText())

        
    # Scrittura su file: Il contenuto dell'email viene scritto su un nuovo file chiamato email1.txt utilizzando il metodo writeToFile()
    
    popa.writeToFile('email1.txt')

    """
    Verifica della presenza di parole chiave:
    Email: Utilizzo del metodo isInText() per verificare se la parola 'incontrarci' è presente nel testo dell'email. Il risultato atteso è True.
    File: Utilizzo del metodo isInText() per verificare se la parola 'percorso' è presente nel testo del file. Il risultato atteso è False.
    """
    print(popa.isInText('incontrarci'))   
    print(popa.isInText('percorso'))   