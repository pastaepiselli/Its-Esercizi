import pygame
from turtle import Turtle

width: int = 1000
height: int = 900

BLOCK_WIDTH = 40
BLOCK_HEIGHT = 40
GRID_WIDTH = BLOCK_WIDTH * 70

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
run: bool = True
turtle = Turtle()
while run:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run: bool = False
            
    pygame.display.update()
    turtle.draw()
    clock.tick(60)
pygame.quit()