"""
HelloWorld.py (pygame style)
Objectives:
    Dependencies (imports)
    Main Game Loop
    Render Text
    Drawing object to surface with surface object
    The Quit Event
"""

# importing dependencies
import pygame, sys
from pygame.locals import *

# initialize
# Must be called before any other pygame functions
pygame.init()

# Creates the Surface object
# window width, height as a tuple --> units = pixels
screen = pygame.display.set_mode((400, 300))

# window caption
pygame.display.set_caption('Hello World!')

# the main game loop
while True:
    sys_font = pygame.font.SysFont("None", 24)
    # Draws text to surface
    rendered = sys_font.render('Hello World!', 0, (255, 100, 100))
    # Draws on the surface
    screen.blit(rendered, (100, 100))

    # the quit event
    for event in pygame.event.get():    # gets a list of Event objects
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # refreshes the surface
    pygame.display.update()
