import random
import pygame
import time
from pygame.locals import *
pygame.init()

#Colors
col_BLUE  = (0, 0, 255)
col_R   = (255, 0, 0)
col_GR = (0, 255, 0)
col_BLACK = (0, 0, 0)
col_WH = (255, 255, 255)
COL_PRP = (230, 230, 250)

# Display variables
display_width = 840
display_height = 650

# the size and color of background screen
display = pygame.display.set_mode((840, 650), RESIZABLE)
display.fill(col_WH)

# setting up the FPS
FPS = 60
clock = pygame.time.Clock()

# loading the images of the cars
car_Enemy = pygame.image.load("C:/Users/User/Desktop/W3exercise/TSIS9/redcar.png")
car_Own = pygame.image.load("C:/Users/User/Desktop/W3exercise/TSIS9/greencar.png")
bg = pygame.image.load("C:/Users/User/Desktop/W3exercise/TSIS9/AnimatedStreet.png")

#fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 40)
game_over = font.render("Game Over", True, col_BLACK)

class coin_generation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.randint(1,3)
        self.img = pygame.transform.scale(pygame.image.load('C:/Users/User/Desktop/W3exercise/TSIS9/coin.png'), (60//self.weight,60//self.weight))
        self.rect = self.img.get_rect()
        self.rect.center = (random.randint(150, display_width-150), random.randint(150, display_height-60))

        

    def check(self):
        pass

    def nextCoin(self):
        self.rect.center = (random.randint(150, display_width-200), random.randint(150, display_height-60))
        self.weight = random.randint(1,3)
        self.img = pygame.transform.scale(pygame.image.load('C:/Users/User/Desktop/W3exercise/TSIS9/coin.png'), (60//self.weight,60//self.weight))
        self.rect = self.img.get_rect()
        self.rect.center = (random.randint(150, display_width-150), random.randint(150, display_height-60))

    def render(self, surface):
        surface.blit(self.img, self.rect)

class ownMovement(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.car = pygame.transform.scale(pygame.image.load('C:/Users/User/Desktop/W3exercise/TSIS9/redcar.png'), (50,70))
        self.rect = self.car.get_rect()
        self.rect.center = (600, 600)
        self.own_speed=5

    def check(self):
        pass

    def move(self):
        key = pygame.key.get_pressed()
        if(self.rect.bottom < display_height):
            if key[K_DOWN]:
                self.rect.move_ip(0, 5)
        if(self.rect.top > 0):
            if key[K_UP]:
                self.rect.move_ip(0, -5)
        if (self.rect.right < display_width-138):
            if key[K_RIGHT]:
                self.rect.move_ip(5, 0)
        if (self.rect.left > 138):
            if key[K_LEFT]:
                self.rect.move_ip(-5, 0)

    def render(self,surface):
        surface.blit(self.car, self.rect)

class enemyMovement(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.car = pygame.transform.scale(pygame.image.load('C:/Users/User/Desktop/W3exercise/TSIS9/greencar.png'), (45, 90))
            self.rect = self.car.get_rect()
            self.rect.center = (random.randint(138, display_width-138),0)
        def check(self):
            pass
        def move(self):
            self.rect.move_ip(0, current_Own.own_speed)
            if(self.rect.bottom>display_width):
                self.rect.top = 0
                self.rect.center = (random.randint(138, display_width-138),0)
        def render(self, surface):
            surface.blit(self.car, self.rect)

current_Own = ownMovement()
current_Enemy = enemyMovement()
current_Coin = coin_generation()
sprite_Coin = pygame.sprite.Group()
sprite_Coin.add(current_Coin)
sprite_Enemy = pygame.sprite.Group()
sprite_Enemy.add(current_Enemy)
sprite_All = pygame.sprite.Group()
sprite_All.add(current_Enemy)
sprite_All.add(current_Own)

global collected
collected = 0
coins = 0
running=True
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while running:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            if current_Own.own_speed > 5:
                pass
            else:
                current_Own.own_speed += 2
        if event.type==QUIT:
            running=False

    display.blit(bg, (0, 0))
    scores = font_small.render(str(coins), True, col_BLACK)
    scores_collected = font_small.render(str(collected), True, col_BLACK)
    display.blit(scores, (840-60, 10))
    display.blit(scores_collected, (100, 10))
    # Moves and Re-draws all Sprites
    for entity in sprite_All:
        display.blit(entity.car, entity.rect)
        entity.move()
    for i in sprite_Coin:
        i.check()
        i.render(display)


    if pygame.sprite.spritecollideany(current_Own, sprite_Coin):
        coins+=current_Coin.weight
        collected+=1
        current_Coin.nextCoin()
        current_Own.own_speed = (collected//5)+5
    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(current_Own, sprite_Enemy):
        pygame.mixer.Sound('C:/Users/User/Desktop/W3exercise/TSIS9/crash.mp3').play()
        time.sleep(0.1)
        display.fill(col_R)
        display.blit(game_over, display.get_rect().center)
        pygame.display.update()

        for entity in sprite_All:
            entity.kill()
        time.sleep(3)
        running=False
    pygame.display.update()
    clock.tick(FPS)