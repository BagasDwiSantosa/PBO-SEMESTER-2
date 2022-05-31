class Penyakit:
    def __init__(self):
        self.jenis = None
        self.jenis=input("Masukan jenis Penyakit\t: ")
        setattr(Penyakit, 'jenis', self.jenis)

    def showInfo(self):
        print("\nshowInfo di class Penyakit") 
        print("jenis:", self.jenis)

class Menular(Penyakit):
    def __init__(self): 
        super().__init__()

    def showInfo(self):
        print("\nshowInfo di subclass Menular") 
        print("jenis:", self.jenis)

class TidakMenular(Penyakit):
    def __init__(self):
        super().__init__()

    def showInfo(self):
        print("\nshowInfo di subclass Tidak menular") 
        print("jenis :", self.jenis)

sakit = Penyakit() 
sakit.showInfo()

sakit2 = Menular() 
sakit2.showInfo()

#hanya mengetahui showinfo diclass animal
sakit3 = TidakMenular() 
sakit3.showInfo()