import pygame
import os
from constants import *
from player import *
from card import *

class Display_Window():
    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Wódospad XD")

    def redrawWindow(self, all_players, cards):
        self.window.fill((0, 255, 0))
        cards[-1].draw(self.window)
        for p in all_players:
            all_players[p].draw(self.window)
        pygame.display.update()

    def selectCharacterWindow(self):
        pass


