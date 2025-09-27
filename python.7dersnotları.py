

class Personel:

    #aşağıdaki attribute (öznitelik), class seviyesinde bir attribute'dir.
    # Bunun anlamı, sadece class düzeyinde ona erişim sağlanır.

    zam_orani = 0.7

    def __init__(self,ad,soyad,departman,maas):#ilk parametre kime ait olduğunu göasterir.self yani
        self.ad = ad
        self.soyad = soyad
        self.departman = departman
        self.maas = maas
    
# class'tan türetilen herşey birer instance (örnek) olarak tanımlanır.
# Aşağıdaki p1 bir instance'dir.

p1 = Personel("Furkan","ATLAN","YBS",50000)

p1.zam_orani = 0.5
print(p1.zam_orani)#selfi p1 olarak tanımladık. her şeyini p1 temsil ediyor.artık self p1in kendisi selfin yaptığı her şeyi p1 yapabilir0.5
print(Personel.zam_orani)#0.7

# YBS isminde bir class tanıımlayın.
# class seviyesinde yerleske isminde bir attribute'ye sahip olacak ve bunun değeri
# 'Bucak ZTYO' olacak

# constructor metodundaki parametreler:
# yil, donem, hoca, ders olacak.
# ders parametresi birden fazla değer alabileceği için list tipinde olacak

class YBS:
    yerleske = "Bucak ZTYO"#class seviyesinde  bir attribute

    def __init__(self, yil, donem, hoca, ders:list):#consructor metodunu tanımlayıp parametre verdik#yıla burda erişmedik
        self.yil = yil#sonradan kullanmak için tuttuk#yıla burdan erişebiliyoruz.#bizi ilgilendiren year.
        self.donem = donem
        self.hoca = hoca
        self.ders = ders
    
    def dersEkle(self,yeni_ders):
        return self.ders.append(yeni_ders)
          #return self.ders
    
    def dersSil(self):
        #return del self.ders[-1]
         return self.ders.pop()
       #  return self.ders
        
    

ybs1 = YBS(4,"Bahar","Furkan ATLAN",["OOP","Orta Düzey Programlama","VTYS"])

print(f"Ders listesi ilk hali = {ybs1.ders}")
print("-"*50)

ybs1.dersEkle("Matematik 2")

print(f"Ders listesi Güncellenmiş hali = {ybs1.ders}")

ybs1.dersSil()

print(f"Ders listesi Son hali = {ybs1.ders}")
# instance seviyesinde bir fonksiyon yazın
# fonksiyonun adı dersSil
# çalıştırıldığı zaman listedeki son dersi silecek
#2. kısım---------------------

# OOP'de Inheritance (miras, kalıtım)

# miras alma, bir sınıfın başka bir sınıfın ya da sınıfların bütün özelliklerini
# fonksiyonlarını ve başlangıç parametrelerini (constructor parameters)
# olduğu gibi aynen miras almasıdır (kendine kopyalamasıdır)

# aşağıdaki tanımlama ile inheritance işlemi yapılır
# class Miras_Alan_Class_Adı(Miras_Alınan_Class_Adı)

# Inheritance işleminde bilinmesi gerekenler:
# 1) Ana class'tan yani miras alınan class'tan instance türetilmez
# (Güvenlik açığı ve verimlilik nedeniyle)

# 2) Miras alan sınıf, genellikle kendine has özellikleri (attribute)
# ve işlevleri (fonksiyon) sonradan tanımlar
# Bu işlem için de (hangisi ana sınıfa ait, hangisi miras alan sınıfa)
# ayırt etmek için super() isimli bir metod kullanılır


# ZTyo'da bölümler var. YBS, BST vs. 
# her bölümün öğrencisi, hocası, dersi, sınıfı var.

class Departman:#ana klass,parent class denir,miras alınan class.bundam instance(örnek) türetilmez

    def __init__(self, ad, calisan_sayisi, gorev_alani):
        self.ad = ad#adı çağırmak için self.ad yazmamız lazım çünkü adı self.ad ın içine attım
        self.calisan_sayisi = calisan_sayisi
        self.gorev_alani = gorev_alani
    
    def bilgiGetir(self):
        return f"Departman adı = {self.ad}, Çalışan sayısı = {self.calisan_sayisi}"

class IT(Departman):#miras alan sınıf,kendine has özellikleri(attribute)sonradan tanımlar
    
    def __init__(self, ad, calisan_sayisi, gorev_alani, maas):#constructor yapıcı metod
        super().__init__(ad, calisan_sayisi, gorev_alani)
        self.maas = maas
    
    def bilgiGetir(self):
        return f"Departman adı = {self.ad}, Çalışan sayısı = {self.calisan_sayisi}, Maaş Ortalaması = {self.maas}"
    

it_1 = IT("IT",50,"Bilişim",50000)#it deki gelir
print(it_1.ad)
print(it_1.bilgiGetir())# fonkiyonu çağırdım.

# iki sınıf arasında miras alma yoluyla bir ilişki olduğu zaman,
# o sınıfların her ikisinde de aynı isimde ve aynı parametrelere sahip
# fonksiyonlar olması durumunda hangisinn geçerli olacağı
# polymorphism (çok biçimlilik) konsepti ile açıklanır.
# Aynı durum, özellikler (attribute) için de geçerlidir


# Bolum adında bir class tanımlayın
# yerleske isminde class seviyesinde attribute olacak
# constructor metodda ad, ogrenci_sayisi, donem parametreleri olacak
# Ayrıca, instance seviyesinde kalanOgrenci isminde bir fonksiyon olacak
# bu fonksiyon dışarıdan girilen bir not 50'nin altında ysa "KALDI", değilse
# "GEÇTİ" değeri döndürecek

# bolum class'ını miras alan YBS adında bir class daha olacak
# bu class'ın hocalar isminde liste tipinde bir constructor parametresi olacak
# ayrıca kalanOgrenci fonksiyonunda geçme notu olarak 65'i baz alacak
# yani, dışarıdan girilen not 65'in altındaysa "KALDI", değilse "GEÇTİ"
# değerini döndürecek


class Bolum:
    yerleske = "ZTYO"#class seviyesinde attribute

    def __init__(self, ad, ogrenci_sayisi, donem):#constructor yapıcı metod yani
        self.ad = ad
        self.ogrenci_sayisi = ogrenci_sayisi
        self.donem = donem
    
    def kalanOgrenci(self, ogr_not):
        if ogr_not<50:
            return "KALDI"
        else:
            return "GEÇTİ"

class YBS(Bolum):
    
    # inheritance (kalıtım, miras alma) örneği
    def __init__(self, ad, ogrenci_sayisi, donem, hocalar:list):
        super().__init__(ad, ogrenci_sayisi, donem)
        self.hocalar = hocalar
    
    # polymorphism (çok biçimlilik) örneği
    def kalanOgrenci(self,ogr_not):# foonksiyonun adı ve parametreleri aynı o yüzden içini istediğim gibi doldurdum
        if ogr_not<65:
            return "KALDI"
        else:
            return "GEÇTİ"

ybs1 = YBS("Yönetim Bilişim Sistemleri",45,"Bahar",["Furkan ATLAN","Mahmut TOKMAK"])

print(ybs1.hocalar)
print("-"*50)
print(ybs1.kalanOgrenci(70))



