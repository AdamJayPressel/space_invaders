#!/usr/bin/python
import pygame
from pygame.locals import *
from colors import *
from random import *

WIDTH = 400
HEIGHT = 647


class Asteroid(pygame.sprite.Sprite):
	#create asteroid object and give it initial position and velocity
	def __init__(self):
                super(Asteroid, self).__init__()
                
                self.image = pygame.image.load('asteroid.png')
                self.image = pygame.transform.scale(self.image, (50,50))
                self.rect = self.image.get_rect()
                self.rect.x = randrange(0,WIDTH)
                self.rect.y = randrange(0,30)
                self.vy = randint(1,5)
                self.vx = randint(-1,1)
        
	#create how asteroid will move with time
	def update(self):
                self.rect.x += self.vx
                self.rect.y += self.vy
                if (self.rect.x > WIDTH):
                        self.rect.x = 0
                elif (self.rect.x < 0):
                        self.rect.x = WIDTH
                elif (self.rect.y > HEIGHT):
                        self.rect.y = 0

        def draw(self,surf):
                surf.blit(self.image, self.rect)

        def off_screen(self):
                off = false
                if(self.rect.centerx > WIDTH):
                        off = true
                if(self.rect.centerx < 0):
                        off = true
                if(self.rect.centery > HEIGHT):
                        off = true
                

                return off


