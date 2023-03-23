import pygame

# pygame setup
pygame.init()
w = 1280
h = 720
r = 25
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
running = True

ball_x = w // 2
ball_y = h // 2


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill("white")

    pygame.draw.circle(screen, "red", (ball_x, ball_y), r)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
            ball_y -= 20
    if keys[pygame.K_DOWN]:
            ball_y += 20
    if keys[pygame.K_LEFT]:
            ball_x -= 20
    if keys[pygame.K_RIGHT]:
            ball_x += 20

    if ball_x < r:
            ball_x = r
    elif ball_x > w - r:
            ball_x = w - r
    if ball_y < r:
            ball_y = r
    elif ball_y > h - r:
            ball_y = h - r

    pygame.display.flip()
    clock.tick(60)

pygame.quit()