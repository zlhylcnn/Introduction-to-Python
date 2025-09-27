#python tekli yorum satırı
"""
python da çoklu yorum satırı
"""
#python da veri tipleri:
#4 adet veri tipi vardır.=> int,float(nümerik veriler için)
#str string => karakter verileri için (metinsel ifadeler)
#bool veri (mantıksal sonuçlar için) False ya da true

#int veri tipi
#python'da değişken tanımlama:
#python'da  değişken tanımlanırken veri tipi yazılmaz, ve kodun sonuna herhangi bir işaret(;) konmaz.

deger=30
#deger(type(deger))
print(deger)

#python'da matematiksel işlemler:
#toplama +,çıkarma-,çarpma*,bölme /

#python'da işlem yapmak için önceden değişken tanımlamaya gerek yok.
print("*"*50)#* bundan 50 tane yazarlar.
print(10+5)
print(10*5)
#bölme işleminin  sonucu int olarak istiyorsak 2 yol vardır:
#1. yol:
print(int(10/5))

deger2=30.452
print(deger2)#deger2 yi olduğu gibi yazdırır.
print(type(deger2))

print(deger2.is_integer())#false değerini döndürür.

#pythonda üs alma işlemi ** ile yapılır.
#üssü alınacak sayı**üs derecesi.
print(3**5)#üs alır.
print(3*5)#çarpma.

#str veri tipi
#python'daki en güçlü veri tipidir.
#çünkü diğer veri tiplerini de içerisinde barındırır.
#çünkü her şey string olarak ifade edilebilir.

#str değişken tanımlama 2 şekilde yapılır:
#çift tırnak içerisine " " ya da tek tırnak  " içerisine tanımlanır
# "" içerisine yazılanı kullanın!!!!!!!
deger3="değişken 3"
deger4="değişken 4"

print(deger3)
print(deger4)
print(type(deger3))#claasını söylüyor. 'str' şeklinde
print(type(deger4))

deger5="makü'nün bölümü"
print(deger5)

#python'da str içinde özel karakterler vardır
#örnek / /n/t
#/n yeni satır demektir(alt satıra geçer)
#/t bir tab boşluk bırakır(3-4 boşluk tuşuna basılmış gibi)

deger6="disk c/nAlperen"
print(deger6)

deger7="Alperen/t/t/Burhan"
print(deger7)

print(10)
print("10")#aynı şeyi yazdırır.
print("10.454")
print("false")

#str içinde matematiksel işlemler yapılabilir.
#toplama ve çarpmza işlemi yapılabilir.

#str ile toplama işlemi
print("MAKÜ ZTYO YBS")
a="MAKÜ"
b="ZTYO"
c="YBS"
print(a+b+c)#üstteki string değerleri yan yana yazar.
#str içinde  çarpma işlemi
print(4*6)
print("?"*88)
#str class'ında slicing(dilimleme,parçalama)işlemi

deger8="Burdur Mehmet Akif Ersoy Üniversitesi"
print(len(deger8))#uzunluğunu verir.


#dilimleme işlemi[:] ile yapılır
#[başlangıç ifadesi:bitiş ifadesi]
#başlangıç indexi dahildir,bitiş indexi dahil değildir.9 bitiş derse 8. indexteki en son yazılandır.
#python'da indexleme işlemi 0'dan başlar
#yani ilk karakterin,item'in index değeri 0'dır.
print("-"*59)
print(deger8)
print(deger8[:7])
print(deger8[7:10])
#dilimleme işlemi [:] sadece bir adet iki nokta işareti olursa:
#bunun anlamı [başlangıç değeri:bitiş değeri]
#[::] iki tane iki nokta olursa bunun anlamı:
#[başlangıç:bitiş:artış(step)]

print("*"*50)
print(deger8[::])
print(deger8[::3])
#bu aşamaya kadar olan slicing işlemi soldan sağa yani,
#pozitif değerler ile yapılıyordu.
#negatif değerlerle de slicing işlemi yapılabilir.
#python'da bir koleksiyonun ilk değeri[0] sıfırıncı indextedir.
#son değeri -1 eski birinci indextedir.

