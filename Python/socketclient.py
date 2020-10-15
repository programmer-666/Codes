import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sct:
    sct.connect(("127.0.0.1", 64095))
    sct.sendall(bytes(input(">"), "utf-8"))
    data = sct.recv(1024)
    print(":{}".format(data.decode()))