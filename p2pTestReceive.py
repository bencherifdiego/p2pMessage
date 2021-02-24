import socket
import struct
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 54000))

while True:
    msg = sock.recvfrom(1024)
    msg = pickle.loads(msg[0], fix_imports=True, encoding="bytes")
    print (msg)
    
input("...")