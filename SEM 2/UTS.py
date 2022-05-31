
# class Lingkaran:
#     def __init__(self):
#         self.phi = 3.14
#         self.jari2 = None
#         self.__diameter = None

#     def inputJari2(self):
#         self.jari2 = float(input("Masukkan Jari-jari Lingkaran : "))
#         setattr(Lingkaran, 'jari2', self.jari2)
    
#     def inputDiameter(self):
#         self.__diameter = float(input("Masukkan Diameter Lingkaran : "))
#         setattr(Lingkaran, '__diameter', self.__diameter)

#     def hitungLuas(self):
#         self.hitung = self.phi * (self.jari2**2)
#         print("Phi \t\t\t:", self.phi)
#         print("Jari-jari\t\t:",  getattr(Lingkaran, 'jari2'))
#         print("Hasil Luas Lingkaran\t:", self.hitung)
    
#     def hitungKeliling(self):
#         self.hitungKel = float(self.phi * self.__diameter)
#         print("Phi \t\t\t:", self.phi)
#         print("Diameter\t\t:",  getattr(Lingkaran, '__diameter'))
#         print("Hasil Keliling Lingkaran\t:", self.hitungKel)        

# print("+"+"-"*50+"+")
# print("|"+" "*10+" PROGRAM MENGHITUNG LINGKARAN "+" "*10+"|")
# print("+"+"-"*50+"+")

# lin = Lingkaran()
# print("\nSilahkan Pilih Opsi yang tersedia ")
# print("1. Luas Lingkaran")
# print("2. Keliling Lingkaran")
# print("3. Keluar")
# pilih = int(input("Masukkan Pilihan anda : "))

# if pilih == 1:
#     print("\nMASUKKAN INPUTAN")
#     lin.inputJari2()
#     print("\nHASIL LUAS LINGKARAN")
#     lin.hitungLuas()

# elif pilih == 2:
#     print("\nMASUKKAN INPUTAN")
#     lin.inputDiameter()
#     print("\nHASIL KELILING LINGKARAN")
#     lin.hitungKeliling()  

# else:
#     print("TERIMAKASIH MASZEH")





#SOAL 2

class PemilikSaham():
    def __init__(self):
        self.id_PemilikSaham = None
        self.Nama_PemilikSaham = None
        self.jumlahInvestasi = None

    def input_dataPemilikSaham(self):
        print("  MASUKKAN DATA PEMILIK SAHAM DIBAWAH INI !!!")
        print("+"+"-"*50+"+")
        self.id_PemilikSaham = input("Masukkan ID Pemilik Saham\t: ")
        self.Nama_PemilikSaham = input("Masukkan Nama Pemilik Saham\t: ")
        self.jumlahInvestasi = input("Masykkan Jumlah Investasi\t: ")

    def tampil_DataPemilikSaham(self):
        print("ID Pemilik Saham\t:", self.id_PemilikSaham)
        print("Nama Pemilik Saham\t:", self.Nama_PemilikSaham)
        print("Jumlah Investasi\t:", self.jumlahInvestasi)

class PemainSepakBola:
    def __init__(self):
        self.id_Pemain = None
        self.nama_Pemain = None
        self.Posisi = None

    def inputDataPemain(self):
        print("+"+"-"*50+"+")
        print("  MASUKKAN DATA PEMAIN SEPAK BOLA DIBAWAH INI !!!")
        print("+"+"-"*50+"+")
        self.id_Pemain = input("Masukkan ID Pemain\t\t: ")
        self.nama_Pemain = input("Masukkan Nama Pemain\t\t: ")
        self.Posisi = input("Masukkan Posisi\t\t\t: ")
    
    def tampilDataPemain(self):
        print("ID Pemain\t\t:",self.id_Pemain)
        print("Nama Pemain\t\t:", self.nama_Pemain)
        print("Posisi Pemain\t\t:", self.Posisi)


class ClubSepakBola(PemilikSaham, PemainSepakBola):
    def __init__(self):
        self.id_club = None
        self.namaClub = None
        self.namaPelatih = None

    def inputDataClub(self):
        ClubSepakBola.input_dataPemilikSaham(self)
        ClubSepakBola.inputDataPemain(self)
        print("+"+"-"*50+"+")
        print("  MASUKAN DATA CLUB SEPAK BOLA DIBAWAH INI !!!")
        print("+"+"-"*50+"+")
        self.id_club = input("Masukkan ID Club\t\t: ")
        self.namaClub = input("Masukkan Nama Club\t\t: ")
        self.namaPelatih =  input("Masukkan Pelatih Club\t\t: ")

    def tampilDataClub(self):
        print("\n+"+"-"*50+"+")
        print("|"+" "*17+" INFORMASI CLUB"+" "*18+"|")
        print("+"+"-"*50+"+")
        ClubSepakBola.tampil_DataPemilikSaham(self)
        ClubSepakBola.tampilDataPemain(self)
        print("ID Club\t\t:", self.id_club)
        print("Nama Club\t\t:", self.namaClub)
        print("Nama Pelatih\t\t:", self.namaPelatih)


print("+"+"-"*50+"+")
print("|"+" "*10+"   PROGRAM KLUB SEPAK BOLA    "+" "*10+"|")
print("+"+"-"*50+"+")
club = ClubSepakBola()
club.inputDataClub()
club.tampilDataClub()