

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
    
    @abstractmethod
    def bilgi(self):
        pass
    
    @abstractmethod
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
