import paramiko
cl = paramiko.SSHClient()
cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ul, pl = [], []
for i in ul:
    for j in pl:
        try:
            a = cl.connect("ip", username = i, password=j)
            cl.close()
            print(i, j)
        except:
            pass
