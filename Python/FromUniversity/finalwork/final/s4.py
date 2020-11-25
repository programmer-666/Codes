class restaurant:
    yiyecek = {
        "balık":20,
        "tavk":17,
        "köfte":15
    }
    icecek = {
        "kola":3,
        "ayran":1,
        "su":1
    }
    tatli = {
        "baklava":8,
        "künefe":10,
        "şöbiyet":8
    }
    def __init__(self, czd):
        self.cz = 0
    def yk(self, ss):
        if restaurant.yiyecek[ss]:
            self.cz += restaurant.yiyecek[ss]
    def ik(self, ss):
        if restaurant.icecek[ss]:
            self.cz += restaurant.icecek[ss]
    def t(self, ss):
        if restaurant.tatli[ss]:
            self.cz += restaurant.tatli[ss]
    def hesap(self):
        print(f"Hesabınız: {self.cz}TL")
if __name__ == "__main__":
    m = restaurant(100)
    m.yk("köfte")
    m.ik("kola")
    m.t("künefe")
    m.hesap()