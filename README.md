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

### Pygame Walkthrough: [Wormy](https://github.com/joetechem/wormy_rasp)  

Fill in the missing code. Explain dependencies, how we use pygame by `import`, discuss how computers handle and display, or represent colors, by using Red, Green, and Blue values (RGB). The retinas of our eyes have three types of photoreceptor cone cells that respond to frequencies of light, categorized into RGB. Similar to painting, we increase/decrease the amount of the three categories to have the computer represent different colors. After using one of the already defined colors as the background color (in Part Two of missing python code), challenge the class to registers their own unique color as a new variable and use as the background color.  

Check out some of the color representations below:   

| Red |Green|Blue | Color |
|-------------------------|
| 0   | 0   | 0   | black |
| 255 | 255 | 255 | white |
| 255 | 255 | 0   | yellow|
| 255 | 130 | 255 | pink  |
| 146 | 81  | 0   | brown |
| 157 | 95  | 82  | purple|
| 140 | 0   | 0   | maroon|  
