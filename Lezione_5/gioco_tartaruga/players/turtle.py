from Lezione_5.gioco_tartaruga.tartarugagame import *
import pygame
class Turtle:
    def __init__(self):
        self.grid_x = 5
        self.grid_y = 5

    def move(self, direction):
        if direction == "RIGHT" and self.grid_x < width // BLOCK_WIDTH - 1:
            self.grid_x += 1
        elif direction == "LEFT" and self.grid_x > 0:
            self.grid_x -= 1
        elif direction == "DOWN" and self.grid_y < height // BLOCK_HEIGHT - 1:
            self.grid_y += 1
        elif direction == "UP" and self.grid_y > 0:
            self.grid_y -= 1

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.grid_x * BLOCK_WIDTH, self.grid_y * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT))

