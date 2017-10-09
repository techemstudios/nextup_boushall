import pygame, sys
from pygame.locals import *
import numpy

pygame.init()

# Creates a game clock
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Animating Objects')
img = pygame.image.load('head.png')


# Initializing Arrays
# Define arrays that hold the coordinates of the postitions

# creates an array with 40 equidistant values between 20 and 360
steps = numpy.linspace(20, 360, 40).astype(int)

# creates an array of the specified dimensions filled with zeroes
right = numpy.zeros((2, len(steps)))
down = numpy.zeros((2, len(steps)))
left = numpy.zeros((2, len(steps)))
up = numpy.zeros((2, len(steps)))

right[0] = steps
right[1] = 20

down[0] = 360
down[1] = steps

# [::-1] reverses the order of the array elements
left[0] = steps[::-1]
left[1] = 360

up[0] = 20
up[1] = steps[::-1]

# Joining the sections
# concatenates arrays to form a new array
pos = numpy.concatenate((right.T, down.T, left.T, up.T))
i = 0

while True:
    # Erase screen
    screen.fill((255, 255, 255))
    
    if i >= len(pos):
        i = 0

    # draw the image to the screen
    screen.blit(img, pos[i])
    i += 1
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    # executes a tick of the game clock (30fps)
    clock.tick(30)
