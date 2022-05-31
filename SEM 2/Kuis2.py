class Mahasiswa:
    def __init__(self, nama = None, nilai = None):
        self.nama = nama
        self.nilai = nilai

listMahasiswa = []

jumlahInput = 5
        
for i in range (jumlahInput):
    
    Mahasiswa1 = input("Masukkan Nama Mahasiswa : ")
    Mahasiswa2 = str(input("Masukkan Nilai Mahasiswa : "))
    print()
    
    listMahasiswa.append(Mahasiswa(Mahasiswa1, Mahasiswa2))
def panggil():
    print("DATA MAHASISWA")
    for Mahasiswa in listMahasiswa:
        print("Nama :{}\nNilai :{}".format(Mahasiswa.nama, Mahasiswa.nilai))

try:
    panggil(listMahasiswa[20])
except:
    print('Data tidak Tersedia')



class Komputer:
  def Prosesor(self):
    print('Prosesor Intel core i3')

class Laptop(Komputer):
  def Prosesor(self):
    super().Prosesor()
    print("dengan generasi ke 10")


Pc = Komputer()
gaming = Laptop()

Pc.Prosesor()
print()
gaming.Prosesor()




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