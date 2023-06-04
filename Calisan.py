from Insan import Insan
class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def zam_hakki(self):
        if self.__tecrube < 2:
            return 0
        elif 2 <= self.__tecrube <= 4 and self.__maas < 15000:
            return self.__maas * float(self.__tecrube) / 12
        elif self.__tecrube > 4 and self.__maas < 25000:
            return (self.__maas * float(self.__tecrube)) / 24
        else:
            return self.__maas

    def __str__(self):
        return super().__str__() + f"\nTecrübe: {float(self.__tecrube)/12}\nYeni Maaş: {self.zam_hakki()}"
