# #PROGRAM SATU

# class Buku:
#     def __init__(self):
#         self.Penulis = None
#         self.Penerbit = None
#         self.Tahunterbit = None

#     def inputBuku(self):
#         self.Penulis= input("Masukkan Penulis\t: ")
#         setattr(Buku, 'Penulis', self.Penulis) 
#         self.Penerbit= input("Masukkan Penerbit\t: ")
#         setattr(Buku, 'Penerbit', self.Penerbit)
#         self.Tahunterbit= input("Masukkan Tahun terbit\t: ")
#         setattr(Buku, 'Tahunterbit', self.Tahunterbit)

#     def jenis(self):
#         print('Pilihan Jenis Buku dibawah\n 1. Fiksi\n 2. Non Fiksi')

#     def tampilBuku(self):
#         print("Penulis\t\t\t:", getattr(Buku, 'Penulis')) 
#         print("Penerbit\t\t:", getattr(Buku, 'Penerbit'))
#         print("Tahun Terbit\t\t:", getattr(Buku, 'Tahunterbit'))

# class Novel (Buku):
#     def jenis(self):
#         self.jenis =None 
#         self.jenis =input("Masukkan Jenis Novel\t: ")
#         setattr(Novel, 'jenis', self.jenis)

#     def tampilNovel(self):
#         print("Jenis Novel\t\t:", getattr(Novel, 'jenis'))

# class pelajaran(Buku): 
#     def jenis(self):
#         self.jenis= None
#         self.jenis =input("Masukkan Jenis Pelajaran: ") 
#         setattr(pelajaran, 'jenis', self.jenis)

#     def tampilPelajaran(self): 
#         print("Jenis Pelajaran\t\t:",getattr(pelajaran, 'jenis'))


# print("= "*18+"=")
# print("| ======= PROGRAM DATA BUKU ========= |")
# print("= "*18+"=")
    
# while True :

#     book=Buku() 
#     book.jenis()

#     pilih=int(input("Masukkan Pilihan\t: "))

#     if pilih == 1:
#         nvl=Novel()
#         print("\n       INPUT DATA NOVEL        ")
#         print("= "*18+"=") 
#         nvl.inputBuku()
#         nvl.jenis()
#         print("\n           DATA NOVEL          ")
#         print("= "*18+"=") 
#         print("Jenis Buku\t\t: Fiksi")
#         nvl.tampilNovel()
#         nvl.tampilBuku()
#         print("= "*18+"=") 

#     elif pilih==2:
#         pljrn = pelajaran()
#         print("\n       INPUT DATA PELAJARAN        ")
#         print("= "*18+"=")     
#         pljrn.inputBuku()
#         pljrn.jenis()
#         print("\n        DATA PELAJARAN        ")
#         print("= "*18+"=")     
#         print("Jenis Buku\t\t: Non Fiksi")
#         pljrn.tampilPelajaran()
#         pljrn.tampilBuku()  
#         print("= "*18+"=")             
    
#     else:
#         print("OOPS TERJADI KESALAHAN :(")
    
#     lanjut = input("Kembali ke Menu awal ? (Y/T) : ")
#     print("= "*18+"=")  
#     if lanjut == 'Y':
#         print()
#         continue
#     elif lanjut == 'T':
#         print()
#         break
#     else:
#         print("OOPS TERJADI KESALAHAN :(")
#         break





#PROGRAM DUAA
class BangunDatar:
    def __init__(self):
        self.Keliling = "   1. Keliling"
        self.Luas = "   2. Luas"

    def hitungLuas(self): 
        print(self.Luas)

    def hitungKeliling(self): 
        print(self.Keliling)

class Lingkaran(BangunDatar):
    def init__(self): 
        self.phi= 3.14 
        self.jari =None

    def inputJari(self):
        self.jari=float(input("Masukkan Jari-Jari\t: ")) 
        setattr(Lingkaran, 'jari', self.jari)

    def hitungLuas(self): 
        print("Phi\t\t\t: "+str(self.phi))
        print("Jari-jari\t\t: "+str(getattr(Lingkaran, 'jari')))
        print("\nLuas Lingkaran\t\t:", str(self.phi*(self.jari**2)))

    def hitungKeliling(self): 
        print("Phi\t\t\t: "+str(self.phi))
        print("Jari-jari\t\t: "+str(getattr(Lingkaran, 'jari')))
        print("Diameter\t\t: "+str(self.jari*2))
        print("\nkeliling Lingkaran\t:",str(2* self.phi*self.jari))

