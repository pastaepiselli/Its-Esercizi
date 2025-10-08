import pygame
import random
width = 1000
height = 800
BLOCK_HEIGHT = 40
BLOCK_WIDTH = 40
run = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TARTARUGA VS LEPRE')

turtle_image = pygame.transform.scale(pygame.image.load('Lezione_5/gioco_tartaruga/assets/tartaruga.jpg'), (40 ,40))
turtle_image.set_colorkey(('grey'))
lepre_image = pygame.transform.scale(pygame.image.load('Lezione_5/gioco_tartaruga/assets/hare.jpg'), (40, 40)) 
lepre_image.set_colorkey((255, 255, 255))
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
        screen.blit(turtle_image, ((self.grid_x * BLOCK_WIDTH, self.grid_y * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)))

turtle = Turtle()

class Lepre:

    def __init__(self):
        self.grid_x = 3
        self.grid_y = 3
    
    def move(self, direction):

        if direction == "RIGHT" and self.grid_x < width // BLOCK_WIDTH - 1:
            self.grid_x += random.randint(1, 5)
        elif direction == "LEFT" and self.grid_x > 0:
            self.grid_x -= random.randint(1, 5)
        elif direction == "DOWN" and self.grid_y < height // BLOCK_HEIGHT - 1:
            self.grid_y += random.randint(1, 5)
        elif direction == "UP" and self.grid_y > 0:
            self.grid_y -= random.randint(1, 5)

        self.grid_x = max(0, min(self.grid_x, width // BLOCK_WIDTH - 1))
        self.grid_y = max(0, min(self.grid_y, height // BLOCK_HEIGHT - 1))

    def draw(self):
         screen.blit(lepre_image, ((self.grid_x * BLOCK_WIDTH, self.grid_y * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)))

lepre = Lepre()
        

while run:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                turtle.move("RIGHT")
            elif event.key == pygame.K_LEFT:
                turtle.move("LEFT")
            elif event.key == pygame.K_DOWN:
                turtle.move("DOWN")
            elif event.key == pygame.K_UP:
                turtle.move("UP")
            
            if event.key == pygame.K_h:
                lepre.move("RIGHT")
            elif event.key == pygame.K_a:
                lepre.move("LEFT")
            elif event.key == pygame.K_s:
                lepre.move("DOWN")
            elif event.key == pygame.K_d:
                lepre.move("UP")
            
        


            

    screen.fill((255, 255, 255))  # Sfondo bianco
    turtle.draw()
    lepre.draw()
    pygame.display.flip()
    clock.tick(11)

pygame.quit()
``