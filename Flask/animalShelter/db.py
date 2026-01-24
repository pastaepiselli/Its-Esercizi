from Shelter import Shelter
from Dog import Dog
from Cat import Cat

# creo shelter
s: Shelter = Shelter()

# un gatto e un cane
c1: Cat = Cat("c1", "Nina", 5, 3.4, False, "ball")
d1: Dog = Dog("d1", "Milo", 5, 6.4, "Shitzu", False)

# aggiungo animali a shelter
s.add(c1)
s.add(d1)