class Segitiga(BangunDatar):
    def __init__(self):
        self.tinggi =None 
        self.alas= None
        self.sisil =None
        self.sisi2= None
        self.sisi3 =None

    def inputTinggiAlas(self):
        self.tinggi=float(input("Masukkan tinggi\t\t: ")) 
        setattr(Segitiga, 'tinggi', self.tinggi) 
        self.alas=float(input("Masukkan alas\t\t: "))
        setattr(Segitiga, 'alas', self.alas)

    def inputSisi(self):
        self.sisi1=float(input("Masukkan Sisi 1\t\t: "))
        setattr(Segitiga, 'sisi1', self.sisi1)
        self.sisi2=float(input("Masukkan Sisi 2\t\t: "))
        setattr(Segitiga, 'sisi2', self.sisi2)
        self.sisi3=float(input("Masukkan Sisi 3\t\t: "))
        setattr(Segitiga, 'sisi3', self.sisi3)

    def hitungLuas(self):
        print("Tinggi Segitiga\t\t:",str(getattr(Segitiga, 'tinggi')))
        print("Alas Segitiga\t\t:",str(getattr(Segitiga, 'alas')))
        print("\nLuas Segitiga\t\t:",str(1/2*self.alas * self.tinggi))

    def hitungKeliling(self):
        print("Sisi 1\t\t\t:", str(self.sisi1))
        print("Sisi 2\t\t\t:", str(self.sisi2))
        print("Sisi 3\t\t\t:", str(self.sisi3))
        print("\nKeliling Segitiga\t:", str(self.sisi1 + self.sisi2 + self.sisi3))

print("= "*23+"=") 
print("|======= PROGRAM MENGHITUNG BANGUN DATAR ======|")
print("= "*23+"=") 

bangun =BangunDatar()

bundar =Lingkaran() 
stg= Segitiga()

while True:
    print("Pilihan Menghitung Bangun Datar Dibawah ") 
    bangun.hitungKeliling() 
    bangun.hitungLuas()
    pilih= int(input("\nMasukkan Pilihan\t: "))
    if pilih ==1:
        print("= "*23+"=") 
        print("Pilihan Bangun Datar Dibawah\n 1. Lingkaran\n 2. Segitiga") 
        pilihBangun =int(input("\nMasukkan Pilihan\t: "))

        if pilihBangun == 1: 
            print("= "*23+"=") 
            bundar.inputJari()
            print("= "*23+"=") 
            print("|"+" "*20+"HASIL"+" "*20+"|")
            print("= "*23+"=") 
            bundar.hitungkeliling()
            print("= "*23+"=") 

        elif pilihBangun == 2:
            print("= "*23+"=") 
            stg.inputSisi()
            print("= "*23+"=") 
            print("|"+" "*20+"HASIL"+" "*20+"|")
            print("= "*23+"=") 
            stg.hitungKeliling()
            print("= "*23+"=") 

        else:
            print("00PS TERJADI KESALAHAN :(")
            break

    elif pilih== 2 :
        print("Pilihan Bangun Datar Dibawah\n 1. Lingkaran\n 2. Segitiga") 
        pilihBangun =int(input("\nMasukkan Pilihan\t: "))
        if pilihBangun == 1: 
            print("= "*23+"=") 
            bundar.inputJari()
            print("= "*23+"=") 
            print("|"+" "*20+"HASIL"+" "*20+"|")
            print("= "*23+"=") 
            bundar.hitungLuas()
            print("= "*23+"=") 

        elif pilihBangun == 2:
            print("= "*23+"=") 
            stg.inputTinggiAlas()
            print("= "*23+"=") 
            print("|"+" "*20+"HASIL"+" "*20+"|")
            print("= "*23+"=") 
            stg.hitungLuas()
            print("= "*23+"=") 

        else:
            print("00PS TERJADI KESALAHAN :(")
            break
  
    else:
        print("00PS TERJADI KESALAHAN :(")
        break

    lanjut = input("Kembali ke Menu awal ? (Y/T) : ")
    print("= "*18+"=")  
    if lanjut == 'Y':
        print()
        continue
    elif lanjut == 'T':
        print()
        break
    else:
        print("OOPS TERJADI KESALAHAN :(")
        break