import pandas as pd

from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

if __name__ == "__main__":
    # Insan sınıfı için 2 nesne üretme
    insan1 = Insan("11111111110", "Ahmet", "Berke", 19, "Erkek", "Türk")
    insan2 = Insan("22222222220", "Betül", "Demir", 25, "Kadın", "Türk")

    print(f"****************************** Kullanıcı Bilgileri ************************{insan1}\n{insan2}")

    # Issiz sınıfı için 3 nesne üretme
    issiz1 = Issiz("33333333330", "Ahmet", "Kaya", 35, "Erkek", "Türk", {"mavi yaka": 2, "beyaz yaka": 4, "yönetici": 6})
    issiz2 = Issiz("44444444440", "Elif", "Şahin", 40, "Kadın", "Türk", {"mavi yaka": 1, "beyaz yaka": 3, "yönetici": 5})
    issiz3 = Issiz("55555555550", "Fatih", "Yıldız", 45, "Erkek", "Türk", {"mavi yaka": 4, "beyaz yaka": 5, "yönetici": 8})

    print(f"{issiz1}\n{issiz2}\n{issiz3}")
    
    # Calisan sınıfı için 3 nesne üretme
    calisan1 = Calisan("66666666660", "Ali", "Koç", 28, "Erkek", "Türk", "Teknoloji", 36, 12000)
    calisan2 = Calisan("77777777770", "Sude", "Aydın", 32, "Kadın", "Türk", "Muhasabe", 62, 18000)
    calisan3 = Calisan("88888888880", "Kemal", "Kılıçdaroğlu", 75, "Erkek", "Türk", "Siyaset", 71, 22000)

    print(f"{calisan1}\n{calisan2}\n{calisan3}")

    # MaviYaka sınıfı için 2 nesne üretme
    mavi_yaka1 = MaviYaka("99999999990", "İrem", "Yılmaz", 30, "Kadın", "Türk", "Teknoloji", 26, 10000, 1000)
    mavi_yaka2 = MaviYaka("101010101010", "İlkay", "Gündoğan", 35, "Erkek", "Türk", "Futbol", 65, 16000, 1500)

    print(f"{mavi_yaka1}\n{mavi_yaka2}")

    # BeyazYaka sınıfı için 2 nesne üretme
    beyaz_yaka1 = BeyazYaka("111111111110", "Hakan", "Çalhanoğlu", 30, "Erkek", "Türk", "Futbol", 22, 10000, 500)
    beyaz_yaka2 = BeyazYaka("121212121210", "Beril", "Demir", 25, "Kadın", "Türk", "Muhasabe", 48, 15000, 800)

    print(f"{beyaz_yaka1}\n{beyaz_yaka2}")

    # Verileri sözlüğe çevirme
    data = {
        "İşçiler": ["Çalışan","Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka", "Beyaz Yaka"],
        "TC No": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(),beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no()],
        "Ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), mavi_yaka1.get_ad(), mavi_yaka2.get_ad(),beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad()],
        "Soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(),beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad()],
        "Yas": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), mavi_yaka1.get_yas(), mavi_yaka2.get_yas(), beyaz_yaka1.get_yas(),beyaz_yaka2.get_yas()],
        "Cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(),calisan3.get_cinsiyet(), mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(),beyaz_yaka2.get_cinsiyet(),beyaz_yaka2.get_cinsiyet()],
        "Uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), mavi_yaka1.get_uyruk(), mavi_yaka2.get_uyruk(), beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk()],
        "Sektör": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), mavi_yaka1.get_sektor(), mavi_yaka2.get_sektor(), beyaz_yaka1.get_sektor(),beyaz_yaka2.get_sektor()],
        "Tecrübe": [float(calisan1.get_tecrube())/12, float(calisan2.get_tecrube())/12, float(calisan3.get_tecrube())/12,float(mavi_yaka1.get_tecrube())/12,float(mavi_yaka2.get_tecrube())/12,float(beyaz_yaka1.get_tecrube())/12,float(beyaz_yaka2.get_tecrube())/12],
        "Maaş": [calisan1.get_maas(),calisan2.get_maas(),calisan3.get_maas(),mavi_yaka1.get_maas(),mavi_yaka2.get_maas(),beyaz_yaka1.get_maas(),beyaz_yaka2.get_maas()],
        "Yıpranma Payı": [None,None,None,mavi_yaka1.get_yipranma_payi(),mavi_yaka2.get_yipranma_payi(),None,None],
        "Teşvik Primi": [None,None,None,None,None,beyaz_yaka1.get_tesvik_primi(),beyaz_yaka2.get_tesvik_primi()],
        "Yeni Maaş": [calisan1.zam_hakki(),calisan2.zam_hakki(),calisan3.zam_hakki(),mavi_yaka1.zam_hakki(),mavi_yaka2.zam_hakki(),beyaz_yaka1.zam_hakki(),beyaz_yaka2.zam_hakki()]
    }
    
