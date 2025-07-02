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