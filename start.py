#/usr/bin/python

#/usr/bin/python

import pygame
import sys
#import math
import random
import parallax

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)

WINDOWSIZE = (800, 600)
screen = pygame.display.set_mode(WINDOWSIZE, pygame.DOUBLEBUF)
pygame.display.set_caption("Platforming at its Learningest!")

background = parallax.ParallaxSurface(WINDOWSIZE, pygame.RLEACCEL)
background.add("bg3/layers/layer-1.png", 20, (WINDOWSIZE))
background.add("bg3/layers/layer-2.png", 9, (WINDOWSIZE))
background.add("bg3/layers/layer-3.png", 7, (WINDOWSIZE))
background.add("bg3/layers/layer-4.png", 5, (WINDOWSIZE))
background.add("bg3/layers/layer-5.png", 5, (WINDOWSIZE))
background.add("bg3/layers/layer-6.png", 15, (WINDOWSIZE))

time_ref = 0
speed = 10

while True:
    #Event Handleing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pressedkeys = pygame.key.get_pressed()
            if pressedkeys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit(0)

    background.scroll(speed, 'horizontal')
    t = pygame.time.get_ticks()
    if (t - time_ref) > 60:
        background.draw(screen)
        pygame.display.flip()



tiles = pygame.sprite.Group()
sprites = pygame.sprite.Group()

def importbackgrounds():
    pass
def renderscreen():
    pass
