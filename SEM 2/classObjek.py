class KlubSepakbola:
    def __init__(self, namaKlub, lisensiKlub):
        self.namaKlub = namaKlub
        self.lisensiKlub = lisensiKlub

    
    def getNamaKlub(self):
        return self.namaKlub

    def getLisensiKlub(self):
        return self.lisensiKlub


class pemainBola(KlubSepakbola):
    def __init__(self, namaPemain, nomorPunggung, skillPemain):
        self.namaPemain = namaPemain
        self.nomorPunggung = nomorPunggung
        self.skillPemain = skillPemain
 
    def getNamaPemain(self):
        return self.namaPemain

    def getnomorPunggung(self):
        return self.nomorPunggung

    def getskillPemain(self):
        return self.skillPemain  

    def tampilkan():
        print(f"\nKlub Sepakbola {b.getNamaKlub()} dengan Lisensi {b.getLisensiKlub()} memiliki pemain bola bernama {c.getNamaPemain()} dengan nomor punggung {c.getnomorPunggung()} dan mempunyai skill {c.getskillPemain()}")

b = KlubSepakbola(namaKlub=input("Masukkan Nama Klub : "), lisensiKlub=input("Masukkan Lisensi Klub : " ))

c = pemainBola(namaPemain=input("Masukkan Nama Pemain Bola : "), nomorPunggung=input("Masukkan Nomor Punggung : "), skillPemain=input("Masukkan Skill Pemain : "))

pemainBola.tampilkan()