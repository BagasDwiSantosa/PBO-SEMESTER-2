# def KelvinFarenheit(suhu):
#     assert(suhu >= 0), "Lebih dingin dari nol mutlak!"
#     # suhu terdingin atau nol mutlak terjadi ketika terdapat suhu 0 derajat kelvin
#     # sehingga tidak boleh ada suhu dibawah 0 derajat kelvin
#     return (((suhu-273)*1.8)+32)
# print (KelvinFarenheit(5),"Farenheit")
# print (KelvinFarenheit(515),"Farenheit")
# print (KelvinFarenheit(-5),"Farenheit")



class Hero(object):
 """__init__() functions as the class constructor"""
 def __init__(self, nama=None, alias=None, kelompok=None, kondisi=None):
    self.nama = nama
    self.alias = alias
    self.kelompok = kelompok
    self.kondisi = kondisi

listHero = []
listHero.append(Hero("Anthony Edward Stark","Iron Man","Avengers","Mati"))
listHero.append(Hero("Peter Jason Quill","Star-Lord","Guardians of Galaxy","Hilang"))
listHero.append(Hero("Barry Allen","The Flash","Justice League","Hidup"))
listHero.append(Hero("Thor Odinson","God of Thunder","Avengers","Hidup"))
listHero.append(Hero("Bruce Wayne","Batman","Justice League","Hidup"))

def panggilHero(pahlawan):
    assert(pahlawan.kelompok == "Avengers"), "Hero tidak bisa dipanggil."
    return print("Avengers Berkumpul!")

try:
    panggilHero(listHero[1])
except:
    print('Hero bukan bagian dari Avengers!')

try:
    panggilHero(listHero[1])
except AssertionError as error:
    print(error)
    print('Hero bukan bagian dari Avengers!')

try:
    panggilHero(listHero[1])
except AssertionError as error:
    print(error)
    print('Hero bukan bagian dari Avengers!')
else:
    k = listHero[1].kelompok
    print("Hero bagian dari",k+'!')


try:
    panggilHero(listHero[0])
except AssertionError as error:
    print(error)
    print('Hero bukan bagian dari Avengers!')
else:
    k = listHero[0].kelompok
    print("Hero bagian dari",k+'!')


try:
    panggilHero(listHero[0])
except AssertionError as error:
    print(error)
    print('Hero bukan bagian dari Avengers!\n')
else:
    k = listHero[0].kelompok
    print("Hero bagian dari",k+'!\n')
finally:
    print('Resume:')
    print('=============================')
    print("Nama: {}\nAlias: {}\nKondisi: {}".format(listHero[0].nama, listHero[0].alias,
    listHero[0].kondisi))
    print('=============================')