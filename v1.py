#/usr/bin/python

import pygame
from pygame.locals import *
import sys
import numpy
#import math
import random
import parallax
import sClasses

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)

WINDOWSIZE = (800, 600)
SPRITESCALE = 13
screen = pygame.display.set_mode(WINDOWSIZE, pygame.DOUBLEBUF)
pygame.display.set_caption("Platforming at its Learningest!")

blackground = pygame.Surface(screen.get_size()).convert()
blackground.fill((0, 0, 0))
backgrounds = parallax.ParallaxSurface(WINDOWSIZE, pygame.RLEACCEL)

pcIdle = pygame.sprite.Group()
pcRun = pygame.sprite.Group()
pcJumpUp = pygame.sprite.Group()
tiles = pygame.sprite.Group()

def importbackgrounds():
    backgrounds.add("assets/bg3/layers/layer-1.png", 20, (WINDOWSIZE))
    backgrounds.add("assets/bg3/layers/layer-2.png", 9, (WINDOWSIZE))
    backgrounds.add("assets/bg3/layers/layer-3.png", 7, (WINDOWSIZE))
    backgrounds.add("assets/bg3/layers/layer-4.png", 5, (WINDOWSIZE))
    backgrounds.add("assets/bg3/layers/layer-5.png", 5, (WINDOWSIZE))
    backgrounds.add("assets/bg3/layers/layer-6.png", 15, (WINDOWSIZE))

def importsprites():
    scale = tuple(numpy.divide(WINDOWSIZE, SPRITESCALE))
    NewSprite = sClasses.Player(scale, 'idle')
    pcIdle.add(NewSprite)
    NewSprite = sClasses.Player(scale, 'run')
    pcRun.add(NewSprite)
    NewSprite = sClasses.Player(scale, 'jump up')
    pcJumpUp.add(NewSprite)

def renderscreen(PlayerState, PlayerDirection):
    def parallax():
        global backgrounds, time_ref, speed
        backgrounds.scroll(speed, 'horizontal')
        t = pygame.time.get_ticks()
        if (t - time_ref) > 60:
            backgrounds.draw(screen)

    def spriteanimation(PlayerState, PlayerDirection):
        if PlayerState == 'run':
            pcRun.update(PlayerDirection)
            pcRun.draw(screen)
        elif PlayerState == 'jump up':
            pcJumpUp.update(PlayerDirection)
            pcJumpUp.draw(screen)
        else:
            pcIdle.update(PlayerDirection)
            pcIdle.draw(screen)

    screen.blit(blackground, (0, 0))
    parallax()
    spriteanimation(PlayerState, PlayerDirection)

    pygame.display.flip()

#init some things
importbackgrounds()
importsprites()

#flags and longs etc.
time_ref = 0
speed = 0
PlayerState = 'idle'
PlayerDirection = 'right'
while True:
    #Event Handleing
    for event in pygame.event.get():
        ##CLOSE WINDOW
        if event.type == pygame.QUIT:
            sys.exit()

        pressedkeys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if pressedkeys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit(0)
        ##CLOSE WINDOW
        ##PLAYER MOVEMENT
        if event.type == KEYDOWN and event.key == K_RIGHT:
            speed += 10
            PlayerState = 'run'
            PlayerDirection = 'right'
        if event.type == KEYUP and event.key == K_RIGHT:
            speed -= 10
            PlayerState = 'idle'
            PlayerDirection = 'right'
        if event.type == KEYDOWN and event.key == K_LEFT:
            speed -= 10
            PlayerState = 'run'
            PlayerDirection = 'left'
        if event.type == KEYUP and event.key == K_LEFT:
            speed += 10
            PlayerState = 'idle'
            PlayerDirection = 'right'
        if event.type == KEYDOWN and event.key == K_SPACE:
            PlayerState = 'jump up'
        if event.type == KEYUP and event.key == K_SPACE:
            PlayerState = PlayerState

        ##PLAYER MOVEMENT

    #print pygame.mouse.get_pos()
    renderscreen(PlayerState, PlayerDirection)

