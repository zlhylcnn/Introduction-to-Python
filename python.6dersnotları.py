 
# Object Oriented Programming (Nesne Tabanlı Programlama)

# OOP, aynı özelliklere ve işlevlere sahip yapıların tek bir kaynaktan
# beslenmesini sağlar.

# herhangi bir class , class ön eki ile tanımlanır.
# tıpkı her fonksiyonun def ile tanımlanması gibi

class YBS:
    # bu seviyede tanımlanan her attribute (özellik)
    # class seviyesindedir.
    yil = 4 # class seviyesinde örnek bir attribute.sadece ve sadece class değiştirebilir

    # her zaman önce __init__() fonksiyonu ile constructor yani yapıcı metot
    # düzenlenir

    def __init__(self, ad, soyad, ogr_not, hocalar:list):
        #__init() içerisinde tanımlanan her bir değişken
        # bir attribute'dir.
        # Ancak, instance seviyesinde attribute'dirler
        self.name = ad #ad olan parametreyi self.name in içine atıyorum,çağırırken self.name i kullanacağım 
        self.soyad = soyad
        self.ogr_not = ogr_not
        self.hocalar = hocalar


# my_ybs1 = instance'dir. YBS ise class'ın kendisidir.
# instance, sınıf içerisindeki tüm özelliklere (attribute) ve 
# fonksiyonlara ve dahi her şeye erişebilir.
# Birçok şeyi de değiştirebilir.
# Hatta class seviyesindeki özellikleri bile değiştirebilir
# Ancak tüm bu değişimler, sadece o instance'yi ilgilendirir.
# Class seviyesindeki her bir özellik
# class için ilk tanımlandığı hali ile kalır.
# Class ise sadece kendisine ait olan özellikleri görüntüleyip,
# kullanabilir.

# my_ybs1 = instance'dir. YBS ise class'ın kendisidir.
my_ybs1 = YBS("Furkan","ATLAN",80,["Hoca 1","Hoca 2","Hoca 3"])
print(my_ybs1.name)#bu da namei yazdırır 
my_ybs1.yil = 5#o instance yi ilgilendirir. 

print(my_ybs1.yil)
print(YBS.yil)
        
# class adı EGMYO
# class seviyesinde attribute = yerleske_adi
# constructor metodu (instance seviyesindeki attribute'ler)
# ders_adi, egitim_yili, hocalar (liste), bolumler (liste)
# bir tane instance üreterek tüm değerleri kullan

class EGMYO:
    yerleske_adi = "EGMYO" # class seviyesindeki öznitelik.#clas seviyesindeki attriributte,class seviyesindeki öznitelik

    def __init__(self,ders_adi, egitim_yili, hocalar:list, bolumler:list):#constructor yani yapıcı metod.ilk parametre her zaman selftir.unutma,diğer parametreleri bize soru verdi
        self.ders_adi = ders_adi#parametre vs karışıklıkolmasın diye selfin öz niteliğini de parametrelerle aynı veriyoruz
        self.egitim_yili=egitim_yili #instance seviyesinde attribute lerdir
        self.egitim_yili = egitim_yili
        self.hocalar = hocalar
        self.bolumler = bolumler

egmyo_1 = EGMYO("YBS",2024,["Hoca 1","Hoca 2","Hoca 3"],["Bilişim Mühendisliği","Elektrik-Elektronik"])

print(egmyo_1.bolumler)

print("-"*50)

class EGMYO:
    yerleske_adi = "EGMYO" # class seviyesindeki öznitelik

    def __init__(self,ders_adi, egitim_yili, hocalar:list, bolumler:list):
        self.ders_adi = ders_adi
        self.egitim_yili = egitim_yili
        self.hocalar = hocalar
        self.bolumler = bolumler
    
    def bilgiGetir(self):#instance seviyesinde fonksiyon
        return f"Dersin adı = {self.ders_adi},eğitim yılı = 2023-{self.egitim_yili}"
    
    def bolumEkle(self,yeni_bolum):#self ve yeni bölüm parametrelerimiz
        self.bolumler.append(yeni_bolum)
        return self.bolumler
    
myo_2 = EGMYO("BST",2024,["Hoca 4","Hoca 5"],["Grafik ve Animasyon","Yapay Zeka"])
print("-"*50)

print(myo_2.bilgiGetir())
print(myo_2.egitim_yili)
print(myo_2.bolumler)

myo_2.bolumEkle("Web Tasarım")

print(myo_2.bolumler)
# yukarıdaki class için bir instance fonksiyon yazın
# bu fonksiyon yeni bir ders eklemek için kullanılsın
# geriye bolum değişkenini döndürecek

"""
class YBS2A:
     bolum_adi="YBS2A"

     def __init__(self,bolum_adi):
        self.bolum_adi=bolum_adi
     def bilgi_Getir2(self):
          return f"bölümün adı={self.bolum_adi}"
YBS_2A=YBS2A("nesne tabanlı programlama")
print(YBS_2A.bilgi_Getir2)
#ben  yaptım
"""

print("-"*50)
print("-"*50)


class Personel:
    zam_orani = 0.7
    sayac = 0

    def __init__(self,ad, soyad, yas, maas, departman:list):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.maas = maas
        self.departman = departman
        Personel.sayac += 1#personel.sayac+1 e eşit
    
    def departmanDegis(self,verilendeger):#self, her zaman ver zorunlu
        self.departman.append(verilendeger)
        return self.departman
    
    def departmanSil(self,silinecek_departman_adi):
        self.departman.remove(silinecek_departman_adi)#self.departman diyerek departmana eriştim sonra metodu yazdım remove
        return self.departman
    
    def yasHesapla(self):#aslında dogum yılı hesaplıyor
        return 2024-self.yas
    
    def isimBuyuk(self):
        return self.ad.upper()

# Personel class'ına ait instance method yazın. Bu method,
# personelin departman bilgisini sizin fonksiyonda parametre olarak
# verdiğiniz değer ile değiştirsin (def bolumDegistir(self, yeni_bolum))

p1 = Personel("Furkan","ATLAN",30,30000,["YBS","BST","Muhasebe"])


print(p1.departman)
print(p1.departmanSil("BST"))
p1.departmanDegis("BST")#bu ve üsttki aynı şeyi yapıyor ikisi de oluyor.#bstyi ekler sona
print(p1.departman)

print(p1.yasHesapla())

degisken = p1.ad
print(f"Değişken = {degisken}")


print(p1.isimBuyuk())
#for attribute, value in vars(myo_1).items():
#    print(f"{attribute.capitalize()}: {value}")

#kullanıcın girdiği yaşa göre doğum yılını hesaplayan ve doğum yılını döndüren fonk()
 
isim = "Furkan"
soyisim = "ATLAN"

def isimDegis(yeni_isim, yeni_soyisim):
    isim = yeni_isim
    soyisim = yeni_soyisim 
    return f"{isim}, {soyisim}"

print(isimDegis("Ahmet","ASLAN"))
# maaşa yüzde 70 zam yapan fonksiyonu yazınız
#isim ve soyismin yerini değiştiren fonksiyon

maas = 30000

def zamHesapla():
    return maas + (maas*0.7)
print(zamHesapla())


