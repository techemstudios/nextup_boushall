"""
A simple walkthrough on drawing objects to a pygame surface
--similar to code_em_fall_2017/objects and graphics/shapes.py--
"""

import pygame, sys
from pygame.locals import *

# NumPy library randomly generates RGB values for colors
import numpy

pygame.init()
screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption('Drawing with Pygame')
# Four tuples containing  three RGB values each with NumPy:
colors = numpy.random.randint(0, 255, size=(4, 3))

# Define white color as a variable
WHITE = (255, 255, 255)

# Set background  color
screen.fill(WHITE)

# Draw a circle in the center of window
pygame.draw.circle(screen, colors[0], (200, 200), 25, 0)

# Draw a Line: need a start point and an end point
pygame.draw.line(screen, colors[1], (0, 0), (200, 200), 3)

# Draw a Rectangle: specify color, coordinates of upper-left corner, and dimensions
pygame.draw.rect(screen, colors[2], (200, 0, 100, 100))

# Draw an ellipse (oval): similar parameters required as for a rectangle
pygame.draw.ellipse(screen, colors[03], (100, 300, 100, 50), 2)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
             pygame.quit()
             sys.exit()

        pygame.display.update()
