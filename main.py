import pygame
import sys
from game_functions import *

# Inicializar PyGame
pygame.init()

# Configuraciones de pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Defensor del Espacio")

# Colores
background = pygame.image.load("images/background.jpg").convert()
background = pygame.transform.scale(background, (800, 600))

# Estado del juego
game_active = False
score = 0

def main_menu():
    global game_active, score
    while not game_active:
        screen.blit(background, (0, 0))
        display_text(screen, "Defensor del Espacio", 400, 300, 50)
        display_text(screen, "Presiona ENTER para comenzar", 400, 400, 30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_active = True
                    score = 0
        
        pygame.display.flip()

def game_loop():
    global score, game_active
    # Variables del juego
    player = Player()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    create_enemies(enemies, 5)
    
    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    bullets.add(bullet)
        
        # Actualizar estado del juego
        player.update()
        enemies.update()
        bullets.update()
        
        # Colisiones
        for bullet in bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, enemies, True)
            if hit_enemies:
                bullets.remove(bullet)
                score += 10
                create_enemies(enemies, len(hit_enemies))
        
        if pygame.sprite.spritecollide(player, enemies, False):
            game_active = False
        
        # Dibujar todo
        screen.blit(background, (0, 0))
        player.draw(screen)
        enemies.draw(screen)
        bullets.draw(screen)
        display_text(screen, f"Score: {score}", 70, 30, 30)
        
        pygame.display.flip()

while True:
    main_menu()
    game_loop()
