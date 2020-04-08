import pygame
import time
from constants import *


class Player():
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.speed = 4
        self.takeCard = False

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.r)

    def isTakeCard(self):
        return self.takeCard

    def setTakeCard(self, a):
        self.takeCard = a

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT")
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_c:
                    print("C up")
                    self.takeCard = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x - self.r > 0:
            self.x -= self.speed

        if keys[pygame.K_RIGHT] and self.x + self.r < WINDOW_WIDTH:
            self.x += self.speed

        if keys[pygame.K_UP] and self.y - self.r > 0:
            self.y -= self.speed

        if keys[pygame.K_DOWN] and self.y + self.r < WINDOW_HEIGHT:
            self.y += self.speed
