class FormulaError(Exception):
    '''L' input deve essere di tre caratteri es(1 + 1)'''

    
def calculator(user_input: str):

    calc = user_input.split()
    primo_elemento = calc[0]
    operatore = calc[1]
    terzo_elemento = calc[2]
    if len(calc) != 3:

        raise FormulaError('''L' input deve essere di tre caratteri es(1 + 1)''')

    try:
        # controlla se il numero inserito e valido 
        elemento1 = float(primo_elemento)
        elemento2 = float(terzo_elemento)
    
    except ValueError:  

        raise FormulaError
    
    if operatore == '+':
        sum = elemento1 + elemento2
        return sum
    elif operatore == '-':
        sotr = elemento1 - elemento2
        return sotr
    else:

        raise FormulaError('Inserire + o -')

def interactive_calculator():
    run: bool = True
    while run:
        equation = str(input('Inserire calcolo: '))
        print(calculator(equation))
        print('Vuoi inserire un altro calcolo?: Yes / Quit')
        scelta = str(input(''))
        if scelta.lower() == 'yes':
            continue
        elif scelta.lower() == 'quit':
            run = False
        else:

            raise ValueError("Expected Yes / Quit")


import unittest

class TestCalculator(unittest.TestCase):

    def test_addizione(self):

        self.assertEqual(calculator('2 + 3'), 5.0)

    def test_sottrazione(self):

        self.assertEqual(calculator('10 - 3'), 7.0)

    def test_operatore_sbagliato(self):

        with self.assertRaises(FormulaError):

            calculator('1 piu 2')


if __name__ == '__main__':

    unittest.main()
