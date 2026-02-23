class Kolik:
    def __init__(self, max_jyldamdyk, siymdylyq):
        self.max_jyldamdyk = max_jyldamdyk
        self.siymdylyq = siymdylyq

    def kozgalu(self):
        pass


class Avtokolik(Kolik):
    def kozgalu(self):
        print("Автокөлік жол бойымен қозғалады")


class Poiyz(Kolik):
    def kozgalu(self):
        print("Пойыз рельс бойымен қозғалады")


class Ushaq(Kolik):
    def kozgalu(self):
        print("Ұшақ ауада ұшады")

auto = Avtokolik(200, "5 жолаушы")
poiyz = Poiyz(300, "500 жолаушы")
ushaq = Ushaq(900, "180 жолаушы")

for k in [auto, poiyz, ushaq]:
    k.kozgalu()
    print("Максималды жылдамдық:", k.max_jyldamdyk)
    print("Сыйымдылығы:", k.siymdylyq)
    print()

