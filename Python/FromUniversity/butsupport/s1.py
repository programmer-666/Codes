c1 = "Ondokuz Mayıs Üniversitesi"
girilecekharf = input("Aranacak Harf:")
c2 = 0
for i in c1:
    if girilecekharf == i:
        c2+=1
print(girilecekharf, c2, "Adet Bulundu")