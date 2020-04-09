import pygame
import os
from constants import *
from player import *
from card import *
from window_functions import *

pygame.init()

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
        button = Button((0, 255, 0), 450, 160, 300, 200, 'OKEY')
        label_name =        Button((0, 255, 0), 20, 100, 100, 32, 'imie', 24)
        label_last_name =   Button((0, 255, 0), 20, 250, 100, 32, 'nazwisko', 24)
        label_nick =        Button((0, 255, 0), 20, 400, 100, 32, 'nick', 24)
        input_name =        InputBox(150, 100, 140, 32)
        input_last_name =   InputBox(150, 250, 140, 32)
        input_nick =        InputBox(150, 400, 140, 32)
        input_boxes = (input_name, input_last_name, input_nick)
        name = ""
        last_name = ""
        nick = ""

        while True:
            self.window.fill((150, 150, 100))
            button.draw(self.window, (0, 0, 0))
            label_name.draw(self.window, (0, 0, 0))
            label_last_name.draw(self.window, (0, 0, 0))
            label_nick.draw(self.window, (0, 0, 0))
            input_name.draw(self.window)
            input_last_name.draw(self.window)
            input_nick.draw(self.window)
            pygame.display.update()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEMOTION:
                    if button.isOver(pos):
                        button.color = (0, 255, 155)
                    else:
                        button.color = (255, 0, 24)

                if event.type == pygame.MOUSEBUTTONUP:
                    if button.isOver(pos):
                        name = input_name.text
                        last_name = input_last_name.text
                        nick = input_nick.text
                        if name != "" and last_name != "" and nick != "":
                            name += "_"
                            name += last_name
                            name.lower()
                            ret = (name, nick)
                            return ret
                    else:
                        pass
                for i in input_boxes:
                    i.handle_event(event)
            for i in input_boxes:
                i.update()
