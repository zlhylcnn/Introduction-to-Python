


# Abstraction (Soyutlama) => Tam anlamıyla boş bir şablon
# oluşturmak için kullanılır.
# python'un yerleşik (built-in) modüllerinden olan
# abc modülünden miras alınır.

#Abstract class'ın tanımlanmasının 2 yolu vardır:
# 1=> python'un abc modülünün içindeki ABC class'ını miras alması
# 2=> kendi içerisinde abstract method tanımlanması

# bu class'tan instance üretilmez !!!
# bu class'ın hiçbir şeyi kendisi için kullanılmaz
# Ancak ve ancak miras alınır ve miras alan sınıf, bunu kendine
# göre doldurur/değiştirir

from abc import ABC, abstractmethod#abstraction metoddur#abc en fazla  bi kerr miras verilir#instance üretemeyiz.!#bu class kendini feda eden asker veya anne gibi
#kendisiyle ilgili hiçbir işlem yapamyız.pyhonda modüller vardır.yazmazsamçağıramam #abc absratmetdoun kısaltımı

# öncelikle en üst çatı olan sınıfı belirleyin

class Animal(ABC):#animal abcnin bütün özelliklerini çağırır.#kalıtımın konusudur.#ana classsı bi kere miras aldık bitti gitti. bundan sonra abc miras alınır.
    #animaldean hiçbir inatance üretilmez. miras ALAn SINIF BUNU KENdine göre değiştirir.
   #yeni bir fonk siyon üretmedim varolanın içine attım.
    def __init__(self,hayvan_ad,hayvan_ayak_sayisi):
        self.hayvan_ad = hayvan_ad
        self.hayvan_ayak_sayisi = hayvan_ayak_sayisi
    
    @abstractmethod#bir yerde yazıp 67 kre çağırmak gibi falan#bubnun içi boş istesekte dolduyramayız
    def speak(self):
       pass#geçmek.boş bırakmak
    
    @abstractmethod
    def tuy(self):#bunları burada tanımladık dog,cat classlarında bunları yazıp değer girmek zorundayız
        pass
        
#herkes artık animal classına bağlı ortak özellikleri bureada tanımla
#cat dog yaprak animal kök .gövdedşr gibi

class Cat(Animal):
    def __init__(self, hayvan_ad, hayvan_ayak_sayisi):
        super().__init__(hayvan_ad, hayvan_ayak_sayisi)
    
    def speak(self):#speaki yukaruıda(ana class ta)tanımladık  dog,cat classlarında bunları yazıp değer girmek zorundayız.değeri olmasa bile fonksiyonuv yazmakzorundayız 
        return "Kediler miyav diye ses çıkarır"
    
    def tuy(self):
        return "pofuduk"

class Dog(Animal):
    def __init__(self, hayvan_ad, hayvan_ayak_sayisi):
        super().__init__(hayvan_ad, hayvan_ayak_sayisi)
    
    def speak(self):
        return "Köpekler hav diye ses çıkarır"
    
    def tuy(self):
        return "kalın post"

class Sneak(Animal):
    def __init__(self, hayvan_ad, hayvan_ayak_sayisi):
        super().__init__(hayvan_ad, hayvan_ayak_sayisi)
    
    def speak(self):
        return "Yılanlar tıslar"
    
    def tuy(self):
        return "Tüyü yoktur, derisi vardır"

c1 = Cat("Kedi",4)
d1 = Dog("Köpek",4)
s1 = Sneak("Yılan",0)

print(c1.speak())
print(d1.speak())
print(s1.speak())

#2. kısım-------------------------------------------------------------

# MAKU isminde abstract bir class tanımlayın
# bu abstract class'ın özellikleri => yuksekokul(bool),bolumler(list),
# hoca_sayisi(int)

# abstract method olarak da hoca bilgisini ve bölüm sayısını veren
# bilgi() adında method tanımlayın
# yerleske() adında bir abstract method daha tanımlayın
# bu method da yerleşkenin ismini str olarak döndürsün

# ZTYO adında bir class tanımlayın
# MAKU class'ını miras alsın
# abstract methodları ZTYO'nun kendi ihtiyaçlarına göre doldurun

from abc import ABC, abstractmethod

class MAKU(ABC):
    def __init__(self, yuksekokul:bool, bolumler:list, 
                 hoca_sayisi:int):
        
        self.yuksekokul = yuksekokul
        self.bolumler = bolumler
        self.hoca_sayisi = hoca_sayisi
    
    @abstractmethod# @ işareti dekoratördür.
    def bilgi(self):
        pass
    
    @abstractmethod#tek tek yazmamız lazım. tek absractor metodund ayazamayız her fpnksiyondan önce @absteacton yaz.
    def yerleske(self):
        pass
    
class ZTYO(MAKU):
    def __init__(self, yuksekokul: bool, bolumler: list, hoca_sayisi: int):
        super().__init__(yuksekokul, bolumler, hoca_sayisi)
    
    def bilgi(self):
        return f"ZTYO'nun Hoca sayısı = {self.hoca_sayisi}, bölüm sayısı ise = {len(self.bolumler)}"

    def yerleske(self):
        return f"ZTYO, Bucak yerleşkesinde bulunmaktadır"
    
z1 = ZTYO(True,["YBS","BST","Gümrük","Muhasebe","Pazarlama"],20)

print(z1.bilgi())
print(z1.yerleske())
