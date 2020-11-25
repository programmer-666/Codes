import socket
h, p = "127.0.0.1", 11224
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
    sc.bind((h, p))
    sc.listen(2)
    c, a = sc.accept()
    with c:
        print(a, ": Connected")