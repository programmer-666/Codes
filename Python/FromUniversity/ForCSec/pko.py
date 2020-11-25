# -*- coding: utf-8 -*-
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.1.105", username = "sshtest", password = "123456")

while True:
    sti, sto, ste = ssh.exec_command(str(input("> ")))
    print(str(sto.read().decode("ascii")))
