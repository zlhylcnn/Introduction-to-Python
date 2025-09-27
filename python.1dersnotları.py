
# Python'da tekli yorum satırı

"""
Python'da çoklu yorum satırı
askjfhaksjf
asfşkassgljsdg
sşdgksdlfjgnlkdfsD 
lajsdfnlkdjagdasasasassas
"""
#Python'da veri tipleri
# 4 adet veri tipi vardır => int ve float (nümerik veriler için)
# str (string) => karakter verileri için (metinsel ifadeler)
# bool veri tipi (mantıksal sonuçlar için) False ya da True

# int veri tipi
# Python'da değişken tanımlama
# Python'da değişken tanımlanırken  veri tipi yazılmaz
# ve kodun sonuna noktalı virgül ya da başka işaret konulmaz

deger = 30
print(type(deger))#değer adlı değişkenin tipini ekrana yazar.
print(deger)

# Python'da matematiksel işlemler
# Toplama +
# Çıkarma -
# Bölme /
# Çarpma *

# Python'da işlem yapmak için önceden değişken tanımlamaya gerek yok
print("*"*50)
print(10+5)
print(10-5)
print(10*5)
print(10/3)

# bölme işleminin sonucu int olarak istiyorsak 2 yol vardır:
# 1. Yol
 
print(int(10/5))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#2. yol bu işaret (/) yerine bunu (//) kullanın!!!!!!!!!!!!!!!!!!!!!!!!!!!        

