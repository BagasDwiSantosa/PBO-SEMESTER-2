import cProfile


class pegawai:
    def __init__(self):
        self.NIP = None
        self.nama = None
        self.gajiPokok = None 
        self.tunjanganJabatan = None
        self.pajak = None
        self.gajiBersihPegawai = None

    def ubahJabatan(self):
        self.NIP = input("Masukkan NIP\t\t\t: ") 
        setattr(pegawai, 'NIP', self.NIP)

        self.nama = input("Masukkan Nama\t\t\t: ")
        setattr(pegawai, 'nama', self.nama)

        self.gajiPokok = int(input("Masukkan Gaji Pokok\t\t: ")) 
        setattr(pegawai, 'gajiPokok', self.gajiPokok)

        self.tunjanganJabatan = int(input("Masukkan Jumlah Tunjangan\t: "))
        setattr(pegawai, 'tunjanganJabatan', self.tunjanganJabatan) 

        self.pajak = int(input("Masukkan Jumlah Pajak\t\t: "))
        setattr(pegawai, 'pajak', self.pajak)

    def ubahGajiPokok(self):
        self.gajiPokok = int(input("Masukkan Gaji Pokok\t\t: "))
        setattr(pegawai, 'gajiPokok', self.gajiPokok)



    def gajiBersihl(self):
        a = self.gajiPokokJabatan
        b = self.tunjangan
        c = self.pajak
        gajiBersihPegawai = a+b-c 
        print("Gaji Bersih\t\t\t:",gajiBersihPegawai)

    def tampilPegawai(self):
        print("Nomor Induk Pegawai\t\t:", getattr(pegawai, 'NIP')) 
        print("Nama\t\t\t\t:", getattr(pegawai, 'nama')) 
        print("Gaji Pokok\t\t\t:", getattr(pegawai, 'gajiPokok'))
        print("Tunjangan Jabatan\t\t:", getattr(pegawai,'tunjanganJabatan')) 
        print("Pajak\t\t\t\t:", getattr(pegawai, 'pajak'))

class sekretaris(pegawai): 
    def __init__(self): 
        self.upahLembur = None

    def ubahUpah(self): 
        self.upahLembur = int(input("\nMasukkan Jumlah Upah Lembur\t: ")) 
        setattr(sekretaris, 'upahLembur', self.upahLembur)

    def gajiBersih2(self):
        a = self.gajiPokok
        b = self.tunjanganJabatan
        c = self.pajak
        d = self.upahLembur
        gajiBersihPegawai = (a+b+d)-c 
        print("Gaji Bersih\t\t\t: ",gajiBersihPegawai)

    def tampilSekretaris(self): 
        pegawai.tampilPegawai(self) 
        print("Upah Lembur\t\t\t:", getattr(sekretaris, 'upahLembur'))

class manajer (pegawai): 
    def __init_(self): 
        self.bonus = None

    def ubahBonus(self):
        self.bonus = int(input("\nMasukkan Bonus\t\t\t: ")) 
        setattr(manajer, 'bonus', self.bonus)
    
    def gajiBersih3(self):
        a = self.gajiPokok
        b = self.tunjanganJabatan
        c = self.pajak
        d = self.bonus
        gajiBersihPegawai = (a+b+d)-c
        print("Gaji Bersih\t\t\t:", gajiBersihPegawai)

    def tampilManajer(self):
        pegawai.tampilPegawai(self)
        print("Bomus\t\t\t\t:",getattr(manajer,'bonus'))


skr = sekretaris()
mnj = manajer()

print('+'+'-'*55+'+')
print('|'+' '*17+' INPUT DATA PEGAWAI '+' '*18+'|')
print('+'+'-'*55+'+')
skr.ubahJabatan()
print('+'+'-'*55+'+')
print('|'+' '*18+' INFORMASI PEGAWAI '+' '*18+'|')
print('+'+'-'*55+'+')
skr.tampilPegawai()
skr.gajiBersih1()

print("\nSilahkan pilih Jabatan yang tersedia : ")
print("1. Sekretaris\n2. Manajer\n3. Exit")
pilih = int(input("Masukkan pilihan anda : "))

if pilih == 1:
    skr.ubahUpah()
    print('+'+'-'*55+'+')
    print('|'+' '*17+' INFORMASI SEKRETARIS '+' '*18+'|')
    print('+'+'-'*55+'+')
    skr.tampilSekretaris()
    skr.gajiBersih2()

    while True:
        print("\nSilahkan pilih jika mau ada perubahan : ")
        print("1. Ubah gaji Pokok\n2. Ubah upah\n3. Exit")
        pilihan = int(input("Masukkan pilihan anda : "))
        if pilihan ==1:
            skr.ubahGajiPokok()
            print('+'+'-'*55+'+')
            print('|'+' '*17+' INFORMASI SEKRETARIS '+' '*18+'|')
            print('+'+'-'*55+'+')
            skr.tampilSekretaris()
            skr.gajiBersih2()

        elif pilihan ==2:
            skr.ubahUpah()
            print('+'+'-'*55+'+')
            print('|'+' '*17+' INFORMASI SEKRETARIS '+' '*18+'|')
            print('+'+'-'*55+'+')
            skr.tampilSekretaris()
            skr.gajiBersih2()
        
        else:
            print('+'+'-'*55+'+')
            print('|'+' '*18+'  TERIMA KASIH    '+' '*18+'|')
            print('+'+'-'*55+'+')
            break

elif pilih == 2:
    skr.ubahUpah()
    print('+'+'-'*55+'+')
    print('|'+' '*18+' INFORMASI MANAJER '+' '*18+'|')
    print('+'+'-'*55+'+')
    mnj.tampilManajer()
    mnj.gajiBersih3()

    while True:
        print("\nSilahkan pilih jika mau ada perubahan : ")
        print("1. Ubah gaji Pokok\n2. Ubah upah\n3. Exit")
        pilihan = int(input("Masukkan pilihan anda : "))
        if pilihan ==1:
            mnj.ubahGajiPokok()
            print('+'+'-'*55+'+')
            print('|'+' '*18+' INFORMASI MANAJER '+' '*18+'|')
            print('+'+'-'*55+'+')
            mnj.tampilManajer()
            mnj.gajiBersih3()
            
        elif pilihan ==2:
            mnj.ubahBonus()
            print('+'+'-'*55+'+')
            print('|'+' '*18+' INFORMASI MANAJER '+' '*18+'|')
            print('+'+'-'*55+'+')
            mnj.tampilManajer()
            mnj.gajiBersih3()
        
        else:
            print('+'+'-'*55+'+')
            print('|'+' '*18+'  TERIMA KASIH    '+' '*18+'|')
            print('+'+'-'*55+'+')
            break
else:
    print('+'+'-'*55+'+')
    print('|'+' '*18+'  TERIMA KASIH    '+' '*18+'|')
    print('+'+'-'*55+'+')
