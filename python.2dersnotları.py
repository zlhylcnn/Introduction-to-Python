
# Python'da yerleşik veri yapıları (built-in data structures)

# Python'da yerleşik olarak 4 veri yapısı vardır. Bunlar:
# List (liste), Dictionary(sözlük), tuple (demet), set(küme)

# En çok kullanılan list ve dictionary
# 1) Liste
# Liste tanımlama

my_list = []#.append,.index,.insert(3,ghjfh),.pop,.remove()-istediğimiz değeri siler
print(my_list)#.clear-liste durur ama içindeki tüm elemaları siler,del-direkt listeyi siler
print(type(my_list))

# List veri yapısına veri ekleme - 1. Yol
# list.append() fonksiyonu veri ekleme
# tek eleman ekler ve sıralı bir şekilde yani 0 indeksinden başlayarak ekler
my_list.append("Ybs")
my_list.append("2a")
my_list.append(15)
my_list.append(86.65)
my_list.append(True)
my_list.append(bool(1))

print(my_list)
print("-"*50)
# Listelerde verinin (değerin) indexini öğrenme
# list.index() fonksiyonu, içerisine bir değer alır ve bu değerin
# listedeki index numarasını döndürür

print(my_list.index("2a"))#2a nın indexini  verir.

# Listeye veri ekleme - 2. yol
# list.insert() fonksiyonu ile veri ekleyebiliriz.
# append() fonksiyonundan farkı: veri setinin uzunluğuna göre istediğimiz
# index değerine ekleme yapabiliriz

print("-"*50)
print(f"listenin uzunluğu = {len(my_list)}")
print(f"orijinal liste = {my_list}")#listeyi çağırırken [] açmamıza gerek yok

my_list.insert(3,"yeni değer") # 3. indexe yeni değer isimli değeri ekledi
print(f"insert işleminden sonra liste = {my_list}")

# Listede aynı indeksteki elemanı güncelleme (veri ekleme değil)
my_list[3] = "son değer"
print(my_list)

# Listeden eleman silme - 1. yol (tekli eleman silme-son elemanı silme)

print("-"*50)
print(my_list)

my_list.pop() # listenin sonundaki -1 indeksli elemanı siler
print(my_list)

# İstediğimiz değeri silen fonksiyonu list.remove()
print("-"*50)
print(my_list)
my_list.remove(86.65)
print(my_list)

#list.clear() listenin içerisindeki tüm elemanları siler
# liste yine durur ama içi boştur

print("-"*50)
print(my_list)
my_list.clear()
print(my_list)

# del fonksiyonu ile silme işlemi
# delete kelimesinin kısaltmasıdır ve listenin direkt kendisini siler

#del my_list
#print(my_list)

print("-"*50)
# del fonksiyonu ile sıralı şekilde çoklu eleman silme

print(my_list)
print(my_list[:2])
del my_list[:2]
print(my_list)


# for döngüsü

#Python'daki for döngüsü c#'taki for ve foreach döngülerinin her ikisinin
# yerine kullanılabilir

# for döngüsü kullanımı - 1 (sayılar ile kullanımı)
# for i in range(başlangıç,bitiş,artış)
# for i in range(başlangıç,bitiş)
# for i in range(bitiş) => 0'dan başlar ve bitiş-1'e kadar yazdırır
# Örnek: for i in range(10) => 0,1,2,3,4,5,6,7,8,9  (10'u yazdırmaz,dahil değildir.)
for i in range(11):
    print(i)

print("*"*50)

# for döngüsü veri yapıları ile kullanımı - 1

print(len(my_list))#kaç karakter var onu verir.uzunluğunu yani
print(my_list)

print("-"*50)

for i in range(len(my_list)):
    print(f"{i}. index numarasına sahip veri = {my_list[i]}")

# for döngüsünün veri yapıları ile kullanımı - 2

print("-"*50)
for i in my_list:#parametresi liste yani üzerinde işlem yapacağı şey.
                 #listenin her elemanını i ye tek tek atadı gibi bir şey
    print(i)#listenin elemanlarını döndürür print gibi

# 2 ) Dictionary (Sözlük)
# "key":"value" mantığına göre çalışır.
# key => benzersizdir. Aynı isme sahip yalnızca 1 key bulunabilir
# value => hepsi aynı olsa da sorun değil.
# value tek bir değer de olabilir. Bir liste de olabilir fark etmez.

# Dictionary veri yapısı tanımlama
print("-"*50)
my_dict = {"isim":"Furkan","soyisim":"ATLAN","bolum":"YBS"}
print(type(my_dict))
print(my_dict)

print("-"*50)
# key'ler ile çalışma
# key çağırma - 1.yol
print(my_dict["bolum"])
#print(my_dict["bolumm"]) # böyle bir key olmadığı için hata verir

# Bu hatayı almamak için get() fonksiyonu ile key değerini çağırırız

print("-"*50)
print("dict veri yapısında get fonksiyonu kullanımı")
print(my_dict.get("bolum"))
print(my_dict.get("bolumm"))

# var olan tüm key değerlerini görmek için keys() fonksiyonunu kullanırız
print("-"*50)
print(my_dict.keys())
# Değerleri (values) çağırma
print("-"*50)
print(my_dict.values())

# hem key hem de values değerleri aynı anda görmek için - 1.yol
print("-"*50)
print(my_dict)

# hem key hem de values değerleri aynı anda görmek için - 2.yol
print("-"*50)
print(my_dict.items()) # for döngüsüyle kullanılır (genellikle)

# Dict veri yapısına veri ekleme - 1. yol
# atama operatörü (=) ile değer ekleme

print("-"*50)
print(my_dict.keys())

my_dict["okul"] = "Bucak ZTYO"
print(my_dict)

my_dict["okul"] = "Burdur Makü/Bucak ZTYO"
print(my_dict)

# Dictionary veri ekleme - 2. yol
# update() fonksiyonu ile önceki değerler ezilir (overwrite) edilir
print("-"*50)
my_dict.update({"isim":"Yusuf","soyisim":"Arslan","bolum":"muhasebe",  "okul":"Zeliha Tolunay"})
print(my_dict)

# Dict veri yapısından veri silme
# Veri silme - 1. yol
print("-"*50)
my_dict.clear()
print(my_dict)

del my_dict
print(my_dict)


# key silmek için
print("-"*50)
print(my_dict.keys())

del my_dict["bolum"]
print(my_dict.keys())

# değer silmek için
# atama operatörü (=) kullanılabilir
print("-"*50)
print(my_dict.values())


my_dict["isim"] = ""
print(my_dict.values())





