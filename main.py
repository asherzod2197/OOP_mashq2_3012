class Hisoblagich:
    def __init__(self):
        self.son = 0

    def oshir(self):
        self.son += 1

    def korsat(self):
        print("🔢 Hozirgi qiymat:", self.son)


h = Hisoblagich()
h.oshir()
h.oshir()
h.korsat()
