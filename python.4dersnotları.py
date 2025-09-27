
# Python'da  FONKSİYONLAR
# fonksiyonlar geriye değer döndüren ve döndürmeyen olarak ikiye ayırılır

# fonksiyon tanımlama kuralı:
# def fonksiyon_adı():

def fonksiyon1():
    print("Bu, geriye değer döndürmeyen bir fonksiyondur")

# Python'da fonksiyonun çağırılması ya da çalıştırılması 2 şekilde olabilir
# 1. yol: doğrudan fonksiyonun adı yazılır ve yanına () işareti konulur
# örnek => fonksiyon1()

# bir fonksiyonda return ifadesi kullanılmıyorsa o fonksiyon geriye
# değer döndürmüyor demektir. Tıpkı aşağıdaki fonksiyon1 gibi
fonksiyon1()
print("BOŞLUK")
print(fonksiyon1())#printle yazdırınca no ne diyor.ekrana değeri yazdırdır.içten dışa doğru yazdırır.bu fonk geriye hangi değeri döndürüyorsa onu istiyoruz.
#ekrana none yazar çğünkü geriye değer döndürmez
# Geriye değer döndüren fonksiyonlar

def fonksiyon2():
    return f"Bu, geriye değer döndüren bir fonksiyondur (2)"


fonksiyon1()
#fonksiyon2()#geriye değer döndürmez
print(fonksiyon2())

##

print("-"*50)
fonksiyon1()
print(fonksiyon2())

print(type(fonksiyon2()))

# fonksiyon çağırma-çalıştırma 2. yol => bir değişkene atayarak çağırma
# fonksiyonun kendisi => fonksiyon2
# fonksiyonun çalıştırılması-sonucu => fonksiyon2()

sonuc = fonksiyon2()

print(f"sonuc = {sonuc}")
#slicing işlemi
print(sonuc[:10])#0.indexten 9. indexe kadar yazar.
# çarpma işlemi (aynı ifadeyi 2 defa yazdırır)
print(sonuc*2)
print("-"*50)
#!!!!1!11!!!!!!1111
#
def degerGetir():
    return ["Makü","ZTYO","YBS",56,78,98.56,True,False]

print(degerGetir())#listeyi olduğu gibi getirdi.printin içinde fonk adı() yaparak çağırdık


print(f"fonksiyonun bellekteki adresi = {degerGetir}")
print(f"fonksiyonun çağırılması, içindeki değerin döndürülmesi= {degerGetir()}") #fonksiyonu çağırdık.
print("-"*50)

my_list = degerGetir()#degerGetir fonksiyonunu liste veri yapısına çevirdik
my_list2 = ["Makü","ZTYO","YBS",56,78,98.56,True,False]

print(f"my_list = {my_list}")
print(f"my_list2 = {my_list2}")

print(my_list[2])#2. indexteki değeri getirir.

def fonksiyon3():
    return 8+5
#anla =>
a = 13 # kendi tanımladığımız değer, 13
b = fonksiyon3() # fonksiyonun döndürdüğü değer = 13

print(a is b) # 13, 13 müdür? diye sorduk? Cevap = True yani evet.#true değer döndürür.

# Parametreli ve Parametresiz Fonksiyonlar
# Parametresiz fonksiyonlar fonksiyon_adı() şeklinde tanımlanır ve parantez içerisi boş olur
# Parametreli fonksiyonlar fonksiyon_adı(parametre1, parametre2) şeklinde   tanımlanır ve parametreler parantez içerisine yazılır,parantez içerisinde parametre değerleri var yani farkı o.



# Parametreli Fonksiyonlar
print("-"*50)

ornek_liste = [1,2,3]#1,2,3 parametre değerleridir.

def sayiTopla(a,b):#a ve b parametrelerdir
    return a+b#temsili parametreler

print(sayiTopla(8,9))#sayıTopla fonksiyonunun 8,9 parametrelerini toplayıp ekrana yazdırdı.
print(type(sayiTopla(8,9)))#sayiTopla fonksiyonunun tipini ekrana yazdırır.

# parametre olarak dışarıdan bir sayı alan ve bu sayının karesini döndüren
# fonksiyonu yazınız

def carpSayi(a):#dışardan alacağım parametre
 return a**2#yapacağım işlem burada

