import pygame
import random
import math
from pygame import mixer

# First, we need to initialize pygame
pygame.init()

# Next, we need to create a screen
pantalla = pygame.display.set_mode((800, 600))

#Titiel and icon
pygame.display.set_caption("Invasión Alienígena")
icono = pygame.image.load("D:\Cursos\PYTHON\Space_Game\ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("D:/Cursos/PYTHON/Space_Game/Fondo.jpg")

# Background music
mixer.music.load("D:/Cursos/PYTHON/Space_Game/MusicaFondo.mp3")
mixer.music.set_volume(0.5)  # Set volume to 50%
mixer.music.play(-1)  # -1 means the music will loop indefinitely

# Player
img_jugador = pygame.image.load("D:\Cursos\PYTHON\Space_Game\cohete_espacial.png")
jugador_x = 368
jugador_y = 500
jugador_x_change = 0

# Enemy
img_enemy = []
enemy_x = []  
enemy_y = [] 
enemy_x_change = []
enemy_y_change = []
number_of_enemys = 8

for e in range(number_of_enemys):
    img_enemy.append(pygame.image.load("D:\Cursos\PYTHON\Space_Game\enemy.png"))
    enemy_x.append(random.randint(0, 768))  # 800 - width of the enemy image (32)  
    enemy_y.append(random.randint(50, 150))  # Random y position for the enemy 
    enemy_x_change.append(0.1)  # Speed of the enemy
    enemy_y_change.append(75) # Vertical movement of the enemy

# Bullet
img_bullet = pygame.image.load("D:/Cursos/PYTHON/Space_Game/bala.png")
bullet_x = 0 
bullet_y = 500 
bullet_x_change = 0
bullet_y_change = 0.5
bullet_visible = False  # Bullet is not visible initially

# punctuation
punctuation = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10

# End game text
fuente_final = pygame.font.Font("freesansbold.ttf", 64)
def end_text():
    mi_fuente_final = fuente_final.render("¡FIN DEL JUEGO!", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (115, 250))
    
# Function to show the score on the screen
def show_score(x, y):
    texto = fuente.render(f"Puntuación: {punctuation}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# function to draw the player and enemy on the screen
def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))

# Enemy function to draw the enemy on the screen
def enemy(x,y,ene):
    pantalla.blit(img_enemy[ene], (x,y)) 

# Bullet function to draw the bullet on the screen
def bullet(x,y):
    global bullet_visible
    bullet_visible = True
    pantalla.blit(img_bullet, (x + 24, y + 10))  # Center the bullet on the player

# function to check for collision
def is_collision(X_1, Y_1, X_2, Y_2):
    distance = math.sqrt((math.pow(X_1 - X_2, 2)) + (math.pow(Y_1 - Y_2, 2)))
    if distance <24:
        return True
    else:
        return False

# This is the loop that will keep the game running
se_ejecuta = True
while se_ejecuta:
    
    # upload the background image from the screen
    pantalla.blit(fondo, (0, 0))
    
    # Herem progam the quit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            se_ejecuta = False
        
        # Here we program the controls for the player 
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                jugador_x_change = -0.2
            if event.key == pygame.K_RIGHT:
                jugador_x_change = 0.2
            
            # Here we program the bullet controls
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound("D:/Cursos/PYTHON/Space_Game/disparo.mp3")  # load bullet sound
                bullet_sound.play()  # Play the sound effect
                if not bullet_visible:  # Only allow shooting if the bullet is not visible
                    bullet_x = jugador_x
                    bullet(bullet_x, bullet_y) 
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_x_change = 0


    # Update the player's position
    jugador_x += jugador_x_change
    
    # keep the player within the screen bounds
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:  # 800 - width of the player image (64)
        jugador_x = 736
        
        
    # Update the enemy's position
    for e in range(number_of_enemys):
        
        # If the enemy reaches the player
        if enemy_y[e] > 490:  
            for j in range(number_of_enemys):
                enemy_y[j] = 1000
            end_text()
            break
        
        enemy_x[e] += enemy_x_change[e]
    
    # keep the enemy within the screen bounds
        if enemy_x[e] <= 0:
            enemy_x_change[e] = 0.1
            enemy_y[e] += enemy_y_change[e]
        elif enemy_x[e] >= 768:  # 800 - width of the player image (64)
            enemy_x_change[e] = -0.1
            enemy_y[e] += enemy_y_change[e]
        

    # Check for collision between the bullet and the enemy
        collition = is_collision(enemy_x[e],enemy_y[e], bullet_x, bullet_y)
        if collition:
            collition_sound = mixer.Sound("D:/Cursos/PYTHON/Space_Game/Golpe.mp3")
            collition_sound.play()  # Play the collision sound effect
            bullet_y = 500
            bullet_visible = False
            punctuation += 1
            print(f"Puntuación: {punctuation}")
            enemy_x[e] = random.randint(0, 768)
            enemy_y[e] = random.randint(50, 150)
        
        enemy(enemy_x[e], enemy_y[e], e)
        
    # bullet movement
    if bullet_y <= -16:
        bullet_y = 500 
        bullet_visible = False
        
    if bullet_visible:  
        bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    
    # Call the function to draw the player on the screen
    jugador(jugador_x,jugador_y)  
    
    # Show the score on the screen
    show_score(text_x, text_y)
    
    # update 
    pygame.display.update() 
    
    


