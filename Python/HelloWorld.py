#!/usr/bin/python3
import os, time
sym = ["|", "/", "-", "\\"]
i = 0
while True:
    print("*", sym[i], "Hello Pandemic", sym[i], "*", "\n\n")
    i+=1
    if i >= len(sym):
        i = 0
    time.sleep(0.1)
    os.system("clear")