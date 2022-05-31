#POLIMORFISME GAESSSSSSSSSSSSSSSSSSSSS
# class Bahasa:
#     def Opening(self):
#         print("Bagas")

# class Indonesia(Bahasa):
#     def Opening(self):
#         print("Hallo")

# class Inggris(Bahasa):
#     def Opening(self):
#         print("Hello")
#         return super().Opening()

# indo = Indonesia()
# ing = Inggris()
# indo.Opening()
# ing.Opening()



#ABSTRAKKKKKKKKKKKKKKKKKKKK
from abc import ABC, abstractmethod

class BahasaDaerah(ABC):
    @abstractmethod
    def Ucapan(self):
        pass

class Jawa(BahasaDaerah):
    def Ucapan(self):
        print("Sugeng Dalu")

class Sunda(BahasaDaerah):
    #Harus ada baru bisa jalan
    # def Ucapan(self):
    #     print("Wilujeng Wengi")
    def Ucap(self):
        print("Kumaha")


Jateng = Jawa()
Jateng.Ucapan()
Jabar = Sunda()
Jabar.Ucap()



#OVERIDINGGGGGGGGGGGGGGGGGGGG
