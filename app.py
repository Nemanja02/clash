from connection import connection as connection
from models.user import loader, user
import pygame

plot = 50
X = 1000
Y = 563

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128, 100) 

loader = loader()
pygame.init()
display_surface = pygame.display.set_mode((X, Y )) 
pygame.display.set_caption('Clash of Koncar')
font = pygame.font.Font('freesansbold.ttf', 16)
print(loader.getUserData())
text = font.render(loader.getUserData()[5], True, white, None)
textRect = text.get_rect()
textRect = (10,10)

done = False
while not done:
    display_surface.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update()  