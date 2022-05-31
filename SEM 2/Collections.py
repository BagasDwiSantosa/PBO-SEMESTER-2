list1 = [3,1,2,4,5]
list2 = ['Unjani', 'Sistem Informasi', 2019,2021]

list1.append(6)
print("Append list 1 ----->", list1)
list2.append('Bagas')
print("Append list 2 ----->", list2)


list1.sort()
print("Sort list 1 ----->", list1)

list1.remove(4)
print("Remove list 1 ----->", list1)
list2.remove(2019)
print("Remove list 2 ----->", list2)

print("Max list 1 ----->", max(list1))

print("Min list 1 ----->", min(list1))

print("Len list 1 ----->", len(list1))




#Mapping]
d_nilai = {
'andi':'A',
'budi':'B',
'citra':'C',
'hendra':'A',
'baron':'D'
}
print("daftar nilai: ",d_nilai)

# mengecek panjang dictionary
print("panjang dictionary: ",len(d_nilai),"\n")

# merubah entry yang sudah ada
d_nilai['citra']='B'
print("perubahan 1: ",d_nilai)

# menambah entry baru
d_nilai['tony']='A'
print("perubahan 2: ",d_nilai)

# mengecek panjang dictionary
print("panjang dictionary: ",len(d_nilai),"\n")

# menghapus entry
del d_nilai['citra']
print("perubahan 3: ",d_nilai)
print("panjang dictionary: ",len(d_nilai),"\n")

# mengosongkan dictionary
d_nilai.clear()
print("perubahan 4: ",d_nilai)
print("panjang dictionary: ",len(d_nilai),"\n")


#Sets
# set data campuran
data = {1, 2.0, "jarvis", (3,4,5)}
print('Set gabungan: ',data)
# bila kita mengisi duplikasi, set akan menghilangkan salah satu 
# output: {1,2,3}
angka = {1,2,2,3,3,3}
print('Set angka:',angka)
# set tidak bisa berisi anggota list
# contoh berikut akan muncul error TypeError
# set_baru = {1,2,[3,4,5]}
# supaya bisa program bisa jalan, baris diatas dikomen atau dihapus
# menambah anggota baru pada set angka
angka.add(4)
print('Set angka perubahan 1:',angka)
# menambah beberapa anggota sekaligus
angka.update([3,4,5,6])
print('Set angka perubahan 2:',angka)
# mengosongkan set
angka.clear()
print('Set angka perubahan 3:',angka)



# Membuat set A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print('A:',A)
print('B:',B)
# Gabungan menggunakan operator |
print('A gabung B: ',(A | B))
# Irisan menggunakan operator & 
print('A irisan B: ',(A & B))
# operasi selisih
print('A - B: ',(A - B))
# operasi komplemen
print('A komplemen B: ',(A ^ B))