class universe:
    __pi = 3.14159265358979323846264338327950288419716
    def __init__(self, r_value):
        self.universe_volume = 4/3*universe.__pi*r_value**3
        self.universe_area = 4*universe.__pi*r_value**2
u = universe(4)
s1 = universe(1)
print(u.universe_volume-s1.universe_volume*60)
