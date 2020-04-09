import pygame
import time
from constants import *


class Player():
    def __init__(self, x, y, path, name):
        self.x = x
        self.y = y
        self.path = path
        self.speed = 4
        self.takeCard = False
        self.name = name

    def draw(self, window):
        img = pygame.image.load(self.path)
        img = pygame.transform.scale(img, (DEFAULT_R*2, DEFAULT_R*2))
        window.blit(img, (self.x, self.y))

    def isTakeCard(self):
        return self.takeCard

    def setTakeCard(self, a):
        self.takeCard = a

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_c:
                    self.takeCard = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed

        if keys[pygame.K_RIGHT] and self.x + DEFAULT_R * 2 < MAP_WIDTH:
            self.x += self.speed

        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed

        if keys[pygame.K_DOWN] and self.y + DEFAULT_R * 2 < MAP_HEIGHT:
            self.y += self.speed
