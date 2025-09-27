
# 3. veri yapısı Tuple (Demet)
# Tuple'nin tanımlanması => normal parantez ile tanımlanır ()

my_tuple = ()
print(my_tuple)

# ilk tanımlamada değer atanır

my_tuple = (15,86.95,True,"Bucak")
print(my_tuple)
print(f"my_tuple değişkeninin uzunluğu = {len(my_tuple)}")

print("-"*50)
print(f"type(my_tuple) = {type(my_tuple)}")
print(f"my_tuple değişkeninin 2. indeksindeki değer = {my_tuple[2]}")
print(f"my_tuple değişkeninin 2. indeksindeki değerin tipi = {type(my_tuple[2])}")

print(f"my_tuple[2] değerinden {my_tuple.count(my_tuple[2])} adet var") # verilen değerden kaç tane olduğunu yazar
print(f"my_tuple içerisindeki Bucak değeri {my_tuple.index('Bucak')}. indekste yer alır")

# Tuple, sonradan eleman eklememize, değiştirmemize (güncellememize) izin vermez!!!

print(f"my_tuple[2] = {my_tuple[2]}")
my_tuple[2] = "yeni değer"
print(my_tuple)

my_list = list(my_tuple)
my_list[2] = "yeni değer" # 2.indeksteki değeri güncelledik (True gitti)
my_list.append("son değer") # son indekse son değer diye bir değer ekledik

my_new_tuple = tuple(my_list) # ekleme işleminden sonra tekrar tuple'ye çevirdik
print(f"my_tuple'nin yeni hali = {my_new_tuple}")
print("-"*50)

# 4. veri yapısı => Set (Küme)
# Matematikteki küme mantığı ile bire bir aynıdır
# Tanımlama => süslü parantez içerisine değer alarak tanımlanır

# set veri yapısında aynı değerden birden fazla yazılsa bile
# print ile ekrana basıldığında ya da işlem yapıldığında
# tek bir tane değermiş gibi davranılır

# set veri yapısında sıralama (indeks değerleri) her defasında farklı yazılır
# print ile ekrana her bastığımızda, değerlerin sırası değişir
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
my_set1  = {15,50,50,15,20,"Bucak","Bucak","Makü",True}
my_set2 = {50,"Bucak","Makü","Makü",False}

print(f"my_set1 = {my_set1}")
print(f"my_set2 = {my_set2}")

my_list = [15,15,"Furkan","Ahmet","Furkan",True,True,98.86,15]
print(f"my_list = {my_list}")

my_new_set = set(my_list)#my listi sete çevirdim çünkğü tekrarlanan değerleri bi kere gösterecek
my_new_list = list(my_new_set)#sete çevirdiğim my listi tekrar listeye çevirdim çünkü her seferinde sırası değişiyor

print(f"my_list'in yeni hali = {my_new_list}")

# Listedeki aynı değerleri silmek ve sonra da tekrar listeye dönüştürmek
print(list(set(my_list)))#yukarıdakilerin kısaltılmış hali
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Kümelerde matematiksel işlemler

print("-"*50)
print(f"my_set1 = {my_set1}")
print(f"my_set2 = {my_set2}")

# Kümelerde birleşim işlemi
print(f"my_set1 birleşim my_set2 = {my_set1.union(my_set2)}")

# Kümelerde kesişim işlemi
print(f"my_set1 kesişim my_set2 = {my_set1.intersection(my_set2)}")


# Kümelerde Fark işlemi
# my_set1'de olup da my_set2'de olmayan elemanlar
print(f"my_set1 fark my_set2 = {my_set1.difference(my_set2)}")

# Kümelerde Fark işlemi
# my_set2'de olup da my_set1'de olmayan elemanlar
print(f"my_set2 fark my_set1 = {my_set2.difference(my_set1)}")


# Python'da for döngüsü kullanımı
# for döngüsü, c#'taki for ve foreach döngülerinin yerine kullanılabilir.

# for döngüsü - 1 (nümerik veriler için - sayılar için)

# for döngüsü aşağıdaki gibi tanımlanabilir
# for anahtar_kelime in range(bitiş değeri)
print("-"*50)
for i in range(10):#varsayılan olarak 0dan başlar,9a kadar yazar
    print(i)
    # i = i+1
    # i += 1

# for döngüsü - 2 (nümerik veriler için - sayılar için)

# for anahtar_kelime in range(başlangıç değeri, bitiş değeri)

print("-"*50)
for i in range(1,11):#1dan baslar 1 a kadar yazar.başlangıçı 1 olarak kabul etti.
    print(i)

# for döngüsü - 3 (nümerik veriler için - sayılar için)

# for anahtar_kelime in range(başlangıç değeri, bitiş değeri, artış değeri)

print("-"*50)

# 0'dan 11'e kadar (11 dahil değil) olan çift sayıların yazımı
for i in range(0,11,2):#0den 10 a kadar çift sayıları yazdırır. v
    print(i)

# 1'den 11'e kadar olan sayıların karesi
print("-"*50)
for i in range(1,11):
    print(i**2)

# for döngüsü veri yapıları ile kullanımı

# 1) Liste ile Kullanımı
# for anahtar_kelime in veri_yapısı
print("-"*50)
my_list = ["Adana","Adıyaman","Afyon","Ankara","İstanbul","Burdur","İzmir"]

for i in my_list:
    print(i)


# my_list içerisindeki illerden 'A' harfi ile başlayanları yazdırma
print("-"*50)
print("A harfi ile başlayan iller:")

# 1. yol hazır fonksiyon ile 
for i in my_list:
    if i.startswith("A"):
        print(i)

# 2. yol (indeks ile müdahale ederek)
print("-"*50)
print("2. Yol")
for i in my_list:
    if i[0] == "A":
        print(i)

# Baş harfi 'İ' olmayan illeri yazdırma

# 1. Yol => hazır fonksiyon ile
print("-"*50)
print("1. Yol")
for i in my_list:
    if not i.startswith('İ'):
        print(i)

# 2. yol => hazır fonksiyon ile
print("-"*50)
print("2. Yol")
for i in my_list:
    if i.startswith('İ') == False:
        print(i)

# 3. yol => indekse göre
print("-"*50)
print("3. Yol")
for i in my_list:
    if i[0] != 'İ':
        print(i)#ben yaptim

# 4. yol => indekse göre
print("-"*50)
print("4. Yol")
for i in my_list:
    if not i[0] == 'İ':
        print(i)

# 5. yol => değere göre
print("-"*50)
print("5. Yol")
for i in my_list:
    if i != "İzmir" and i != 'İstanbul':
        print(i)