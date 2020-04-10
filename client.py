import pygame
from player import Player
from network import Network
from card import *
from display_window import *

def main():

    window = Display_Window()
    clock = pygame.time.Clock()

    test = window.selectCharacterWindow()
    path = test[0]
    name = test[1]
    font = pygame.font.SysFont("comicsansms", 18)
    texts = [[font.render("Hello, World", True, (0, 0, 200)), font.render("Hello, World", True, (0, 0, 200)), 0],
             [font.render("Hello, World", True, (0, 0, 200)), font.render("Hello, World", True, (0, 0, 200)), 0],
             [font.render("Hello, World", True, (0, 0, 200)), font.render("Hello, World", True, (0, 0, 200)), 0],
             [font.render("Hello, World", True, (0, 0, 200)), font.render("Hello, World", True, (0, 0, 200)), 0],
             [font.render("Hello, World", True, (0, 0, 200)), font.render("Hello, World", True, (0, 0, 200)), 0]]
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
        i = 0
        if msg != "":
            while(texts[i][2]==1):
                i += 1
                if i == 5:
                    texts[0] = texts[1]
                    texts[1] = texts[2]
                    texts[2] = texts[3]
                    texts[3] = texts[4]
                    texts[4] = (font.render(msg[0], True, (0, 128, 0))), (font.render(msg[1], True, (0, 128, 0))), 1
                    break
            print(msg)
            if i < 5:
                texts[i] = (font.render(msg[0], True, (0, 128, 0))), (font.render(msg[1], True, (0, 128, 0))), 1
        p.setTakeCard(False)

        p.move()

        window.redrawWindow(all_players, deck, texts)


main()