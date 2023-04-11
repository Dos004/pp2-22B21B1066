import pygame
import math
pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

def FindVerticesOfEquilateralTriangle(x0,y0,x,y):

    # calculate the angle between the center and vertex
    theta1 = math.atan2(y - y0, x - x0)

    # calculate the length of r using the formula we derived earlier
    r = math.sqrt((x - x0)**2 + (y - y0)**2) * 2 / math.sqrt(3)

    # calculate the coordinates of the other two vertices using the polar coordinate formula
    # with angles of theta1 + 120 degrees and theta1 - 120 degrees
    x1 = x0 + r * math.cos(theta1 + math.radians(120))
    y1 = y0 + r * math.sin(theta1 + math.radians(120))
    x2 = x0 + r * math.cos(theta1 - math.radians(120))
    y2 = y0 + r * math.sin(theta1 - math.radians(120))

    # Return the coordinates of all three vertices
    return [(x, y), (x1, y1), (x2, y2)]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameObject:
    def draw(self):
        return

    def update(self, current_pos):
        return

class ButtonPen(GameObject):
    def __init__(self):
        self.size = 40
        self.pen = pygame.transform.scale(pygame.image.load("C:/Users/User/Desktop/W3exercise/TSIS9/penbuttonimages.png"),(40,40))
        self.rect = pygame.draw.rect(
            SCREEN,
            (0, 0, 0),
            (
                WIDTH // 2 - 150 - self.size // 2,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self):
        SCREEN.blit(self.pen,(WIDTH // 2 - 150 - self.size // 2,20))

    def update(self, current_pos):
        pass



class ButtonRightTriangle(GameObject):
    def __init__(self):
        self.size = 40
        self.pen = pygame.transform.scale(pygame.image.load("C:/Users/User/Desktop/W3exercise/TSIS9/righttriangle.png"),(40,40))
        self.rect = pygame.draw.rect(
            SCREEN,
            (0, 0, 0),
            (
                WIDTH // 2 +80 - self.size // 2,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self):
        SCREEN.blit(self.pen,(WIDTH // 2 +80 - self.size // 2,20))

    def update(self, current_pos):
        pass



class ButtonEraser(GameObject):
    def __init__(self):
        self.size = 40
        self.pen = pygame.transform.scale(pygame.image.load("C:/Users/User/Desktop/W3exercise/TSIS9/eraserbutton.png"),(40,40))
        self.rect = pygame.draw.rect(
            SCREEN,
            (0, 0, 0),
            (
                WIDTH // 2 - 100 - self.size // 2,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self):
        SCREEN.blit(self.pen,(WIDTH // 2 - 100 - self.size // 2,20))

    def update(self, current_pos):
        pass

class ButtonRombus(GameObject):
    def __init__(self):
        self.size = 40
        self.pen = pygame.transform.scale(pygame.image.load("C:/Users/User/Desktop/W3exercise/TSIS9/rombus.png"),(40,40))
        self.rect = pygame.draw.rect(
            SCREEN,
            (0, 0, 0),
            (
                WIDTH // 2 +130 - self.size // 2,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self):
        SCREEN.blit(self.pen,(WIDTH // 2 +130- self.size // 2,20))

    def update(self, current_pos):
        pass


class ButtonEquileiteral(GameObject):
    def __init__(self):
        self.size = 40
        self.pen = pygame.transform.scale(pygame.image.load("C:/Users/User/Desktop/W3exercise/TSIS9/equileiteral.png"),(40,40))
        self.rect = pygame.draw.rect(
            SCREEN,
            (0, 0, 0),
            (
                WIDTH // 2 +190 - self.size // 2,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self):
        SCREEN.blit(self.pen,(WIDTH // 2 +190- self.size // 2,20))

    def update(self, current_pos):
        pass



class ButtonRect(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            (0, 0, 0),
            (
                WIDTH // 2 - 50 - self.size // 2,
                20,
                self.size+10,
                self.size-10,
            )
        )

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            (255, 255, 255),
            pygame.Rect(
                WIDTH // 2 -50 - self.size // 2,
                20,
                self.size+10,
                self.size-10,
            )
        )

    def update(self, current_pos):
        pass


class ButtonCube(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            (0, 0, 0),
            (
                WIDTH // 2 +20 - self.size // 2,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            (255, 255, 255),
            pygame.Rect(
                WIDTH // 2 +20  - self.size // 2,
                20,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass


class ButtonCircle(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            (0, 0, 0),
            (
                WIDTH // 2 -200 - self.size // 2,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            (255, 255, 255),
            pygame.Rect(
                WIDTH // 2 - 200 - self.size // 2,
                20,
                self.size,
                self.size,
            ),
            0,
            -1,20,20,20,20
        )

    def update(self, current_pos):
        pass



class Pen(GameObject):
    def __init__(self,draw_font,draw_color,*args, **kwargs):
        self.points: list[Point] = [] 
        self.draw_font=draw_font
        self.draw_color=draw_color

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):
            next_point = self.points[idx + 1]
            pygame.draw.line(
                SCREEN,
                self.draw_color,
                start_pos=(point.x, point.y),
                end_pos=(next_point.x, next_point.y),
                width=self.draw_font
            )

    def update(self, current_pos):
        self.points.append(Point(*current_pos))


class Cube(GameObject):
    def __init__(self, start_pos, draw_font, draw_color, *args, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.draw_font = draw_font
        self.draw_color = draw_color


    def draw(self):
        start_pos_x = self.start_pos.x
        start_pos_y = self.start_pos.y
        end_pos_x = self.end_pos.x
        end_pos_y = self.end_pos.y
        distance = ((start_pos_x-end_pos_x)**2+(end_pos_y-start_pos_y)**2)**0.5
        start_pos_x=start_pos_x-(distance*(2**0.5))/2
        start_pos_y=start_pos_y-(distance*(2**0.5))/2
        pygame.draw.rect(
            SCREEN,
            self.draw_color,
            (
                start_pos_x,
                start_pos_y,
                (distance*(2**0.5)),
                (distance*(2**0.5))

            ),
            width=self.draw_font,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


class EquilateralTriangle(GameObject):
    def __init__(self, start_pos,draw_font,draw_color, *args, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.draw_font=draw_font
        self.draw_color=draw_color

    def draw(self):
        pygame.draw.polygon(SCREEN,self.draw_color,FindVerticesOfEquilateralTriangle(self.start_pos.x,self.start_pos.y,self.end_pos.x,self.end_pos.y),draw_font)
    def update(self, current_pos):
        self.end_pos.x,self.end_pos.y = current_pos


class RightTriangle(GameObject):
    def __init__(self, start_pos,draw_font,draw_color, *args, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.draw_font=draw_font
        self.draw_color=draw_color

    def draw(self):
        third_pos_x=self.end_pos.x
        third_pos_y=self.start_pos.y
        pygame.draw.polygon(SCREEN,self.draw_color,[(self.start_pos.x,self.start_pos.y),(self.end_pos.x,self.end_pos.y),(third_pos_x,third_pos_y)],self.draw_font)

    def update(self, current_pos):
        self.end_pos.x,self.end_pos.y = current_pos

class Rectangle(GameObject):
    def __init__(self, start_pos,draw_font,draw_color, *args, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.draw_font=draw_font
        self.draw_color=draw_color

    def draw(self):
        start_pos_x =min(self.start_pos.x, self.end_pos.x)
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.rect(
            SCREEN,
            self.draw_color,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=self.draw_font,
        )

    def update(self, current_pos):
        self.end_pos.x,self.end_pos.y = current_pos



class Rombus(GameObject):
    def __init__(self, start_pos,draw_font,draw_color, *args, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.draw_font=draw_font
        self.draw_color=draw_color

    def draw(self):
        start_pos_x =self.start_pos.x
        start_pos_y = self.start_pos.y

        end_pos_x = self.end_pos.x
        end_pos_y = self.end_pos.y
        distance = ((start_pos_x-end_pos_x)**2+(end_pos_y-start_pos_y)**2)**0.5
        next_pos_x=start_pos_x-(distance*(2**0.5))/2
        next_pos_y=start_pos_y-(distance*(2**0.5))/2

        pygame.draw.polygon(SCREEN,self.draw_color,
                            [(start_pos_x,abs(start_pos_y-(start_pos_y-end_pos_y)) ),
                             (abs( start_pos_x+(start_pos_x-end_pos_x)),start_pos_y),
                             (start_pos_x,abs(start_pos_y+(start_pos_y-end_pos_y)) ),
                             (abs( start_pos_x-(start_pos_x-end_pos_x)),start_pos_y)],
                             draw_font)



    def update(self, current_pos):
        self.end_pos.x,self.end_pos.y = current_pos

class Circle(GameObject):
    def __init__(self,start_pos,draw_font,draw_color,*arg,**kwarg):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.draw_font=draw_font
        self.draw_color=draw_color
    def draw(self):
        center_x=self.start_pos.x
        center_y=self.start_pos.y
        end_pos_x=self.end_pos.x
        end_pos_y=self.end_pos.y
        print(23)
        radius=(abs(end_pos_x-center_x)**2+abs(end_pos_y-center_y)**2)**0.5
        pygame.draw.circle(
            SCREEN,
            self.draw_color,
            (center_x,center_y),
            radius,
            self.draw_font
        )
    def update(self, current_pos):
        self.end_pos.x,self.end_pos.y=current_pos
def main():
    running = True
    global draw_font
    draw_font=5
    draw_color=WHITE
    game_object = GameObject()
    active_obj = game_object
    current_shape = Pen # current_shape()
    button_pen=ButtonPen()
    button_eraser = ButtonEraser()
    button_rect = ButtonRect()
    button_circle=ButtonCircle()
    button_cube=ButtonCube()
    button_rombus=ButtonRombus()
    button_equileiteral=ButtonEquileiteral()
    button_right_triangle=ButtonRightTriangle()

    objects = [
        (button_pen,0,draw_color),
        (button_rect,0,draw_color),
        (button_eraser,0,draw_color),
        (button_circle,0,draw_color),
        (button_cube,0,draw_color),
        (button_right_triangle,0,draw_color),
        (button_rombus,0,draw_color),
        (button_equileiteral,0,draw_color)
    ]

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.rect.collidepoint(event.pos):
                    current_shape = Rectangle
                    draw_color= WHITE
                elif button_circle.rect.collidepoint(event.pos):
                    current_shape = Circle
                    draw_color= WHITE
                elif button_pen.rect.collidepoint(event.pos):
                    current_shape = Pen
                    draw_color= WHITE
                elif button_cube.rect.collidepoint(event.pos):
                    current_shape = Cube
                    draw_color= WHITE
                elif button_eraser.rect.collidepoint(event.pos):
                    current_shape = Pen
                    draw_color=(0,0,0)
                elif button_right_triangle.rect.collidepoint(event.pos):
                    current_shape = RightTriangle
                    draw_color=WHITE
                elif button_rombus.rect.collidepoint(event.pos):
                    current_shape = Rombus
                    draw_color=WHITE
                elif button_equileiteral.rect.collidepoint(event.pos):
                    current_shape = EquilateralTriangle
                    draw_color=WHITE
                else:
                    active_obj = current_shape(start_pos=pygame.mouse.get_pos(),draw_font=draw_font,draw_color=draw_color)
                    objects.append((active_obj,draw_font,draw_color))

            if event.type == pygame.MOUSEMOTION:
                active_obj.update(current_pos=pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONUP:
                active_obj = game_object
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    draw_font=min(100,draw_font+3)
                if event.key == pygame.K_DOWN:
                    draw_font=max(1,draw_font-3)
                if event.key == pygame.K_r:
                    draw_color=(255,0,0)
                elif event.key == pygame.K_g:
                    draw_color=(0,255,0)
                elif event.key == pygame.K_b:
                    draw_color=(0,0,255)
                

        for obj in objects:
            obj[0].draw_font=obj[1]
            obj[0].draw_color=obj[2]
            obj[0].draw()

        clock.tick(45)
        pygame.display.flip()


if __name__ == '__main__':
    main()