print(carpSayi(6))#ben yaptim
print(type(carpSayi(a)))

def kareal(param1):
    #return param1*param1
    return param1**2

print(kareal(15))

# Python'da dışarıdan değer almak için input() fonksiyonu kullanılır

# Dışarıdan girilen bir sayının tek mi çift mi olduğunu yazan fonksiyon

def tekcift(deger):
    deger = int(input("Lütfen bir sayı giriniz: "))
    if deger%2==0:
        return "Çift Sayı"
    else:
        return "Tek Sayı"

print(tekcift(10))

# for döngüsü kullanılır
# artış miktarı belirlenir, başlangıç değeri buna göre ayarlanır
# döngü yazılır
# eğer sizden geriye bir liste döndürülmesi isteniyorsa
# return kullanın
# sadece değerleri yazmanız istiyorsa print() kullanın

# 10'dan 100'e kadar olan (100'de dahil) sayılardan 10 ile bölümünden kalan
# sıfır olan yani 10'un katı olan sayıları yazan fonksiyonu yazın
print("-"*50)

print("-"*50)
def artis1():
    for i in range(10,101):# 10'dan 100'e kadar olan (100'de dahil) sayılardan 10un katı olanları yazdırır.
        if i%10==0:
            print(i)

artis1()

print("yeni")
def artis2():
    for i in range(10,101,10):#
        print(i)

artis2()#yaptim

# 1'den 500'e kadar (500'de dahil) olan sayılardan 
# 7'nin ve 8'in ortak katı olan sayıları yazdıran fonksiyon

# 1. yol if kontrolü ile 
print("-"*50)
def kat1():
    for i in range(1,501):
        if i%7==0 and i%8==0:# ya da deseydi or diyecektik.
            print(i)

kat1()

print("-"*50)
#2.yol
def kat2():
    for i in range(1,501,56):
        print(i)

# size verilen listedeki elemanları karelerini alıp onları boş bir listeye
# ekleyin. İşiniz bittiğinde listeyi geriye döndürün. Bu fonksiyonu yazın

# fonksiyonu tanımla
# parametreyi yaz
# boş liste oluştur
# for döngüsü ile parametre olarak verilen listenin içerisine gir
# her bir değerin karesini hesapla
# hesapladığın değeri boş listeye append() fonksiyonu ile ekle
# döngü bittiğinde fonksiyonun altına gel ve return bos_liste yaz

def listedondur(rastgele):#fonksiyonun adı listedondur,parametre adı rastgele
    bos_liste = []
    for i in rastgele:#parametre olarak verilen listenin içersine girdik.
        bos_liste.append(i**2)#her bir değerin karesini hesapladık.# hesapladığın değeri boş listeye append() fonksiyonu ile ekle
    return bos_liste

kare_liste = [1,2,3,4,5,6,7,8,9,10]

print("-"*50)
print(f"orijinal liste = {kare_liste}")
print(f"Karesi alınmış liste = {listedondur(kare_liste)}")


# Fonksiyonlarda çoklu parametre kullanımı

# *args  ve **kwargs anahtar kelimeleri ile yapılır
# *args tuple tipindedir ve sadece değer alır
# **kwargs dictionary tipindedir key=value şeklinde değer alır
# istediğimiz kadar çok değer verebiliriz, bir sınır yoktur

# kullanıcının kaç tane sayı ya da parametre gireceğini bilmiyorsak!!!
# *args ya da **kwargs kullanırız

# *args kullanımına örnek

print("-"*50)
def sayiTopla(*args):#*sayi#paramretre olarak *arga yazıyoruz yani
    return sum(args)#sayi da denebilirdi
print(sayiTopla(1,2,3,4,5,6,7,8,9,10,100))#yukarıda *args tanımladığımız için burada istediğimix kadar çok değer girebiliyoruz

# **kwargs kullanımı

def bilgi(**kwargs):
    for key,value in kwargs.items():
        print(f"anahtar = {key}, değer = {value}")

bilgi(uni="MAKÜ",okul="ZTYO",bolum="YBS",sinif=3,sube="A",donem="Bahar",deneme="son")#uni key, makü değeridir.
#istediğimizi girer istediğimizi çıkarırız.

