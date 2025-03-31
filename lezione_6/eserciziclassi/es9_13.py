import random
class Dice:

    def __init__(self, sides = 6):

        self.sides = sides

    def roll_die(self):

        print(random.randint(1, self.sides))

        

#dado 6 facce
dado6 = Dice()
for i in range(0, 10):
    dado6.roll_die()

#dado 10 facce
dado10 = Dice(10)
for i in range(0, 10):
    dado10.roll_die()

#dado 20 facce
dado20 = Dice(20)
for i in range(0, 10):
    dado20.roll_die()

        