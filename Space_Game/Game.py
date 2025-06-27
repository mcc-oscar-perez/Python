import pygame

# First, we need to initialize pygame
pygame.init()

# Next, we need to create a screen
pantalla = pygame.display.set_mode((800, 600))

#Titiel and icon
pygame.display.set_caption("Invasión Alienígena")
icono = pygame.image.load("D:\Cursos\PYTHON\Carpeta_10\ovni.png")
pygame.display.set_icon(icono)

# Player
img_jugador = pygame.image.load("D:\Cursos\PYTHON\Carpeta_10\cohete_espacial.png")
jugador_x = 368
jugador_y = 536

def jugador():
    pantalla.blit(img_jugador, (jugador_x, jugador_y))

# This is the loop that will keep the game running
se_ejecuta = True
while se_ejecuta:
    
    # Fill the screen with a color (RGB)
    pantalla.fill((205, 144, 228))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            se_ejecuta = False
    
    jugador()  # Call the function to draw the player
    
    pygame.display.update() 

