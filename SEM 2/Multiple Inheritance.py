print("+"+"-"*50+"+")
print("|"+" "*5+"   PORTAL AKADEMIK MAHASISWA UNJANI YK  "+" "*5+"|")
print("+"+"-"*50+"+")

class pordik:
    def __init__(self):
        self.username = None
        self.__password = None

    def inputLogin(self):
        print("+"+"-"*50+"+")
        self.username = input(" Username\t: ")
        setattr(pordik, 'username', self.username)
        self.password = input(" Password\t: ")
        setattr(pordik, '__password', self.password)

    def tampilLogin(self):
        print("+"+"-"*50+"+")
        print("| SELAMAT DATANG DI PORTAL AKADEMIK, "+self.username+" " *(14-len(self.username))+"|")
        print("+"+"-"*50+"+")

class Profile(pordik):
    def __init__(self):
        self.nama = None
        self.npm = None
        self.prodi = None
    
    def inputProfile(self):
        self.nama = input(" Masukkan Nama\t\t: ")
        setattr(Profile, 'nama', self.nama)
        self.npm = input(" Masukkan npm\t\t: ")
        setattr(Profile, 'npm', self.npm)
        self.prodi = input(" Masukkan prodi\t\t: ")
        setattr(Profile, 'prodi', self.prodi)
    
    def tampilProfile(self):
        print("| Nama\t: "+self.nama+" "*(41-len(self.nama))+"|")
        print("| NPM\t: "+self.npm+" "*(41-len(self.npm))+"|")
        print("| Prodi\t: "+self.prodi+" "*(41-len(self.prodi))+"|")
        print("+"+"-"*50+"+")

class KRS(pordik):
    def __init__(self):
        self.jumlahMatkul = None 
        self.jumlahSKS = None

    def inputKRS(self):
        self.jumlahMatkul = (input("Masukkan jumlah Matkul\t: ")) 
        setattr(KRS, 'jumlahMatkul', self.jumlahMatkul)
        self.jumlahSKS = input("Masukkan Jumlah SKS\t: ")
        setattr(KRS, 'jumlahSKS', self.jumlahSKS)

    def tampilKRS(self):
        print("| Jumlah Mata Kuliah\t: "+self.jumlahMatkul+" "*(25-len(self.jumlahMatkul))+"|")
        print("| Jumlah SKS\t\t: "+self.jumlahSKS+" "*(25-len(self.jumlahSKS))+"|")

class hasilKRS(Profile, KRS): 
    def tampilHasil(self):
        print("+"+"-"*50+"+")
        print("|"+" "*12+" DATA HASIL KRS MAHASISWA "+" "*12+"|")
        print("+"+"-"*50+"+")
        hasilKRS.tampilProfile(self)
        hasilKRS.tampilKRS(self)
        print("+"+"-"*50+"+")


hasil = hasilKRS()
hasil.inputLogin()
hasil.tampilLogin()

print("|"+" "*8+"  Silahkan Inputkan Profil Anda   "+" "*8+"|")
print("+"+"-"*50+"+")
hasil.inputProfile()
print("+"+"-"*50+"+")
print("|"+" "*15+"  PROFIL MAHASISWA  "+" "*15+"|")
print("+"+"-"*50+"+")
hasil.tampilProfile()

print("|"+" "*8+"    Silahkan Inputkan KRS Anda    "+" "*8+"|")
print("+"+"-"*50+"+")
hasil.inputKRS()
print("+"+"-"*50+"+")
print("|"+" "*15+"   KRS MAHASISWA   "+" "*15+"|")
print("+"+"-"*50+"+")
hasil.tampilKRS()
hasil.tampilHasil()

