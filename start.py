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
pygame.key.set_repeat(500, 30)

WINDOWSIZE = (800, 600)
SPRITESCALE = 13
TILESCALE = 8

screen = pygame.display.set_mode(WINDOWSIZE, pygame.DOUBLEBUF)
pygame.display.set_caption("Platforming at its Learningest!")

blackground = pygame.Surface(screen.get_size()).convert()
blackground.fill((0, 0, 0))
backgrounds = parallax.ParallaxSurface(WINDOWSIZE, pygame.RLEACCEL)

pcIdle = pygame.sprite.Group()
pcRun = pygame.sprite.Group()
pcJumpUp = pygame.sprite.Group()
pcJumpDown = pygame.sprite.Group()

tiles = pygame.sprite.Group()

def importbackgrounds():
    backgrounds.add("assets/bg3/layers/layer-1.png", 20, (WINDOWSIZE))
    backgrounds.add("assets/bg3/layers/layer-2.png", 9, (WINDOWSIZE))
    backgrounds.add("assets/bg3/layers/layer-3.png", 7, (WINDOWSIZE))
    backgrounds.add("assets/bg3/layers/layer-4.png", 5, (WINDOWSIZE))
    backgrounds.add("assets/bg3/layers/layer-5.png", 5, (WINDOWSIZE))
    backgrounds.add("assets/bg3/layers/layer-6.png", 15, (WINDOWSIZE))

def importsprites():
    global Ground
    scale = tuple(numpy.divide(WINDOWSIZE, SPRITESCALE))
    NewSprite = sClasses.Player(scale, 'idle')
    pcIdle.add(NewSprite)
    NewSprite = sClasses.Player(scale, 'run')
    pcRun.add(NewSprite)
    NewSprite = sClasses.Player(scale, 'jump up')
    pcJumpUp.add(NewSprite)
    NewSprite = sClasses.Player(scale, 'jump down')
    pcJumpDown.add(NewSprite)

def eventhandler(event):
    global PlayerState, PlayerDirection, speed, vspeed, Falling
    ##CLOSE WINDOWs
    if event.type == pygame.QUIT:
        sys.exit()

    pressedkeys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if pressedkeys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit(0)
    ##CLOSE WINDOW

    ##PLAYER MOVEMENT
        ##HORIZONTAL MOVEMENT
    if event.type == KEYDOWN and event.key == K_RIGHT:
        PlayerState = 'run'
        PlayerDirection = 'right'
    if event.type == KEYUP and event.key == K_RIGHT:
        PlayerState = 'idle'
        PlayerDirection = 'right'
    if event.type == KEYDOWN and event.key == K_LEFT:
        PlayerState = 'run'
        PlayerDirection = 'left'
    if event.type == KEYUP and event.key == K_LEFT:
        PlayerState = 'idle'
        PlayerDirection = 'left'
        ##HORIZONTAL MOVEMENT

        ##VERTICAL MOVEMENT
    if event.type == KEYDOWN and event.key == K_SPACE:
        PlayerState = 'jump up'
    if event.type == KEYUP and event.key == K_SPACE:
        #todo: after collision, PlayerState needs to go back to whatever button is being pressed
        PlayerState = 'jump down'

        ##VERTICAL MOVEMENT
    ##PLAYER MOVEMENT

def renderscreen(PlayerState, PlayerDirection):
    def parallax():
        global backgrounds, time_ref, speed, vspeed
        backgrounds.scroll(speed, 'horizontal')
        t = pygame.time.get_ticks()
        if (t - time_ref) > 60:
            backgrounds.draw(screen)

    def spriteanimation(PlayerState, PlayerDirection):
        global speed, vspeed, Falling
        if vspeed >= 80 and not Falling:
            vspeed -= 2
            Falling = True
        elif vspeed <= 0:
            vspeed = 0
            Falling = False
        if PlayerState == 'run':
            if PlayerDirection == 'right':
                speed = 10
            elif PlayerDirection == 'left':
                speed = -10
            if vspeed > 0 and Falling == True:
                vspeed -= 2
            pcRun.update(PlayerDirection, vspeed)
            pcRun.draw(screen)
        elif PlayerState == 'jump up':
            if not Falling:
                vspeed += 1
            if Falling:
                vspeed -= 2

            pcJumpUp.update(PlayerDirection, vspeed)
            pcJumpUp.draw(screen)
        elif PlayerState == 'jump down':
            Falling = True
            if vspeed > 0 and Falling == True:
                vspeed -= 2
            pcJumpDown.update(PlayerDirection, vspeed)
            pcJumpDown.draw(screen)
        elif PlayerState == 'idle':
            speed = 0
            if vspeed > 0 and Falling == True:
                vspeed -= 2
            pcIdle.update(PlayerDirection, vspeed)
            pcIdle.draw(screen)

    parallax()
    spriteanimation(PlayerState, PlayerDirection)
    pygame.display.flip()

#init some things
importbackgrounds()
importsprites()

#flags and longs etc.
time_ref = 0
speed = 0
vspeed = 0
Falling = False
PlayerState = 'idle'
PlayerDirection = 'right'
while True:
    #Event Handleing
    for event in pygame.event.get():
        eventhandler(event)

    #Rendering
    renderscreen(PlayerState, PlayerDirection)