print("-"*67)
print(deger8)#hepsini yazdırır normal şekilde
print(deger8[0])#0. indextekini yazar sadece
print(deger8[-1])#değer8'in hepsini tersten yazdırır.- kullandığımız için
print(deger8[::-1])#terstren yazdırma.başı sonu yok. -1 artışı olduğu için hepsini tersten yazdı.
print(deger8[-5:-1])#tersten yazılmış halindekinin başlangıcı5.index ten -1. indexe kadar sola doğru gider.


#bool veri tipi
#iki türü var False(0) ve True(1)
print("-"*98)
print(bool(0))
print(bool(1))
#kontrol yapıları
#if elif else
#python'da yukarıdaki üç ifade ile kontrol yapısı sağlanabilir

sayi1=15
sayi2=30

if sayi1==sayi2:
    print("eşittir.")
else:
    print("eşit değil.")

print("-"*99)
print(sayi1==sayi2)
print(15==23)
print(id(sayi1))
print(id(sayi2))

#== eşittir iişleminin sözel karşılığı is anahtar kelimesidir.
"""!=eşit değildir işleminin sözel karşılığı not kelimesidir.
"""
print(23 is 34)
print(889 is 356)
#ve işlemi and kelimesi ile yapılır
#ya da işlemi or kelimesi ile yapılır
print("90"*99)
print(14 is 10 and 14 is 14)#and işleminde tüm artların true olması lazım
print(14 is 10 and 14 is 14)# or işleminde  sadece 1 şartın ture olması  gerek.işlemin sonucunun true olarak gelmesi için

print("-"*99)
deger9="BURDUR MEHMT AKİF ERSOY ÜNİVERSİTESİ ZTYO"

#[başlangıç değeri:bitiş değeri]0'dan başlar bitiş değerine kadar.
#bitiş değeri dahil değil.
print(deger9)
print(deger9[5:10])


#[başlangıç:bitiş:artış değeri(step sayısı)]
print("-"*99)
print(deger9[::])
print(deger9[::2])

#bu aşamaya kadar olan soldan sağa pozitif sayılarla dilimlemeydi.
#birde sağdan sola negatif sayılarla dilimleme işlemi var.
print("-"*99)
print(deger9[::])
print(deger9[::2])
print(deger9[:-2])


print("*"*99)
print(deger9[::1])
print(deger9[::-1])

#artış miktarında pozitif sayı ile negatif sayının karşılığı yani
#çıktısı aynıdır.sadece sıralamaları birbirine göre terstir

#ters sıralamada slicing işlmi böyle yapılır.
#---------------------------------------------------------------------------------aşağısı2.haftA
#pythonda yerleşik veri yapıları
#python da yerleşik olarak 4 tane veri yapısı vardır.
#list(liste),dictionary(sözlük),tuple(demet) ,set(küme)

#1-liste
#liste tanımlama
my_list=[]#boş bir liste
print(my_list)
print(type(my_list))#listenin veri tipini anlamak için


#list veri yapısına veri ekleme- 1. yol
#list.append() fonk ile veri ekleme
#tek eleman ekler ve sıraı bir şelikde yani 0 indexinden  başlar.
my_list.append("ybs")
my_list.append("2a")
my_list.append(15)
my_list.append(True)
my_list.append(bool(1))

print(my_list)
print("-"*20)


#listelerde verinin(değerin) indexini öğrenme
#list.index() fonksiyonu, içerisinde bir değer alır ve bu değerin listedeki index numarasını döndürür

print(my_list.index("2a"))#2a nın indexini döndürür

#listeye veri ekleme- 2. yol
#list.insert( )fonksiyonu ile veri ekleyebiliriz
#append() fonksiyonundan farkı: veri setinin uzunluğuna göre istediğimiz
#index değerine ekleme yapabiliriz

