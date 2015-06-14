#!/usr/bin/env python

import pygame
import numpy
import sys
import os

WINDOWSIZE = (800, 600)
SPRITESCALE = 13

def load_image(path, scale):
    image = pygame.transform.scale(pygame.image.load(path), scale).convert_alpha()
    return image

class Player(pygame.sprite.Sprite):
    def __init__(self, scale, sType='idle'):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.NextFrameCounter = 0
        self.NextFrameMax = 12

        #all the frames our guy can be.
        if sType == 'idle':
            self.images.append(load_image('assets/player/idle/frame-1.png', scale))
            self.images.append(load_image('assets/player/idle/frame-2.png', scale))
        if sType == 'run':
            self.images.append(load_image('assets/player/run/frame-1.png', scale))
            self.images.append(load_image('assets/player/run/frame-2.png', scale))
            self.images.append(load_image('assets/player/run/frame-3.png', scale))
            self.images.append(load_image('assets/player/run/frame-4.png', scale))
        if sType == 'jump up':
            self.images.append(load_image('assets/player/jump up/frame.png', scale))

        self.image = self.images[self.index]
        self.rect = pygame.Rect((212, 520-self.image.get_height()), (0, 0))

    def update(self, direction='right'):
        if self.NextFrameCounter < self.NextFrameMax:
            self.NextFrameCounter += 1
        else:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.NextFrameCounter = 0
            if direction == 'left':
                self.image = self.images[self.index]
                self.image = pygame.transform.flip(self.image, True, False)
            else:
                self.image = self.images[self.index]
