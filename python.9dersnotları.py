 
#Bolumler adında bir class oluşturun
# öznitelikler => bolum_ad

#YBS adında bir class oluşturun
#öznitelikler => ogrenci_sayisi(int), dersler(list)
#hocalar(list),bolum_ad(varsayılan "YBS")
#YBS class'ı Bolumler class'ını miras alacak

#YBS class'ı içerisine instance seviyesinde fonksiyon yazın
# hocaEkle() isimli bu fonksiyon dışarıdan str tipinde parametre alacak
# aldığı bu parametreyi hocalar listesine ekleyip bize döndürecek

#bir de dersSil() adında bir fonksiyon tanımlayın
# bu fonksiyon da dışarıdan aldığı hocanın adı hocalar listesinde varsa
# o değeri silecek ve hocalar listesinin son halini bize döndürecek

class Bolumler:
    yerleske = "ZTYO"
    def __init__(self,ogrenci_sayisi:int,dersler:list,hocalar:list,bolum_ad):
        self.ogrenci_sayisi = ogrenci_sayisi
        self.dersler = dersler
        self.hocalar = hocalar
        self.bolum_ad = bolum_ad
    
    def hocaEkle(self,yeni_hoca:str):
        self.hocalar.append(yeni_hoca)
        return self.hocalar
    
    def dersSil(self,deger_sil:str):
        if deger_sil in self.dersler:
            self.dersler.remove(deger_sil)
            return self.dersler
        else:
            return f"girmiş olduğunuz {deger_sil} isimli ders {self.bolum_ad} bölümüne kayıtlı değil"


ybs_1 = Bolumler(55,["OOP","Orta Düzey"],["Furkan ATLAN","Mahmut TOKMAK"],"YBS")

print(f"Mevcut Hocalar = {ybs_1.hocalar}")

print(f"Ekleme işleminden sonra hocalar:\n{ybs_1.hocaEkle('Adnan KALKAN')}")


print("-"*50)

print(f"Mevcut Dersler = {ybs_1.dersler}")

print(f"Ders silme sonrası dersler = {ybs_1.dersSil('Orta Düzeyy')}")
#Öğrenci tablosu:
# no, ad, soyad, bölüm, sınıf, dersler, iletişim bilgileri ...a
# numara, ad ,soyad üm öğrencilerde farklıdır (bu 3 öznitelik tek bir tabloda olsun)
# bu tablonun adı da ogrenci_isim

#bölüm (okuldaki tüm bölümleri belirtir o halde sadece bölümleri barındıran bir tablo olsun)

# sınıf => Hazırlık, 1, 2, 3, 4 (o zaman sadece sınıf bilgisinin tutulduğu bir tablo)

# dersler için de ayrı bir tablo (ancak, ders ya da bölüm birbirlerinin tablosunda tanımlanacak)


#kapsülleme-------2. kısım

# Encapsulation (Kapsülleme)
# projemizin kodlarına dışarıdan erişimin kısıtlanması için
#kullanılan bir OOP ayağıdır.

class Calisanlar:
    def __init__(self,ad,soyad,departman,maas,zam_orani=0.5):
        self.ad = ad
        self.soyad = soyad
        self.departman = departman
        self.maas = maas
        self.__zam_orani = zam_orani#instance seviyesinde değiştirebilirDim ama daha önce claas seviyesinde tanımlandıysa yine claas seviyesindeki şeklinde kalır instance kendi içinde değiştirdiğini kullanır
    #neyi kapsüllemek istiyorsak(zam_oranı).dışarıdan biri değiştiremiyor
    def get__zam_orani(self):#kapsüllemek istedğimizi İçin yaptık 
        return self.__zam_orani
    
    def set__zam_orani(self,yeni_zam):#tekrardan dışarıdan değer vermek için yaptık.yeni değer vereceğimiz için parametre aldık selfin yanına
        self.__zam_orani = yeni_zam#__ tam koruma sağlar.
    


c1 = Calisanlar("Furkan","ATLAN","YBS",50000)#instance seviyesinde bir attribute

print(c1.get__zam_orani())

#$ßc1.__zam_orani = 0.9#1
c1.set__zam_orani(0.8)#setle erişebiliriz#2 => 1 ve 2 aynı işlevi görür ikisini de kullanabilirsin

print(c1.get__zam_orani())

#-3. kısım-----------------------------------------------------------------------

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
    
    def get__bolum_ad(self):
        return self.__bolum_ad
    
    def set__bolum_ad(self,yeni_deger):
        self.__bolum_ad=yeni_deger

ybs_1 = YBS(42,"YBS",["Furkan","Mahmut"],["OOP","İstatistik 1"])

print(ybs_1.get__bolum_ad())

#ybs_1.set_bolum_ad("BST")

#print(ybs_1.get_bolum_ad())

ybs_1.set__bolum_ad("BST")
print(ybs_1.get__bolum_ad())



