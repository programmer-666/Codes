# -*- coding: utf-8 -*-
# Tek Çift Uygulaması
t, c = [], []
for i in range(102):
    if i % 2 == 0:
        c.append(i)
    else:
        t.append(i)
print(len(t), len(c))