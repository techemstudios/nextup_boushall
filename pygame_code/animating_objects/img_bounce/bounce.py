import sys, pygame

# initialize pygame
pygame.init()

# window size
size = width, height = 600, 700

# set speed
speed = [1, 1]

# create a variable color
color = 130, 202, 154

# tell Python the type of screen
screen = pygame.display.set_mode(size)

# set variable for image
# and tell Python the file name to get
ball = pygame.image.load("basketball.png")

# set variable 
ballrect = ball.get_rect()

# setup the loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # fill the background with the color specified earlier
    screen.fill(color)
    # draw image file to screen
    screen.blit(ball, ballrect)
    pygame.display.flip()
