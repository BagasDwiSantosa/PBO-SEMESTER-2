from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def bahan_bakar(self):
        pass

class Mobil(Kendaraan):
    def bahan_bakar(self):
        super().bahan_bakar()
        print("Pertamax")

class Motor(Kendaraan):
    # def fuel(self):
    def bahan_bakar(self):
        super().bahan_bakar()
        print("Pertamax Racing")

x = Mobil()
y = Motor()
x.bahan_bakar()
y.bahan_bakar()



from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
    def __init__(self,value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_something(self):
        pass

class tambah42(AbstractClassExample):
    def do_something(self):
        return self.value+42

class kali42(AbstractClassExample):
    def do_something(self):
        return self.value*42

x = tambah42(10)
y = kali42(10)

print(x.do_something())
print(y.do_something())