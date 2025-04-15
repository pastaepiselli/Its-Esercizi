from persona import Persona
from studente import Studente

# creo un oggetto della classe persona

fm: Persona = Persona('Lorenzo', 'Rossi' , 19)

# visualizzare le informazioni relative all'oggetto

print(fm)

# creo un oggetto della classe studente

studente1: Studente = Studente('Alessadro', 'Popa', 13, '')

# visualizzare attributi dell'oggetto studente
# eredita sia gli attributi che i metoodi
print(studente1)

# controlla se studente1 sia istanza della classe Studente
# isinstance(obj, class) -> controlla se l'oggetto obj sia un istanza della classe studente
# ritorna valori booleani

if isinstance(studente1, Studente):

    print('Studente 1 e istanza della classe studente')

if isinstance(studente1, Persona):

    
    print('Studente 1 e un istanza della classe Persona')

# controllo se l'oggetto fm sia istanza della classe persona

if isinstance(fm, Persona):

    print('Fm e un istanza della classe Persona')

# controllo anche se fm e un istanza della classe studente

if isinstance(fm, Studente):

    print('Fm e un istanza della classe studente')

else:

    print('Fm non e un istanza della classe studente')


# controllare che la classe Studente sia sottoclasse di Persona
# issubclss(Class1, Class2) -> controlla che Class1  sia sottoclasse della Classe2
# ritornano valori booleani

if issubclass(Studente, Persona):

    print('La classe studente e sottoclasse della classe persona')
