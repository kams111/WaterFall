import socket
from src.constants import *
from src.player import Player
import pickle
from _thread import *
from src.card import *

server = "192.168.1.13"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(MAX_PLAYERS_NUMBER)
print("Waiting for connection, Server Started! Max number of players: " + str(MAX_PLAYERS_NUMBER))

deck = init_card_deck()
players = []
pool_of_players = []
for i in range(MAX_PLAYERS_NUMBER):
    pool_of_players.append(i)
print(pool_of_players)


currentPlayer = 0

def threaded_client(conn, player):
    global deck
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if players[player].isTakeCard():
                    deck.pop(-1)
                    print("Zostało jeszcze: {} kart do odkrycia".format(len(deck)-1))
                    if len(deck) == 0:
                        deck = init_card_deck()
                reply = players.copy()
                reply.remove(players[player])
                data_to_send = (players, deck)
            conn.send(pickle.dumps(data_to_send))
        except:
            break
    global currentPlayer
    currentPlayer -= 1
    players.remove(players[player])
    pool_of_players.append(player)
    pool_of_players.sort()
    print("Lost connection")
    conn.close()

def runSerwer():
    global currentPlayer
    while True:
        if currentPlayer < MAX_PLAYERS_NUMBER:
            conn, addr = s.accept()
            print("Connected to: ", addr)
            players.append(Player(PLAYER_START[pool_of_players[0]][0], PLAYER_START[pool_of_players[0]][1], DEFAULT_R,
                                  PLAYER_START[pool_of_players[0]][2]))
            start_new_thread(threaded_client, (conn, pool_of_players[0]))
            pool_of_players.remove(pool_of_players[0])
            currentPlayer += 1


start_new_thread(runSerwer, ())

while True:
    x = input('Czekam na komende: ')
    print(x)

