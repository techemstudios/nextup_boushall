# NextUp Boushall
NextUp, links to previous game design repos on readme

## Mondays & Wednesdays

### Game Design  

May be worthwhile to consider Hyperpad/Design Thinking lessons.

* [wormy](https://github.com/joetechem/wormy_rasp)  
* [pong](https://github.com/joetechem/pong/tree/master/pong-pygame/pong)
* [frogger](https://github.com/joetechem/frogger)
* [pacman](https://github.com/joetechem/pacman-python-mirror) 
* [spaceshooter](https://github.com/joetechem/pygame_tutorials) 
* [alien invasion](https://github.com/joetechem/alien_invasion/tree/master/alien_invade)

# OOP  

Dice game, before pygame intro?  

## Starting Pygame  

Pygame is part of the Python framework including tools to create video games. What does Pygame have, that allows us to do create games? It is built on top of the Simple Direct Media Layer (SDL), a C framework which gives access to a range of graphics, sounds, keyboard handlers, and other input devices on various operating systems including Linux, MAC OS X, and Windows. -*Instant Pygame for Python Game Development, Ivan Idris*  

### Hello World! (Pygame Style)  

* Objectives  
  - Main Game Loop  
  - Render Text  
  - Surface Object  
  - Quit Event  

#### Dependencies  

#### Initialization  

#### The Main Game Loop  
```python    
# importing dependencies
import pygame, sys
from pygame.locals import *

# initialize
pygame.init()

# window width, height --> units = pixels
screen = pygame.display.set_mode((400, 300))

# window caption
pygame.display.set_caption('Hello World!')

# the main game loop
while True:
    sys_font = pygame.font.SysFont("None", 19)
    rendered = sys_font.render('Hello World', 0, (255, 100, 100))
    # the blit() method, draws items to the surface
    screen.blit(rendered, (100, 100))

    # the quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
```  