print("-"*990)
print(f"listenin uzunluğu={len(my_list)}")#f formattan gelir.özellik.
print(f"orjinal liste={(my_list)}")

my_list.insert(3,"yeni değer")#3. indexe yeni değer isimli değer eklendi
print(f"insert işleminden sonra liste={my_list}")

#listede aynı indexteki eleemanı güncelleme(veri ekleme değil.mantık olarak benzwer ama farklı işlemlerdir)
my_list[3]="son değer"
print(my_list)

#listeden eleman silme -1. yol(tekli elemanı silme- son elemanı silme)
print("-"*99)
print(my_list)


my_list.pop()#listenin aonundaki -1 insexli elemanı siler
print(my_list)

#istediğimiz değeri silen fonksiyonu list.remove()
print("*"*50)
print(my_list)
my_list.remove(86.65)
print(my_list)

#lisrt.clear() listenin içerisindeki tüm elemanları siler
#liste yine durur ama içi boştur
#print("*"*50)
#print(my_list)
#my_list.clear()
#print(my_list)

#del fonksiyonu ile silme işlemi
#delete kelimesinin kısaltmasıdır ve listenin direkt kendisini diler

#del my_list
#print(my_list)
print(my_list)
del my_list[:2]#istediğimiz aralığı verirriiz o aralığı siler.faydalı kullan
print(my_list)

#for döngüsü
#pythondaki for döngüsü c#taki for ve foreach döngülerinin her ikisinin yerine kullanılır.

#for döngüsü kullanımı -1(sayılar ile kullan)
#for i in range(başlangıç,btitiş,artış)
#for i in range(başlangıç,bitiş)
#for i in range(bitiş)=>0'dan başlar ve bitiş -1'e kadar yazdırır.
#örnek: for i in range(10)=>0,1,2,3,4,5,6,7,8,9(10 u yazdırırmaz)
for i in range(1,11,2):#başlangıç değeri,bitiş değeri,artış değeri
      print(i)#i 1le 11iç inindeyken yazdırır . i=i+1


print("-"*55)
#for döngüsü veri yapıları ile kullanımı -1
print(len(my_list))
print(my_list)


for i in range(len(my_list)):
     print(f"{i}.index numarasına sahip veri={my_list[0]}")

print("son değer" in my_list)#içinde var mı yok mu diye kontrol eder.

#for döngüsünün veri yapıları ile kullanımı -2

print ("-"*20)
for i in my_list:
     print(i)

#2. veri yapısı dictionary (sözlük)
#"key":"value" mantığına göre çalışır
#key => benzersizdir. aynı isme sahip yalnızca 1 key bulunabilir.
#value=> hepsi aynı olsa da sorun değil
#value tek bir değerde olabilir. bir liste de olabilir .fark etmez.
     


    
#dictioary veri yapısı tanımlama

my_dict={"isim":"zel","soyisim":"yalçın"}
print(type)
print(type(my_dict))
print(my_dict)

#keyler ile çalışma
#key çağırma -1.yol
print(my_dict["bolum"])
#print(my-dict["bolum"]) böyle bir key olmadığı için hata  verir


#bu hatayı almamak için get fonksiyonu ile key değerini çağırırız.

print("-"*20)
print(my_dict.get["bolum"])
print(my_dict.get["bolumm"])

#var olan tüm key değerlerini görmek için keys() fonksiyonunu kullanırız.
print("*"*20)
print(my_dict.keys())
#değerleri (values ile çağırma)
print ("*"*13)
print(my_dict.values())

#hem key hem de values değerleri aynı anda görmek için -2. yol
print("*"*8)
print(my_dict.items)#for döngüsü ile kullanılır(genellikle)



#dict veri yapısına veri ekleme -1. yol
#artama operatörü(=) ile değer ekleme

print(my_dict.keys())

my_dict["okul"]="bucak ztyo"
print(my_dict)


my_dict["okul"]="bucak ztyo/burdur makü"
print(my_dict)

