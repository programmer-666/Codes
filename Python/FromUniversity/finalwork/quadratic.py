# -*- coding: utf-8 -*-
# Quaratik denklem
import math
x, y, z = 10, 1, -30

def deltaf(a,b,c):
    return b**2-4*a*c
def x1(a, b, delta):
    return (-b+math.sqrt(delta))/(2*a)
def x2(a, b, delta):
    return (-b-math.sqrt(delta))/(2*a)

if deltaf(x,y,z) > 0:
    print(x1(x, y, deltaf(x, y, z)), x2(x, y, deltaf(x, y, z)))