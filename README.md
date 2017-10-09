# NextUp Boushall
NextUp, links to previous game design repos on readme

## Mondays  

### Game Design  

Come up with all new pygame lessons, for repeat students from last year.  

Consider Hyperpad and Codea.

link to repo 1  
link to repo 2  
link to repo 3  
link to repo 4  
link to repo 5  
link to repo 6  
link to repo 7  
link to repo 8    

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
