


class pemainBola:
    def __init__(self, namaPemain, nomorPunggung, warnaJersey):
        self.namaPemain = namaPemain
        self.nomorPunggung = nomorPunggung
        self.warnaJersey = warnaJersey

    def skillPemain(self):
        skill = "Menendang, Mengumpan, Menyundul, Mendrible"
        print("Skill Pemain : "+skill)

    
    def tampilPemain(self):
        print("\nIDENTITAS LENGKAP PEMAIN DAN SKILLNYA")
        print(f"Nama Pemain : {self.namaPemain}\nNomor Punggung : {self.nomorPunggung}\nWarna Jersey : {self.warnaJersey}")


print("MASUKAN DATA PEMAIN SEPAK BOLA")
Pemain = pemainBola(namaPemain=input("Masukan Nama Pemain : "), nomorPunggung=input("Masukan Nomor Punggung : "), warnaJersey=input("Masukan Warna Jersey : "))
Pemain.tampilPemain()
Pemain.skillPemain()

while True:
    print("\nSilahkan Pilih opsi yang tersedia dibawah : ")
    print("""   1. Mengubah Data Pemain
    2. Mengambil Data Pemain
    3. Memeriksa Data Pemain
    4. Menghapus Data Pemain
    5. Keluar Program""")

    pilih = int(input("Pilih Opsi yang tersedia : "))

    if pilih == 1:
        print("MENGUBAH DATA PEMAIN SEPAK BOLA")
        setattrNama = input("Masukan Nama Pemain Baru : ")
        setattrNomor = input("Masukan Nomor Punggung Baru : ")
        setattrWarna = input("Masukan Warna Jersey baru : ")

        setattr(Pemain, 'namaPemain', setattrNama)
        setattr(Pemain, 'nomorPunggung', setattrNomor)
        setattr(Pemain, 'warnaJersey', setattrWarna)

        Pemain.tampilPemain()
        Pemain.skillPemain()

        lanjut = input("\nKembali ke Menu utama (Y/N) : ")
        if lanjut == 'Y' or lanjut == 'y':
            continue
        elif lanjut == 'N' or lanjut == 'n':
            print("TERIMAKASIH")
            break

    elif pilih == 2:
        print("Data pemain yang bisa diambil : namaPunggung/nomorPunggung/warnaJersey")
        ambil = input("Apa yang mau diambil : ")
        print(f"Hasil Pengambilan {ambil} "+getattr(Pemain, ambil))
        lanjut = input("\nKembali ke Menu utama (Y/N) : ")
        if lanjut == 'Y' or lanjut == 'y':
            continue
        elif lanjut == 'N' or lanjut == 'n':
            print("TERIMAKASIH")
            break 

    elif pilih == 3:
        print("Data yang bisa periksa : namaPunggung/nomorPunggung/warnaJersey")
        cek = input("Apa yang mau diperiksa : ")
        print(f"Hasil Pengcekan {cek} ", hasattr(Pemain, cek))
        lanjut = input("\nKembali ke Menu utama (Y/N) : ")
        if lanjut == 'Y' or lanjut == 'y':
            continue
        elif lanjut == 'N' or lanjut == 'n':
            print("TERIMAKASIH")
            break       

    elif pilih == 4:
        print("Data yang bisa dihapus : namaPunggung/nomorPunggung/warnaJersey")
        hapus = input("Apa yang mau dihapus : ")
        delattr(Pemain, hapus)
        print(f"Hasil Penghapusan {hapus} telah terhapus")
        lanjut = input("\nKembali ke Menu utama (Y/N) : ")
        if lanjut == 'Y' or lanjut == 'y':
            continue
        elif lanjut == 'N' or lanjut == 'n':
            print("TERIMAKASIH")
            break 

    else:
        print("TERIMAKASIH")
        break