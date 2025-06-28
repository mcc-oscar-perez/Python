import pygame

# First, we need to initialize pygame
pygame.init()

# Next, we need to create a screen
pantalla = pygame.display.set_mode((800, 600))

#Titiel and icon
pygame.display.set_caption("Invasión Alienígena")
icono = pygame.image.load("D:\Cursos\PYTHON\Space_Game\ovni.png")
pygame.display.set_icon(icono)

# Player
img_jugador = pygame.image.load("D:\Cursos\PYTHON\Space_Game\cohete_espacial.png")
jugador_x = 368
jugador_y = 536
jugador_x_change = 0


def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))

# This is the loop that will keep the game running
se_ejecuta = True
while se_ejecuta:
    
    # Fill the screen with a color (RGB)
    pantalla.fill((205, 144, 228))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            se_ejecuta = False
        # Here we program the controls for the player 
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                jugador_x_change = -0.1
            if event.key == pygame.K_RIGHT:
                jugador_x_change = 0.1
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_x_change = 0
                


    # Update the player's position
    jugador_x += jugador_x_change
    jugador(jugador_x,jugador_y)  # Call the function to draw the player
    
    pygame.display.update() 


