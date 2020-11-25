import socket
port = 443
try:
    sc = socket.socket()
    sc.connect(("137.74.187.104", port))
    print(port, str(sc.recv(1024)))
    sc.close()
except:
    print(port, "Closed")
        