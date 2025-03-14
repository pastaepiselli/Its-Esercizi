from classepersona import Persona



persona_1: Persona = Persona("Mario", "Rossi", 30)


def esempio(input_1: Persona):

    print(input_1.get_nome())
    print(input_1.get_password())
    print(input_1.stipendio)