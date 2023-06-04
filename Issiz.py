from Insan import Insan
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube_dict):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube_dict = tecrube_dict

    def get_tecrube_dict(self):
        return self.__tecrube_dict

    def set_tecrube_dict(self, tecrube_dict):
        self.__tecrube_dict = tecrube_dict

    def statu_bul(self):
        max_statu = max(self.__tecrube_dict, key=self.__tecrube_dict.get)
        return max_statu

    def __str__(self):
        return super().__str__() + f"\nEn Uygun Statü: {self.statu_bul()}"