#dictioary veri ekleme- 2. yol
#update() fonksiyonu ile önceki değerler ezilir(owewrite) edilir
my_dict.update(("isim":"zel","s":"yalçın","bolum":"ybs","okul:":"ztyo"))

print(my_dict)

#dict veri yapısından veri silme
#veri silme-1. yol

my_dict.clear
print(my_dict)

#del my_dict
#print(my_dict)


#key silmek için 
print(my_dict.keys())
del my_dict["bolum"]
print(my_dict.keys())


#değer silmekl için
#atama operatörü (=) kullanılabilir 

print("-"*36)
print(my_dict.values())
my_dict["isim"]=""
print(my_dict.values())
#---------------------------------------------------------------------------------------------------------3.hafta aşağısıııı
#3. veri yapısı tuple(demet)
#tuple'in tanımlanması=>normal parantez ile tanımlanır

my_tuple=()
print(my_tuple)

#ilk tanımlamada değer atanır

my_tuple(15,86.95,True,"Bucak")
print(my_tuple)

print(f"my_tuple değişkeninin uzunluğu="{len(my_tuple)})

print(f"type(my_tuple) = {type (my_tuple)}")
print(f"my_tuple değişkeninin 2. inddeksindeki değer={my_tuple[2]}")
print(f"my_tuple değişkeninin 2. inddeksindeki değerin tipi ={type(my_tuple[2]})")


print(f"my_tuple[2] değerinden {my_tuple.count(my_tuple[2])} adet var") #veri
print(f"my_tuple içerisindeki Bucak değeri {my_tuple.index('Bucak')} . insekste")

#tuple sonradan eleman eklememize, değiştirmemize yani (güncellememize) izin vermez.
#eleman eklemek için tuple ı listeye çevirip eleman ekleyebiliriz.maliyetli olur ama python izin verir.

print(f"my_tuple[2]={my_tuple[2]}")
my_tuple[2]="yeni değer"

print(my_tuple)

my_list=list(my_tuple)
my_list[2]="yeni değer"#2. indexteki değeri güncelledik.
my_list.append("son değer")#son indexe son değer diye bir şey ekledik.#direkt sona ekledi. append hep son değeri en sona ekler.

my_new_tuple=tuple(my_list)#ekleme işleminden sonra tekrar tuple'a çevirdik.
print(f"my_tuple'ın yeni hali={my_new_tuple} ")

""""
#listeyi çoklu eleman ekleme
my_list=["burdur","mehmet","aktif"]
my_list2=["ersoy","üniversitesi"]

my_list.extend(my_list)
print(my_list)
"""

#4.veri yapısı=>set(küme)
#matematikteki küme mantığı ile birebir aynıdır.
#tanımlama=>süslü parantez içerisine değer alarak tanımlanır.
#aynı değerden birden fazla yazılsa bile print ile ekrana basıldığında ya da işlem yapıldığında tek bir tane değermiş gibi davranılır.

#set veri yapısında sıralama (index değerleri) 
my_set1={15,50,50,15,20,"Bucak","Bucak,Makü",True}
my_set2={50,"Bucak","Bucak,Makü",False}

print(f"my_set1={my_set1}")
print(f"my_set2={my_set2}")

#print("my_set2[2] ={my_set2[2]}")#hata verecek çüğnkü her seferinde indexi değişiyor.
my_list=[15,15,"Furkan","ahmet","furkan",14,23,14]
print(f"my_list={my_list}")


my_new_set=set(my_list)
my_new_list=list(my_new_set)

print(f"my_list'in yeni hali= {my_new_list}")


print(list(set(my_list)))

#kümelerde matematiksel işlemler
#kümelerde birleşim işlemi

print(f"my_set1 birleşim my_set2={my_set1.union(my_set2)}")

#kümelerde kesişim işlemi

print(f"my_set1 birleşim my_set2={my_set1.intersection(my_set2)}")

#kümelerde fark işlemi

print(f"my_set1 fark  my_set2={my_set1.difference(my_set2)}")
#########
print(f"my_set2 fark my_set1={my_set2.difference(my_set1)}")



