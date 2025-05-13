from persona2 import Persona
from alieno import Alieno


#creare un oggetto della classe persona
p: Persona = Persona('Lorenzo' ,'Rossi', 19)

# visualizzare le informazioni dell'oggetto p classe persona
print(p)


# creare oggetto della classe alieno
et: Alieno = Alieno("Andromeda")

# visualizzare le informazioni dell'oggetto et 
print('\n', et)

# invocare il metodo speak() della classe persona

p.speak()
print('\n')

# invocare il metodo speak() di un alieno

et.speak()