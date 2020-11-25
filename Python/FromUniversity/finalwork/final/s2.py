c = input("Aranacak karakter: ")
with open("Odev.txt") as fp:
    ct = fp.read()
x = 0
for i in ct:
    if c == i:
        print(x)
        break
    x+=1