# Asal sayı: 1'den ve kendisinde başka sayıya bölünmeyen sayılar. 1'den büyük ve pozitif, minimum 2.
i = 155801
z = 0
with open("primenums.txt", "w") as fop:
    while True:
        i+=1
        f = False
        for x in range(2,i):
            if i % x == 0:
                f = True
        if f == False:
            fop.write(f"{i},")
            print(z)
            z+=1
        