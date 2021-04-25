#Ciclo básico para iniciar un programa en python.

import pygame, sys

width = 640
height = 480

# Definir pantalla (tamaño y altura)
screen = pygame.display.set_mode((width,height))
screen.fill((246,127,18))
pygame.display.set_caption("Ciclo básico de pygame")

pygame.init()

gameOver = False
while not gameOver:
    
    #Comprobar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    #Refrescar pantalla      
    pygame.display.flip()
    
pygame.quit()
sys.exit()