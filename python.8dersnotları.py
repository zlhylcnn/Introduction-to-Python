
#parametre_adı:parametrenin_tipi
# miras alınan class'lardan nesne (örnek-instance) türetilmez

# Inheritance (kalıtım,miras alma), bir sınıfın başka bir sınıfın tüm özelliklerini ve 
# işlevlerini (fonksiyonlarını) olduğu gibi kendine kopyalamasıdır

# Polymoprhism ise miras alan-miras alınan sınıflar arasında !aynı isme ve aynı parametreye!
# sahip olan fonksiyonların değerlerinin (içeriğinin) değiştirilmesidir

#Polymorphism'de eğer miras alan sınıf tarafından fonksiyonların içeriği değiştirilmezse
#varsayılan olarak miras alınan sınıfın çıktıları üretilir.

#Polymorphism, zaten aynı isim ve parametrelere sahip fonksiyonların miras alan sınıflar
#tarafından kendi ihtiyaçlarına göre değiştirilmesidir.

class Bolum:
    def __init__(self,bolum_ad,hocalar:list,dersler:list):

        self.bolum_ad = bolum_ad#bölüm_adı self.bolum_ad içine attım çağırırken soldaki ifadeyi kullan
        self.hocalar = hocalar
        self.dersler = dersler
    
    def bilgiGetir(self):
        return f"Bölüm class'ı oluşturuldu"


class Ogrenci(Bolum):
    # miras alan class'ın (Ogrenci) constructor (__init__) metodu tanımlanırken
    # ilk olarak kendisinin constructor metodu yazılır
    def __init__(self, ad,soyad,numara,bolum_ad, hocalar: list, dersler: list):#Ogrenci'nin constructor metodu
        super().__init__(bolum_ad, hocalar, dersler)#Bolum'un constructor metodu
        self.ad = ad#self.year=yıl , deseydim çağırırken  self.year demem lazım çünkü yılı self.yearın içine attım.
        self.soyad = soyad
        self.numara = numara
    
    def bilgiGetir(self):
        return f"Öğrencinin adı = {self.ad}, soyadı = {self.soyad}"#self.ad olarak çağırdım çünkü adı =operatörü ile self.ad ın içine attım

ogr_1 = Ogrenci("Ahmet","YILMAZ",1312506018,"YBS",["Furkan ATLAN","Mahmut TOKMAK"],["OOP","Kodlama"])#ogrenci claas ındaki constructor metodundaki parametrelere göre yazdım.

# ogr_1 instance'ye karşılık gelir.


print(ogr_1.bilgiGetir())

#sor!
class Deneme(Ogrenci):
    def bilgiGetir(self):
        return super().bilgiGetir()

deneme_1 = Deneme("Ahmet","YILMAZ",1312506018,"YBS",["Furkan ATLAN","Mahmut TOKMAK"],["OOP","Kodlama"])

print(deneme_1.bilgiGetir())

#2. kısım------------------------------------------------------------------------------------------------------------------------------------------------------
        

#Departman adında class oluşturun.
# bu class'ın özellikleri (attributes): (Aşağıda)
# departman_ad, departman_yonetici, eleman_sayisi, eleman_maas
# maasHesapla isminde instance seviyesinde bir fonksiyon yazın
# bu fonksiyon dışarıdan değer almayacak ve çalışanın maaşına yüzde 60 zam yapmak
# üzere tasarlanmış olacak.

class Departman:
    def __init__(self,departman_ad,departman_yonetici,eleman_sayisi,eleman_maas):
        self.departman_ad = departman_ad
        self.departman_yonetici = departman_yonetici
        self.eleman_sayisi = eleman_sayisi
        self.eleman_maas = eleman_maas#eleman_maas ifadesini self.eleman_maas içine attım
    
    def maasHesapla(self):#instance seviyesinde bir fonksiyon
        return (self.eleman_maas * 0.6)+self.eleman_maas#zamlı maaşı bulurum

# Muhasebe adında bir class tanımlayın
# bu class, Departman class'ını miras alacak.
# Ek olarak, Muhasebe class'ının evrak_giderleri adında bir özelliği (atttribute) olacak
# Bunun yanında, Muhasebe class'ının maasHesapla() fonksiyonunda maaş zaman oranı
# yüzde 60 yerine yüzde 55 olarak hesaplanacak
#!anla  

class Muhasebe(Departman):
    def __init__(self, departman_ad, departman_yonetici, eleman_sayisi, eleman_maas,evrak_giderleri):
        super().__init__(departman_ad, departman_yonetici, eleman_sayisi, eleman_maas)
        self.evrak_giderleri = evrak_giderleri

    def maasHesapla(self):
        return (self.eleman_maas * 0.55) + self.eleman_maas#zam oranı değişti sadece


m1 = Muhasebe("Muhasebe","Nagihan Hoca",10,45000,1500)
print(f"Mevcut maaş : {m1.eleman_maas}")
print(f"Zamlı maaş : {m1.maasHesapla()}")
# 2 önemli husus:
# 1. si yazdığınız dilin (programlama dilinin) syntax yapısı (söz dizimi)
# 2. si yapılması istenen işlevlerin sırası


#3. kısım---------------------------------------------  --------------------------------------------------------------------------------------------------------

# Departman adında bir class tanımlayın
# bu class'ın maas_orani isminde bir class seviyesinde özniteliği olacak
# bu classın: departman_ad, eleman_sayisi, isminde özniteliği olacak (instance)

class Departman:
    maas_orani = 0.5#claas seviyesinde attribute(öznitelik)

    def __init__(self,departman_ad,eleman_sayisi):
        self.departman_ad = departman_ad#instance seviyesinde öznitelik
        self.eleman_sayisi = eleman_sayisi
    
# IT isminde bir class oluşturun.
# bu class Departman class'ını miras alacak.
# maas_orani özniteliğini yüzde 65 olarak değiştirin
# IT class'ının contructor (yapıcı metod) metodunda departman_ad özelliği
# varsayılan olarak "IT" yazılacak

class IT(Departman):
    maas_orani = 0.65

    def __init__(self, eleman_sayisi, departman_ad="IT"):
        super().__init__(departman_ad, eleman_sayisi)

# Personel isminde bir class yazın
# IT class'ını miras alacak
# maas_orani %62 olacak
# eleman_maas isminde bir öznitelik olacak (instance seviyesinde)
# Personel class'ına özel zamHesapla isminde bir fonksiyon yazın
# maas_orani özniteliği ile mevcut maaşı zamlı olarak hesaplayacak
# personelden bir adet instance üretin ve değeleri gösterin

class Personel(IT):
    maas_orani = 0.62#claas seviyesinde bir öznitelik

    def __init__(self, eleman_sayisi, eleman_maas, departman_ad="IT"):#kendisi
        super().__init__(eleman_sayisi, departman_ad)#miras aldığı
        self.eleman_maas = eleman_maas
    
    def zamHesapla(self):
        return (self.eleman_maas*Personel.maas_orani) + self.eleman_maas#zamlı maaşı hesaplar

p1 = Personel(20,50000)
print(p1.departman_ad)
print("-"*50)
print(p1.zamHesapla())
 