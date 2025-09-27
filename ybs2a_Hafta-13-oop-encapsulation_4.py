


# Bolumler adında bir class yazın
# öznitelikler => ogrenci_sayisi:int, bolum_ad:str, akreditasyon:True


# YBS adında bir class oluşturun, Bolumler class'ını miras alsın
# kendi öznitelikleri de hocalar:list, dersler:list olsun

#YBS bölümündeki bolum_ad özniteliğini kapsülleyin


class Bolumler:
    def __init__(self,ogrenci_sayisi:int,bolum_ad:str,akreditasyon=True):
        self.ogrenci_sayisi = ogrenci_sayisi
        self.bolum_ad = bolum_ad
        self.akreditasyon = akreditasyon

class YBS(Bolumler):
    def __init__(self, ogrenci_sayisi: int, bolum_ad: str, hocalar:list,dersler:list,akreditasyon=True):
        super().__init__(ogrenci_sayisi, bolum_ad, akreditasyon)
        self.hocalar = hocalar
        self.dersler = dersler

        self.__bolum_ad = bolum_ad
    
    def get_bolum_ad(self):
        return self.__bolum_ad
    
    def set_bolum_ad(self,yeni_deger):
        self.__bolum_ad=yeni_deger

ybs_1 = YBS(42,"YBS",["Furkan","Mahmut"],["OOP","İstatistik 1"])

print(ybs_1.get_bolum_ad())

#ybs_1.set_bolum_ad("BST")

#print(ybs_1.get_bolum_ad())

ybs_1.set_bolum_ad("BST")
print(ybs_1.get_bolum_ad())


