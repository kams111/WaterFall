import socket
from constants import *
from player import Player
import pickle
from _thread import *
from card import *

server = "25.129.108.254"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(MAX_PLAYERS_NUMBER)
print("Waiting for connection, Server Started! Max number of players: " + str(MAX_PLAYERS_NUMBER))

deck = init_card_deck()
players = {}
msg = {}

pool_of_players = []
for i in range(MAX_PLAYERS_NUMBER):
    pool_of_players.append(i)
pool_of_players.append(MAX_PLAYERS_NUMBER + 1)
print(pool_of_players)

currentPlayer = 0


def threaded_client(conn, player):
    d = pickle.loads(conn.recv(2048))
    players[player] = Player(PLAYER_START[0][0], PLAYER_START[0][1], d[0], d[1])
    global deck
    global msg
    conn.send(pickle.dumps(players[player]))
    print("Stworzona postać dla: {}".format(players[player].name))
    msg[player] = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if players[player].isTakeCard():
                    deleted_card = deck.pop(-1)
                    print(deleted_card.path)
                    for m in msg:
                        msg[m] = ["{} odkrył kartę.".format(players[player].name),
                                  "Zostało jeszcze: {} kart".format(len(deck) - 1)]
                    if len(deck) == 0:
                        deck = init_card_deck()
                data_to_send = (players, deck, msg[player])
            conn.send(pickle.dumps(data_to_send))
            msg[player] = ""
        except:
            break
    global currentPlayer
    players.pop(player)
    pool_of_players.append(player)
    pool_of_players.sort()
    currentPlayer = pool_of_players[0]
    print("Lost connection")
    conn.close()


def runSerwer():
    global currentPlayer
    while True:
        if currentPlayer < MAX_PLAYERS_NUMBER:
            conn, addr = s.accept()
            print("Connected to: ", addr)
            print("Player {} just joined".format(currentPlayer))
            start_new_thread(threaded_client, (conn, pool_of_players[0]))
            pool_of_players.remove(pool_of_players[0])
            currentPlayer = pool_of_players[0]


start_new_thread(runSerwer, ())

while True:
    x = input('Czekam na komende: ')
    if x == "new deck":
        deck = init_card_deck()
