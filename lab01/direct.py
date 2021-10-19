import pydirectinput
import pygame
import random

# class for drawing circles
class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y),
                           self.radius)


pygame.init() # initialize
pad = pygame.joystick.Joystick(0) # get joystick
width, height = 1980, 900 # set window size
screen = pygame.display # display screen
surface = screen.set_mode((width, height)) # set surface

pad_name = pad.get_name() # ged pad name
pygame.display.set_caption(f"{pad_name} - drawing") # display pad name

# cursor position, default center
position_x = width / 2
position_y = height / 2

speed = 0.5 # cursor speed
running = True # while false, run program
drawing = False # if true, draw

color = (0, 0, 0) # default color

radius = 25 # cursor radius

circles = [] # drawed circles

#main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.JOYBUTTONDOWN:
            if pad.get_button(0):
                drawing = True
            if pad.get_button(1):
                speed *= 0.5 # set speed to slower
            if pad.get_button(2):
                speed *= 2 # set speed to higher
            if pad.get_button(3): # set random color
                color = (random.randrange(0, 255),
                         random.randrange(0, 255),
                         random.randrange(0, 255))
            if pad.get_button(5): # change cursor size
                if radius != 1:
                    radius -= 1
            if pad.get_button(6):
                radius += 1
        if event.type == pygame.JOYBUTTONUP: # if fire clicked then draw
            if not pad.get_button(0):
                drawing = False

    surface.fill((255, 255, 255)) # fill cursor

    # draw all circles
    for circle in circles:
        circle.draw(surface)
    
    # change cursor position
    position_x += pad.get_axis(0) * speed
    position_y += pad.get_axis(1) * speed

    # display cursor
    pygame.draw.circle(surface, (0, 0, 0), (position_x, position_y),
                       radius)

    # add new circles
    if drawing:
        circles.append(Circle(position_x, position_y, radius, color))

    screen.update()
