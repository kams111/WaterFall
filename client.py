import pygame
from player import Player
from  network import Network
from constants import *
from card import *

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Wódospad XD")


def redrawWindow(win, all_players, cards):
    win.fill((255, 255, 255))
    cards[-1].draw(win)
    for p in all_players:
        p.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    print(p)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        data_to_send = p
        data_received = n.send(data_to_send)
        all_players = data_received[0]
        deck = data_received[1]
        p.setTakeCard(False)

        p.move()

        redrawWindow(window, all_players, deck)


main()