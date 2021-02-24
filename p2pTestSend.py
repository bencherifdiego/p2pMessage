import socket
import struct
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    msg = input()
    data = pickle.dumps(msg, 0)
    
    sock.sendto(data, ('255.255.255.255', 54000))

input("...")