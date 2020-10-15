import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sct:
    sct.bind(("127.0.0.1", 64095))
    sct.listen()
    conn, addr = sct.accept()
    with conn:
        print("Connected [{}]".format(addr))
        