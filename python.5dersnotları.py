 

# 6. HAFTA => HATA YÖNETİMİ VE SINIF KAVRAMINA GİRİŞ

# Hata Yönetimi
# Python'da Hata Yönetimi Genel olarak 3 yolla ele alınır.
# 1 => try-except
# kod, try bloğu içerisine yazılır, eğer bir hata olacaksa bu hata
# except bloğu içerisinde tanımlanır.
# diğer 2 hata yönetimi türünden farkı, kodun hatalı kısımdan sonra bile
# çalışmasına izin vermesidir.!!!!!!!!!1!!!!!!!

a = 5
b = 8

try:
    #kodun çalışacağı kısım
    print(a+b)
except Exception as e:
    #eğer hata varsa, oluşursa hatanın tipinin yazıldığı kısım
    # hata ile ilgili bilgi verilen kısım
    print(f"Hata tipi = {e}, İsim Hatası aldınız")

# global scope, şu aşamada finally kısmına denk gelir. (try-except'in altında)
# kalan kısım finally bloğudur. Her halükarda çalışır
# Kod hata verse de vermese de !!!1!!!!!!1!1!!!!!!!!
print("Kod çalıştı")

# 2. hata yönetimi tipi => Assertion Error (assert)
# Genellikle python'da tip-versiyon kontrolünde
# versiyon uyuşmazlıklarını tespit etmek için kullanılır

# Aşağıdaki 3 kod satırı yorum haline getirildi
# Çalışacağınız zaman yorum satırlarını kaldırın
bilgi = input("Lütfen isminizi giriniz: ")
assert bilgi=="Furkann", "Girilmesi gereken bilgi Furkann olmalıdır"
print(f"Hoşgeldiniz {bilgi}")

# assert ifade == True olarak algılanır
# asser kelimesinin yanındaki ifade doğru ise alt satırdaki kodları çalıştırır
# değilse ya hata verir (AssertionError) ya da assert'in sağında tanımlanan
# hata mesajını verir (AssertionError: Hata Mesajı)!!!!!!!!!!!!!!!


# input fonksiyonu varsayılan olarak str tipinde değer döndürür
# Hangi tipte veri girerseniz girin str tipinde döndürür!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Aşağıda yorum satırı haline getirilmiş kodları, çalışırken açınız
deger = int(input("Lütfen bir sayı giriniz: "))

deger = input("Lütfen bir sayı giriniz: ")
deger = int(deger)
assert type(deger)==int, "int tipinde bir tamsayı giriniz"
print(f"Girmiş olduğunuz sayı = {deger}")

# Kullanıcında 2 sayı girişi alınız. Bu sayıların toplamının yarısı
# ortalaması 50'den küçükse hata verecek ve kaldınız yazacak, 
# alt satırdaki print kodu çalışsın ve geçtiniz yazsın

sayi1 = int(input("Lütfen 1. sayıyı giriniz: "))
sayi2 = int(input("Lütfen 2. sayıyı giriniz: "))

ortalama = (sayi1+sayi2)/2

assert ortalama>50, f"Ortalamanız = {ortalama}, Kaldınız"#şartı assert te tanımlıyorum
print(f"Ortalamanız = {ortalama}, Geçtiniz")
#50yse geçtin direkt alt atıra geç 1. şart. kaldınız 2. şart yani değilse demiş gibi olduk
#kodun devamına bir şey yazsak üstte hata verdiyse alt satırlara geçmez!!!!!!!,try except geçer .tüm satırlara


# try-except ile assert'in farkı:
# try-except Hata verse de vermese de döngünün dışında olan yani kendi
# kapsamının dışında olan (alt satırlardaki) kodları her halükarda ÇALIŞTIRIR
# assert'te ise eğer assert'in yanındaki ifade True sonucunu döndürmüyorsa
# o zaman assert'in yanındaki hata mesajını yazar ve kodun alt satırlarını
# ÇALIŞTIRMAZ. Kod o satırda kırılır.!!!!!!!!

# 3. hata yönetimi türü => raise

sayi = 50

# if sayi<40:
if sayi<40:
    print("Bu sayı 40'tan küçüktür")
else:
    #print("Bu sayı 40'tan büyüktür")
    raise Exception("Lütfen 40'tan büyük bir sayı giriniz")

print("Kod sonrası çalıştı")
#kendinden sonraki blokları çalıştırmaz.çalıştıran sadece try excep tir.

# SINIF KAVRAMI

# Python'da OOP (Object Oriented Programming) konsepti, bir şablon olarak
# işlev görür. Biz, benzer özellikleri taşıyan yapıları ayrı ayrı tanımlamak,
# oluşturmak yerine tek bir yapıda toplarız. Diğer benzer özellikleri taşıyan
# yapılar aynı olan özelliklerini ondan miras alır, farklı olan özelliklerini
# kendileri tanımlar

# sınıf class anahtar kelimesi ile tanımlanır

class ZTYO():
    def __init__(self,sinif,sube,ogrenciSayi,hoca):
        self.benimsinif = sinif#sınıfı benim sınıf içine attım
        self.sube = sube
        self.ogrenciSayi = ogrenciSayi
        self.hoca = hoca

class YBS(ZTYO):
    pass#iki noktadan sonra alt satıra herhangi bir şey yazmayacaksak pass kullan

# FONKSİYON ÖRNEKLERİ

# 1 ile 250 arasında 8'e bölünen ama 6'ya bölünmeyen sayıları yazan fonk

def ornek1():
    for i in range(1,251):
        if i%8==0 and i%6!=0:
            print(i)

ornek1()#fonksiyonu burda çağırdık.
 
# 1 ile 350 arasında 5'e bölünen ama 2'ye bölünmeyen sayıları yazan fonk

def ornek2():
    for i in range(1,351):
        if i%5==0 and i%2!=0:
            print(i)

ornek2()

# Dışarıdan verilen bir vize not listesinin içindeki her bir değerin
# yüzde kırkını hesaplayan ve bu değeri boş bir listeye ekleyip en sonda da
# döndüren fonksiyonu yazınız

def ornek3(my_list: list):#list olarak tipinibelirtmiş olduk
    bos_liste = []

    for i in my_list:#parametre olarask belirttiğim şey üzerinde işlem yapıyorum
        bos_liste.append(i*0.4)
    return bos_liste

print(ornek3([50,85,35,40,90]))

# Dışarıdan verilen bir vize not listesinin içindeki her bir değerin
# eğer yüzde kırkı hesaplanmış değer 30'dan küçükse listeye "Kaldı" yazsın
# değilse "Geçti" yazsın


def vizeNot2(my_list:list):#o anki hayali bir parametre olarak tanımladık.bilgisayarın değer tutması için.geçici olarak tuttu.
    bos_liste = []#değer döndürmeyi istiyorsa direkt boş bir liste tanımla başta.geçici işlem yapmak için liste oluşturdum
    
    for i in my_list:#forla hesaplamayı hayali olarak tuttuğumuz parametreyi kullanarak yaptık

        if i*0.4<30:
            bos_liste.append("Kaldı")
        else:
            bos_liste.append("Geçti")
    return bos_liste

print(vizeNot2([50,85,35,40,90]))





