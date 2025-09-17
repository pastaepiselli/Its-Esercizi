from dottore import Dottore
from fattura import Fattura
from paziente import Paziente
from persona import Persona

if __name__ == '__main__':

    vernuccio = Dottore('Paolo', 'Vernuccio', 'Pediatra', 35.5)
    garufi = Dottore('Francesco', 'Garufi', 'Ginecologo', 50.5) 

    # Impostare l'età di ogni medico, affinché i due medici risultino validi!

    vernuccio.setAge(45)
    garufi.setAge(53)

    # Il primo medico e il secondo medico si presentano, richiamando il rispettivo metodo doctorGreet().

    vernuccio.doctorGreet()
    garufi.doctorGreet()

    # pazienti
    luca = Paziente('Luca', 'Marchetti', '01')
    pier = Paziente('Pier', 'Damien', '02')
    marco = Paziente('Marco', 'Pierleoni', '03')

    popa = Paziente('Alessandro', 'Popa', '04')

    # Creare un oggetto fattura chiamato fattura1. Alla fattura 1 devono essere associati il dottore_1 e la lista di 3 pazienti.

    fattura1 = Fattura(vernuccio, [luca, pier, marco])

    # Creare un oggetto fattura chiamato fattura2. Alla fattura 2 devono essere associati il dottore_2 e la lista di un solo paziente.

    fattura2 = Fattura(garufi, [popa])

    # Stampare in output il salario di ogni singolo dottore. 

    print(f'Salario dottor {vernuccio.getLastName()}: {fattura1.getSalary()}')
    print(f'Salario dottor {garufi.getLastName()}: {fattura2.getSalary()}')

    # Rimuovere un paziente dalla lista dei pazienti del dottore 1 ed inserire tale paziente nella lista del dottore 2.

    fattura1.removePatient('01')
    fattura2.addPatient(luca)

    # Stampare in output il salario di ogni dottore.

    print('Salari aggiornati...')

    print(f'Salario dottor (aggiornato) {vernuccio.getLastName()}: {fattura1.getSalary()}')
    print(f'Salario dottor (aggiornato) {garufi.getLastName()}: {fattura2.getSalary()}')

    # Stampare in output il guadagno totale incassato dall'ospedale. Il guadagno totale viene calcolato sommando i guadagni di ogni dottore. 

    print(f'In totale, l\'ospedale ha incassato: {fattura1.getSalary() + fattura2.getSalary()}')