import pygame

import time

pygame.init()

pressed=False
running=True
started=False
mode,font,shape =(0,0,0),5,0
SCREEN=pygame.display.set_mode((500,500))
pygame.display.set_caption("paint")
SCREEN.fill((255,255,255))
while running:
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed:
                pressed=True
                x2=pygame.mouse.get_pos()[0]
                y2=pygame.mouse.get_pos()[1]

        elif event.type==pygame.MOUSEBUTTONUP:
            pressed=False
            if started and shape==1:
                pygame.draw.circle(SCREEN,mode,(start_pointsx,start_pointsy),((start_pointsx-x)**2+(start_pointsy-y)**2)**0.5,font)
                started=False
            if started and shape==2:
                pygame.draw.rect(SCREEN,mode,pygame.Rect(start_pointsx,start_pointsy,abs(start_pointsx-x),abs(start_pointsy-y)),font)
                started=False
                
        if event.type==pygame.KEYDOWN:
            #color of drawing
            if event.key == pygame.K_r:
                mode = (255,0,0)
            elif event.key == pygame.K_g:
                mode = (0,255,0)
            elif event.key == pygame.K_b:
                mode = (0,0,255)
            elif event.key==pygame.K_e:
                shape=0
                mode = (255,255,255)

            #Fontchange
            elif event.key == pygame.K_UP:
                font=min(font+3,100)
            elif event.key == pygame.K_DOWN:
                font=max(1,font-3)

            #Shapechanging,0=line,1=circle,2=rectangle
            elif event.key == pygame.K_RIGHT:
                shape+=1
                if shape>2:
                    shape=0
            elif event.key == pygame.K_LEFT:
                shape-=1
                if shape<0:
                    shape=2

        x=pygame.mouse.get_pos()[0]
        y=pygame.mouse.get_pos()[1]

        if pressed and shape==0:
            pygame.draw.line(SCREEN,mode,(x,y),(x2,y2),font)
            x2=x
            y2=y
        elif pressed and not started and (shape==1 or shape==2):
            start_pointsx=x
            start_pointsy=y
            started=True
    pygame.display.flip()