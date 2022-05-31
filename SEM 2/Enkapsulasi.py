print("+"+"-"*50+"+")
print("|"+" "*5+"  PORTAL AKADEMIK MAHASISWA UNJANI YK   "+" "*5+"|")
print("+"+"-"*50+"+")

class pordik:
    def __init__(self):
        self.username = None
        self.__password = None

    def inputLogin(self):
        print("+"+"-"*50+"+")
        self.username = input("  Username\t: ")
        setattr(pordik, 'username', self.username)
        self.__password = input("  Password\t: ")
        setattr(pordik, '__password', self.__password)

    def tampilLogin(self):
        print("+"+"-"*50+"+")
        print("| SELAMAT DATANG DI PORTAL AKADEMIK, "+ self.username+" "*(14-len(self.username))+"|")
        print("+"+"-"*50+"+")

hasil = pordik()
hasil.inputLogin()
hasil.tampilLogin()