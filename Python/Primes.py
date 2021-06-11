num = 307
def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) != 0:
                return 1
                break
            else:
                return 0
                break

i = 200000001287
while True:
    for j in range(2, i):
        if i%j == 0:break
    else:
        print(i)
    i+=1