print(10//5)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

deger2 = 30.452
print(deger2)
print(type(deger2))

print(deger2.is_integer())

#Python'da üs alma işlemi ** ile yapılır
# üssü alınacak sayı ** üs derecesi
print(3*5)#çarpar
print(3**5)#üs alır

# str veri tipi
# Python'daki en güçlü veri tipidir
# Çünkü diğer veri tiplerini de içerisinde barındırır
# Her şey string olarak ifade edilebilir

# str değişken tanımlama 2 şekilde yapılır
# çift tırnak içerisine "" ya da tek tırnak içerisine '' tanımlanır
# çift tırnak içerisine yazılanı kullanın !
deger1 = "değişken 1"
deger2 = 'değişken 2'

print(deger1)
print(deger2)
print(type(deger1))
print(type(deger2))

deger3 = "Makü'nün bölümü"
print(deger3)

#Python'da str içerisinde özel karakterler vardır
# örnek / /n /t
# \n yeni satır demektir (alt satıra geçer)
# \t bir tab boşluk bırakır (3-4 defa boşluk tuşuna basılmış gibi)

deger4 = "disk c\nMasaüstü"
print(deger4)

deger5 = "isim\t\t\tsoyisim"
print(deger5) 

print(10)#int
print("10")#string
print("10.568")#string
print("False")#string

# str içerisinde matematiksel işlemler yapılabilir
# Toplama ve çarpma işlemi yapılır

# str ile toplama işlemi

print("Makü ZTYO YBS 2. sınıf")

a = "Makü "
b = "ZTYO "
c = "YBS "
d = "2. sınıf"
print(a+b+c+d)

# str içerisinde çarpma işlemi
print(10*5)
print("-"*10)

# str class'ında slicing (dilimleme, parçalama) işlemi

deger1 = "Burdur Mehmet Akif Ersoy Üniversitesi"
print(len(deger1))

# dilimleme işlemi [:] ifadesi ile yapılır.
# [başlangıç  indeksi:bitiş indeksi]
# başlangıç indeksi dahildir, bitiş indeksi değeri dahil değildir
# Python'da indeksleme işlemi 0'dan başlar
# yani ilk karakterin, item'in indeks değeri 0'dır
print("-"*50)
print(deger1)
print(deger1[:5])
print(deger1[5:10])
# dilimleme işleminde [:] sadece bir adet iki nokta işareti olursa
# bunun anlamı [başlangıç değeri:bitiş değeri]
# [::] iki tane iki nokta olursa bunun anlamı
# [başlangıç:bitiş:artış (step)]

print("*"*50)
print(deger1[::])
print(deger1[::2])

# bu aşamaya kadar olan slicing işlemi soldan sağa yani
# pozitif değerler ile yapılıyordu
# negatif değerlerle de slicing işlemi yapılabilir
# python'da bir koleksiyonun ilk değeri [0] sıfırıncı indekstedir
# son değeri -1 eksi birinci indekstedir

print("-"*50)
print(deger1)
print(deger1[0])
print(deger1[-1])
print(deger1[::-1]) # tersten yazdırma.son değeri yazdırır.-1. indextedir
print(deger1[-5:-1])

# bool veri tipi
# iki veri türü var False (0) ve True (1)

print("-"*50)
print(bool(0))
print(bool(1))

# Kontrol yapıları
# if elif else
# python'da yukarıdaki 3 ifade ile kontrol yapısı sağlanabilir

sayi1 = 15
sayi2 = 10

if sayi1 == sayi2:
    print("eşittir")

else:
    print("eşit değil")

print("-"*50)

print(sayi1==sayi2)#eşit mi diye kontrol ediyor
print(15==10)#eşit mi diye kontrol ediyor eşit değilse false, eşitse true yazar

print(id(sayi1))
print(id(sayi2))

# == Eşittir işleminin sözel karşılığı is anahtar kelimesidir
# != Eşit değildir işleminin sözel karşılığı is not anahtar kelimesidir
print(15 is 10)
print(15 is not 10)

# and (ve) işlemi and anahtar kelimesi ile yapılabilir
# or (veya) işlemi or anahtar kelimesi ile yapılabilir

print("-"*50)
print(15 is 10 and 15 is 15) # and işleminde tüm şartların True olması gerek
print(15 is 10 or 15 is 15) # or işleminde sadece 1 şartın True olması gerek
# İşlemin sonucunun True gelmesi için


print("-"*50)
deger = "Burdur Mehmet Akif Ersoy Üniversitesi"

# [başlangıç değeri:bitiş değeri] 0'dan başlar bitiş değerine kadar
# bitiş değeri dahil değil
print(deger)
print(deger[5:10])

# [başlangıç:bitiş:artış değeri (step sayısı)]
print("-"*50)
print(deger[::])
print(deger[::2])

# bu aşamaya kadar olan soldan sağa pozitif sayılarla dilimleme idi.
# bir de sağdan sola negatif sayılarla dilimleme işlemi var.
print("-"*50)
print(deger[::])
print(deger[::2])
print(deger[::-2])

print("-"*50)
print(deger[::1])
print(deger[::-1])

# artış miktarında pozitif sayı ile negatif sayının karşılığı yani
# çıktısı aynıdır. Sadece sıralamaları birbirine göre terstir

# ters sıralama slicing işlemi böyle yapılır

#2. kısım------------------------------------------------------------------------------------------------------------------------------------------------

# Bu bir yorum satırıdır

"""
Bu bir
çoklu yorum satırı
örneğidir
"""

# Python'da int ve float değişkenler
print("Python'da int ve float değişkenler")

deger1 = 10
deger2 = 20.0

print(deger1)
print(deger2)

print("-"*50)

# Python'da değişkenin tipini öğrenmek
print("Python'da değişkenin tipini öğrenmek")

print(type(deger1))
print(type(deger2))
print("-"*50)

# Python'da Matematiksel işlemler
deger1 = 20
deger2 = 10

print("Python'da Matematiksel işlemler")
print(deger1+deger2) # Toplama
print(deger1-deger2) # Çıkarma
print(deger1/deger2) # Bölme
print(deger1*deger2) # Çarpma
print(deger1**3) # deger1'in (20) üssünü alma (3. dereceden)
print("-"*50)

# Python'da int değişkenlerin bölümünde int tipinde sonuç elde etmek için
# 1. Yol
print("Python'da int değişkenlerin bölümünde int tipinde sonuç elde etmek için 1. Yol")
print(deger1//deger2)

# 2. Yol
print("Python'da int değişkenlerin bölümünde int tipinde sonuç elde etmek için 2. Yol")
print(int(deger1/deger2))
print("-"*50)

# Python'da değişken tanımlamadan matematiksel işlemleri kullanımı
print("Python'da değişken tanımlamadan matematiksel işlemleri kullanımı")

print(20+10)
print(20-10) 
print(20//10)
print(20*10)
print(20**3)
print(int(20/25))
#Python'da str veri tipi

deger1 = "Bu bir str tipinde değişkendir"
deger2 = 'Bu da str tipinde bir değişkendir'

print("Python'da str veri tipi")

print(deger1)
print(deger2)
print(type(deger1))
print(type(deger2))
print("-"*50)

# Python'da kesme str veri tipinde kesme işareti kullanımı
print("Python'da kesme str veri tipinde kesme işareti kullanımı")

deger = "Türkiye'nin başkenti Ankara'dır"
print(deger)
print("-"*50)

deger1 = "1. Satır \n 2. Satır"
deger2 = "Bir tab kadar \t boşluk"

print(deger1)
print(deger2)
print("-"*50)

# str veri tipinde kullanılan fonksiyonlar 
print("str veri tipinde kullanılan fonksiyonlar")
#*******************************************************************
# Arka arkaya fonksiyon kullanımı
print("str veri tipi için Arka arkaya fonksiyon kullanımı")

print(deger)
print(deger.upper())
print(deger.upper().replace("I","İ"))
print("-"*50)

# str veri tipinde matematiksel işlemler-toplama işlemi
print("str veri tipinde matematiksel işlemler-toplama işlemi")

a = "Burdur "
b = "Mehmet "
c = "Akif "
d = "Ersoy "
e = "Üniversitesi"

print(a+b+c+d+e)
print("-"*50)


# str veri tipinde matematiksel işlemler-çarpma işlemi
print("str veri tipinde matematiksel işlemler-çarpma işlemi")

deger = "a"
print(deger*10) # değişken tanımlayıp 10 defa a yazdırmak
print("a"*10) # değişken tanımlamadan direkt 10 defa a yazdırmak
print("-"*50)

# str veri tipinde f formatlama işlemi
print("str veri tipinde f formatlama işlemi")

print(f"{a}{b}{c}{d}{e} {18} yaşında")
print("-"*50)


# str veri tipinde slicing (dilimleme) işlemi
print("str veri tipinde slicing (dilimleme) işlemi")

deger = "Burdur Mehmet Akif Ersoy Üniversitesi"
print(deger) # deger değişkenin içerisindeki ifade
print(len(deger)) # deger değişkeninin uzunluğu (37 karakter uzunluğunda)
print(deger[0]) # deger değişkeninin ilk elemanı
print(deger[36]) # deger değişkeninin son elemanı
print(deger[-1]) # deger değişkeninin son elemanı
print("-"*50)

print(deger) # deger değişkeninin tamamını yazar
print(deger[:]) # başlangıç-bitiş değeri belirtilmezse tamamını yazar
print(deger[:5]) # başlangıç değeri belirtilmezse 0 kabul edilir
print(deger[3:10]) # başlangıç-bitiş belirtilirse ilgili yerleri yazar 
print("-"*50)


print(deger) # tamamını yazdırır
print(deger[:]) # tamamını yazdırır
print(deger[::]) # tamamını yazdırır
print(deger[::1]) # tamamını yazdırır
print(deger[::2]) # yalnızca çift indeks numarasına sahip değerleri yazdırır
print("-"*50)

# str veri tipinde slicing (dilimleme) işlemi-tersten yazma
print("str veri tipinde slicing (dilimleme) işlemi-tersten yazma")

print(deger[::2])
print(deger[::-2])
print("-"*50)

# bool veri tipi
print("bool veri tipi")

print(bool(1))
print(bool(0))
print("-"*50)

#Python'da Kontrol Yapıları
print("Python'da Kontrol Yapıları")

deger1 = 20
deger2 = 10
if deger1>deger2: #deger1 büyükse deger2'den aşağıdaki print yazılacak
    print(f"{deger1} büyüktür {deger2}")

elif deger2>deger1: # else if'in kısaltmasıdır ve 2. bir if koşuludur
    print(f"{deger2} büyüktür {deger1}")

else: # yukarıdaki şartların hiçbiri sağlanmazsa bu blok çalışacak
    print(f"{deger2} eşittir {deger1}")

print("-"*50)

# Python'da Kontrol yapıları
print("Python'da Kontrol yapıları")

print(20>10) # 20 büyüktür 10 (True)
print(20<10) # 20 küçüktür 10 (False)
print(20==10) # 20 eşittir 10 (False)
print(20!=10) # 20 eşit değildir 10 (True)

print("-"*50)

print(20==20)
print(20 is 20)

print(20 != 10)
print(20 is not 10)

print("-"*50)

# Python’da Kontrol Yapıları-sözel ifadeler
print("Python’da Kontrol Yapıları-sözel ifadeler")

print(20>10 and 20>15) # True and True ==> Sonuç True
print(20>10 and 20>30) # True and False ==> Sonuç False
print("-"*50)
print(20>10 or 20==10) # True or False ==> Sonuç True
print(20<10 or 20==10) # False and False ==> Sonuç False

print("-"*50)

# Python'da not kullanımı
print("Python'da not kullanımı")

print(20>10) # 20, 10'dan büyüktür, doğru yani True
print(not 20>10) # cevap True ama not kullandığımız için False oldu
print("-"*50)
print(20==20) # 20 eşittir 20, cevap doğru yani True
print(not 20==20) # cevap True ama not kullandık ve False oldu
print("*"*50)

# Python'da in anahtar kelimesi kullanımı
print("Python'da in anahtar kelimesi kullanımı")

deger1 = "Makü ztyo"
print("Makü" in deger1)#içindeyse true değer döndürür
print("M" in deger1)
print("ty" in deger1)
print("Bakü" in deger1)






