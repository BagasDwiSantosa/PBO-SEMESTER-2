class Tugas:
    def __init__ (self):
        self.nilalTugas = 0
        
    def inputNilaiTugas(self): 
        self.nilaiTugas = float(input("Masukkan Nilai Tugas\t\t: "))
        setattr(Tugas, 'nilaiTugas', self.nilaiTugas)

class UTSUAS:
    def __init__ (self):
        self.nilaiutsuas = 0

    def inputNilaiUTSUAS(self):
        self.nilaiutsuas = float(input("Masukkan Nilai UTS dan UAS\t: ")) 
        setattr(UTSUAS, 'nilaiutsuas', self.nilaiutsuas)

class Keaktifan:
    def __init__ (self):
        self.nilaikeaktifan = 0

    def inputNilaiAktif(self):
        self.nilaikeaktifan = float(input("Masukkan Nilai Keaktifan\t: ")) 
        setattr(Keaktifan, 'nilaikeaktifan', self.nilaikeaktifan)

class PBO(Tugas, UTSUAS, Keaktifan):
    def __init__(self): 
        self.sksPBO = 0
        self.Rata2PBO = 0
        self.totalPBO = 0

    def rumusPBO(self):
        PBO.inputNilaiTugas(self)
        PBO.inputNilaiUTSUAS(self) 
        PBO.inputNilaiAktif(self) 
        self.sksPBO = int(input("Masukkan Jumlah SKS Matkul\t: ")) 
        setattr(PBO, 'sksPBO', self.sksPBO)

        A_sksPBO = self.sksPBO 
        A_tgs = self.nilaiTugas
        A_uts = self.nilaiutsuas
        A_aktif = self.nilaikeaktifan 
        self.Rata2PBO = ((A_aktif + A_tgs + A_uts)/3)
        self.totalPBO = self.Rata2PBO * A_sksPBO

    def tampilPBO(self): 
        print("Rata-Rata Nilai PB0\t\t:", self.Rata2PBO)
        print("Total Nilai Akhir PB0\t\t:", self.totalPBO)

class UIUX(Tugas, UTSUAS, Keaktifan):
    def __init__ (self): 
        self.sksUIUX = 0
        self.rata2UIUX = 0
        self.totalUIUX = 0

    def rumusUIUX(self):
        UIUX.inputNilaiTugas(self)
        UIUX.inputNilaiAktif(self)
        UIUX.inputNilaiAktif(self)
        self.sksUIUX = int(input("Masukkan Jumlah SKS Matkul\t: "))
        setattr(UIUX, 'sksUIUX', self.sksUIUX)
    
        B_sksUIUX = self.sksUIUX
        B_tgs = self.nilaiTugas
        B_uts = self.nilaiutsuas
        B_aktif = self.nilaikeaktifan
        self.rata2UIUX = ((B_aktif+B_tgs+B_uts)/3)
        self.totalUIUX = self.rata2UIUX *  B_sksUIUX
    
    def tampilUIUX (self):
        print("Rata-Rata Nital UIUX\t\t:", self.rata2UIUX) 
        print("Total Nilai Akhir UIUX\t\t:", self.totalUIUX)

class SIM(Tugas, UTSUAS, Keaktifan):
    def __init__(self):
        self.sksSIM = 0
        self.rata2SIM = 0
        self.totalSIM = 0

    def rumusSIM(self):
        SIM.inputNilaiTugas(self) 
        SIM.inputNilaiUTSUAS(self)
        SIM.inputNilaiAktif(self) 
        self.sksSIM = int(input("Masukkan Jumlah SKS Matkul\t: ")) 
        setattr(SIM, 'sksSIM', self.sksSIM)

        C_sksSIM = self.sksSIM
        C_tgs = self.nilaiTugas
        C_uts = self.nilaiutsuas 
        C_aktif = self.nilaikeaktifan
        self.rata2SIM = ((C_aktif+C_tgs+C_uts)/3)
        self.totalSIM = self.rata2SIM * C_sksSIM

    def tampilSIM(self):
        print("Rata-rata Nilai SIM\t\t:", self.rata2SIM) 
        print("Total Nilai Akhir SIM\t\t:", self.totalSIM)

class IPK(PBO, UIUX, SIM):
    def __init__ (self): 
        self.ipk = 0

    def rumusIPK(self): 
        E_pbo = self.sksPBO
        E_iuiux = self.sksUIUX
        E_sim =  self.sksSIM
        E_total = E_pbo+E_iuiux+E_sim

        D_pbo = self.totalPBO
        D_uiux = self.totalUIUX
        D_sim = self.totalSIM
        self.ipk = (D_pbo+D_sim+D_uiux)/E_total 

        print("Total Semua SKS\t\t\t:",E_total)
        print('Indeks Prestasi Kumulatif\t:', self.ipk)


hasil = IPK()
print("+"+"-"*50+"+")
print("|"+" "*8+" PROGRAM INDEKS PRESTASI KUMULATIF "+" "*7+"|")
print("+"+"-"*50+"+")

while True:
    print()
    print(" "*4+" MATA KULIAH PEMROGRAMAN BERIORIENTASI OBJEK "+" "*3)
    print("+"+"-"*50+"+")
    hasil.rumusPBO()

    print()
    print(" "*10+" MATA KULIAH UI UX DESIGNER "+" "*7)
    print("+"+"-"*50+"+")
    hasil.rumusUIUX()

    print()
    print(" "*5+" MATA KULIAH SISTEM INFORMASI MANAJEMEN "+" "*5)
    print("+"+"-"*50+"+")
    hasil.rumusSIM()  

    print("+"+"-"*50+"+")
    print("|"+" "*11+" INDEKS PRESTASI KUMULATIF "+" "*11+"|")
    print("+"+"-"*50+"+")
    hasil.tampilPBO()
    hasil.tampilUIUX()
    hasil.tampilSIM()
    print("+"+"-"*50+"+")
    hasil.rumusIPK()
    print("+"+"-"*50+"+")

    lanjut = input("Kembali Menginputkan Nilai ? (Y/T) : ")
    if lanjut == "Y" or lanjut == "y":
        print()
        continue
    else:
        print("+"+"-"*50+"+")
        print("|"+" "*19+" TERIMAKASIH"+" "*19+"|")
        print("+"+"-"*50+"+")
        break