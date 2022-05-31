class Hero(object):
 """__init__() functions as the class constructor"""
 def __init__(self, nama=None, alias=None, kelompok=None):
    self.nama = nama
    self.alias = alias
    self.kelompok = kelompok

listHero = []
print("Daftar SuperHero:\n")
jumlahData = int(input("Masukkan Jumlah Data :"))

for i in range(jumlahData):
    listHero1 = input("Masukkan Nama\t\t: ")
    listHero2 = input("Masukkan Alias\t\t: ")
    listHero3 = input("Masukkan Kelompok\t: ")

    listHero.append(Hero(listHero1, listHero2, listHero3))
def panggilan():
    print("\nData SuperHero")
    for Hero in listHero:
        print("Nama\t\t: {}\nAlias\t\t: {}\nKelompok\t: {}".format(Hero.nama, Hero.alias, Hero.kelompok))


try:
    panggilan(listHero[10])
except:
    print('Hero bukan bagian dari Avengers!')