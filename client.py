import pygame
from player import Player
from network import Network
from card import *
from display_window import Display_Window

def main():

    window = Display_Window()

    path = "./imgs/characters"

    path += "/ja.jpg"
    name = "Kams"

    run = True
    n = Network()
    d_t_s = (path, name)
    p = n.getP(d_t_s)
    print(p)
    clock = pygame.time.Clock()

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