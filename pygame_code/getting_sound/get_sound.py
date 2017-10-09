import pygame, sys
from pygame.locals import *
import numpy
import urllib2
import time

WAV_FILE = 'smashingbaby.wav'

def play():
    audio = pygame.mixer.Sound(WAV_FILE)
    audio.play(-1)
    TIMEOUT = 1
    pygame.time.delay(TIMEOUT * 3000)
    audio.stop()
    time.sleep(TIMEOUT)
    
pygame.init()
pygame.display.set_caption('Sound Demo')

response = urllib2.urlopen('http://www.thesoundarchive.com/austinpowers/smashingbaby.wav')
                           
filehandle = open(WAV_FILE, 'w')
filehandle.write(response.read())
filehandle.close()
screen = pygame.display.set_mode((400, 400))
                           
while True:
    sys_font = pygame.font.SysFont("None", 19)
    rendered = sys_font.render('Smashing Baby', 0, (255, 100, 100))
    screen.blit(rendered, (100, 100))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            play()
            pygame.quit()
            sys.exit()
                           
    pygame.display.update()
