import pygame
from player import Player
from network import Network
from card import *
from display_window import *

import time

def main():

    window = Display_Window()
    clock = pygame.time.Clock()

    path = "./imgs/characters/"

    test = window.selectCharacterWindow()
    path += test[0]
    path += ".png"
    name = test[1]


    run = True
    n = Network()
    d_t_s = (path, name)
    p = n.getP(d_t_s)
    print(p)

    while run:
        clock.tick(60)
        data_to_send = p
        data_received = n.send(data_to_send)
        all_players = data_received[0]
        deck = data_received[1]
        msg = data_received[2]
        if msg != "":
            print(msg)
        p.setTakeCard(False)

        p.move()

        window.redrawWindow(all_players, deck)


main()