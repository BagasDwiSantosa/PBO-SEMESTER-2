class PrismaSegitiga: 
    def pilihan():
        print('_'*65+' ')
        print('|'+'='*8+'-'*8+'>'+' '*3+" Program Prisma Segitiga "+' '*3+'<'+'-'*8+'='*8+'|')
        print('_'*65+' ')
        print("""
Silahkan Pilih opsi yang tersedia dibawah :
        1. Menghitung Keliling Alas Prisma Segitiga 
        2. Menghitung Luas Permukaan Prisma Segitiga
        3. Menghitung Volume Prisma Segitiga
        4. Keluar Program""")


    def __init__(self, sisi1, sisi2, sisi3, luasAlas, kelilingAlas, tinggiPrisma):
        self.sisi1 = sisi1 
        self.sisi2 = sisi2
        self.sisi3 = sisi3
        self.luasAlas = luasAlas
        self.kelilingAlas = kelilingAlas
        self.tinggiPrisma = tinggiPrisma

    def tampil_keliling(self):
        self.rumus1 = self.sisi1 + self.sisi2 + self.sisi3 
        print("Keliling Prisma Segitiga : ",self.rumus1)

    def tampil_luas(self):
        self.rumus2 = (2* self.luasAlas)+(self.kelilingAlas*self.tinggiPrisma) 
        print("Luas Permukaan Prisma Segitiga: ", self.rumus2)

    def tampil_volume(self): 
        self.rumus3 = (self.luasAlas * self.tinggiPrisma) 
        print("volume Prisma Segitiga : ",self.rumus3)


while True:
    PrismaSegitiga.pilihan() 
    pilih = int(input("Masukkan Opsi yang tersedia : "))
    if pilih == 1:

        inputan1= PrismaSegitiga(sisil=int (input("Masukkan Sisi 1: ")), sisi2=int(input ("Masukkan Sisi 2: ")), sisi3=int(input("Masukkan sisi 1: ")), luasAlas=0, kelilingAlas=0, tinggiPrisma=0) 
        inputan1.tampil_keliling()

        lanjut = input("\nKembali Ke Menu utama (Y/N) : ") 
        if lanjut == 'Y' or lanjut == 'y':
            print('')
            continue

        elif lanjut == 'N' or lanjut == 'n':
            print("+"+'_'*65+' ')
            print('|'+'='*8+'-'*8+'>'+' '*3+"      Terima Kasih      "+' '*3+'<'+'-'*8+'='*8+'|')
            print("+"+'_'*65+' ')
            break


    elif pilih == 2:

        inputan2 = PrismaSegitiga(luasAlass=int (input ("Masukkan Luas Alas: ")), kelilingalas=int(input("Masukkan Keliling Alas: ")), tinggiPrisma=int(input ("Masukkan Tinggi: ")), sisi1=0, sisi2=0, sisi3=0) 
        inputan2.tampil_luas() 
        lanjut=input("\nKembali Ke Menu utama (Y/N) : ") 
        lanjut = input("\nKembali Ke Menu utama (Y/N) : ") 
        if lanjut == 'Y' or lanjut == 'y':
            print('')
            continue

        elif lanjut == 'N' or lanjut == 'n':
            print("+"+'_'*65+' ')
            print('|'+'='*8+'-'*8+'>'+' '*3+"      Terima Kasih      "+' '*3+'<'+'-'*8+'='*8+'|')
            print("+"+'_'*65+' ')
            break

    elif pilih == 3:

        kamu = PrismaSegitiga (luasAlas=int (input ("Masukkan Luas Alas: ")), tinggiPrisma=int (input ("Masukkan Tinggi Prisma: ")), kelilingAlas=0, sisil=0, sisi2=0, sisi3=0)
        kamu.tampil_volume()

        lanjut = input("\nKembali Ke Menu utama (Y/N) : ") 
        if lanjut == 'Y' or lanjut == 'y':
            print('')
            continue

        elif lanjut == 'N' or lanjut == 'n':
            print("+"+'_'*65+' ')
            print('|'+'='*8+'-'*8+'>'+' '*3+"      Terima Kasih      "+' '*3+'<'+'-'*8+'='*8+'|')
            print("+"+'_'*65+' ')
            break

    elif lanjut == 'N' or lanjut == 'n':
        print("+"+'_'*65+' ')
        print('|'+'='*8+'-'*8+'>'+' '*3+"      Terima Kasih      "+' '*3+'<'+'-'*8+'='*8+'|')
        print("+"+'_'*65+' ')
        break