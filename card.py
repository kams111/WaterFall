import pygame
import random


class Card():
    def __init__(self, path, id):
        self.path = path
        self.id = id

    def draw(self, window):
        img = pygame.image.load(self.path)
        # img = pygame.transform.scale(img, (150,220))
        window.blit(img, (190, 100))


def init_card_deck():
    deck = []
    for i in range (13):
        str = "./imgs/KI{}.png".format(i+1)
        deck.append(Card(str, i*4+1))
        str = "./imgs/KA{}.png".format(i+1)
        deck.append(Card(str, i*4+2))
        str = "./imgs/P{}.png".format(i+1)
        deck.append(Card(str, i*4+3))
        str = "./imgs/T{}.png".format(i+1)
        deck.append(Card(str, i*4+4))

    deck.append(Card("./imgs/RED_JOKER.png", 53))
    deck.append(Card("./imgs/BLACK_JOKER.png", 54))

    random.shuffle(deck)

    deck.append(Card("./imgs/REVERS.png", 55))

    return deck


