import os, time
for i in range(6):
    time.sleep(0.2)
    os.mkdir(str(i))
for i in range(6):
    time.sleep(0.2)
    os.rmdir(str(i))