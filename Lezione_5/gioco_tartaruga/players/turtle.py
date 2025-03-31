import random
import pygame

class Turtle:
    def __init__(self):

        self.movement_opportunity = random.randint(1, 10)

    def move(self):

        match self.movement_opportunity:

            case 1 | 2 | 3 | 4 | 5:


        