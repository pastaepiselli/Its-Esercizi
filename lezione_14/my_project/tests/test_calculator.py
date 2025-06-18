from my_project.calculator import Calculator
import pytest

# def test_addition():
#     calculation: Calculator = Calculator(10, 5)
#     assert calculation.addition() == 13, 'The sum is wrong'

# def test_subtraction():
#     calculation: Calculator = Calculator(10, 5)
#     assert calculation.subtraction() == 5, 'The subtraction is wrong'

# def test_multiplication():
#     calculation: Calculator = Calculator(10, 5)
#     assert calculation.multiplication() == 50, 'The multiplication is wrong'

# def test_division():
#     calculation: Calculator = Calculator(10, 5)
#     assert calculation.division() == 2.00, 'The division is wrong'    
    

# per rendere questo codice piu comodo e leggibile usiamo i decorator di pytest

@pytest.fixture

def calculation():
    # crea un istanza della classe calcolatrice
    return Calculator(10, 5)

def test_addition(calculation: Calculator):
    assert calculation.addition() == 13, 'The sum is wrong'

def test_subtraction(calculation: Calculator):
    assert calculation.subtraction() == 5, 'The subtraction is wrong'

def test_multiplication(calculation: Calculator):
    assert calculation.multiplication() == 50, 'The multiplication is wrong'

def test_division(calculation: Calculator):
    assert calculation.division() == 2.00, 'The division is wrong'

