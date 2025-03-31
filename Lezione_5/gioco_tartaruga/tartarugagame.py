import pygame


width: int = 640
height: int = 420

BACKGROUND = pygame.image.load('/home/lorenzo-rossi/Its-Esercizi/Lezione_5/gioco_tartaruga/assets/backgroundtart.jpg')

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('tartarga e la lepre')

clock = pygame.time.Clock()
running: bool = True

while running:
    
    screen.blit(BACKGROUND, (0, 0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
    pygame.display.update()
    clock.tick(60)
pygame.quit()