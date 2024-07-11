import pygame
import random

# Clase Jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/player_ship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(400, 550))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed
    
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

# Clase Enemigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/enemy_ship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(random.randint(40, 760), random.randint(-100, -40)))
        self.speed = random.randint(1, 3)
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.rect.center = (random.randint(40, 760), random.randint(-100, -40))

# Clase Bala
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 7
    
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

def create_enemies(group, number):
    for _ in range(number):
        enemy = Enemy()
        group.add(enemy)

def display_text(screen, text, x, y, size):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, (0, 0, 0))
    rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, rect)
