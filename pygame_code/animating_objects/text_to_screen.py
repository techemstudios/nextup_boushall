import pygame, sys
from pygame.locals import *
import numpy

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 480))

pygame.display.set_caption('Animating Objects')
img = pygame.image.load('head.png')

steps = numpy.linspace(20, 360, 40).astype(int)
right = numpy.zeros((2, len(steps)))
down = numpy.zeros((2, len(steps)))
left = numpy.zeros((2, len(steps)))
up = numpy.zeros((2, len(steps)))

right[0] = steps
right[1] = 20

down[0] = 360
down[1] = steps

left[0] = steps[::-1]
left[1] = 360

up[0] = 20
up[1] = steps[::-1]

pos = numpy.concatenate((right.T, down.T, left.T, up.T))
i = 0

# create a font
font = pygame.font.Font('freesansbold.ttf', 32)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

while True:
    # Erase screen
    screen.fill((0, 0, 0))
    if i >= len(pos):
        i = 0
        
    screen.blit(img, pos[i])
    
    # displaying text in the center of the screen
    text = "%d %d %d" % (i, pos[i][0], pos[i][1])
    rendered = font.render(text, True, RED, BLUE)
    screen.blit(rendered, (180, 200))
    i += 1
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(30)
