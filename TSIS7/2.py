import pygame
pygame.init()
W, H = 800, 800
x = W//2
y = H//2
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
mickey = pygame.image.load(r"C:\Users\diase\OneDrive\Рабочий стол\Python\PP2\week 7\main-clock.png")
leftHand = pygame.image.load(r"C:\Users\diase\OneDrive\Рабочий стол\Python\PP2\week 7\left-hand.png")
rightHand = pygame.image.load(r"C:\Users\diase\OneDrive\Рабочий стол\Python\PP2\week 7\right-hand.png")
mickeyRect = mickey.get_rect()
def blitRotateCenter(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = center).center)
    surf.blit(rotated_image, new_rect)
langle = 0
rangle = 0
while True:
    sc.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    langle -= 0.06
    rangle -= 0.000006
    
    sc.fill(WHITE)
    sc.blit(mickey, (x, y))
    sc.blit(mickey, mickeyRect)
    blitRotateCenter(sc, rightHand, (x,y), rangle)
    blitRotateCenter(sc, leftHand, (x,y), langle) 
    
    pygame.display.update()