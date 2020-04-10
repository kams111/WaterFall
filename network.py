import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "25.129.108.254"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.connect()

    def getP(self, data):
        try:
            self.client.send(pickle.dumps(data))
        except:
            print("no nie!")
        return pickle.loads(self.client.recv(2048))

    def connect(self):
        try:
            self.client.connect(self.addr)

        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            data1 = []
            while True:
                packet = self.client.recv(4096)
                data1.append(packet)
                if len(packet) != 4096:
                    break
            return pickle.loads(b"".join(data1))
        except socket.error as e:
            print(e)
