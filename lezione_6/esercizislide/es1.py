class Person:
 def __init__(self, name, age):
   self.name = name
   self.age = age
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

# if alice.age > bob.age:
#   print(alice.name)
# else:
#   print(bob.name)
  
pier = Person("Pier.D", 19)
luca = Person("Luca.M", 20)
popa = Person("Alessando.P", 20)

persons: list[Person] = [pier, luca, popa, bob, alice]

current = persons[0]

for item in persons:
  if item.age < current.age:
    current = item
print(current.name)
    

  
  
  
  