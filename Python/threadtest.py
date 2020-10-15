import threading, time
timeval = float(input("input time (sec): "))
class w0(threading.Thread):
    def run(self):
        global x
        x = 5
        for i in range(x):
            print("a")
            time.sleep(timeval)
class w1(threading.Thread):
    def run(self):
        for a in range(x):
            print("b")
            time.sleep(timeval)
w = w0()
ww = w1()

w.start()
time.sleep(timeval/2)
ww.start()

w.join()
ww.join()