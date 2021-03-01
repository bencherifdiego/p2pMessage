import socket
import pickle
import threading



class sendMsg(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        name = input("input your name: ")

        while True:
            msg = input()
            data = pickle.dumps(name + ": " + msg, 0)

            sock.sendto(data, ('255.255.255.255', 54000))

class recvMsg(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('127.0.0.1', 54000))

        while True:
            data = sock.recvfrom(1024)
            msg = pickle.loads(data[0], fix_imports=True, encoding="bytes")
            print(msg)

threadSend = sendMsg()
threadSend.start()

threadRecv = recvMsg()
threadRecv.start()

input("...")