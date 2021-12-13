'''
Nama    : Adhistianita Safira Husna
NIM     : 1301213039
Kelas   : IF-45-09
'''

print("=== Angka Muncul Sekali ===\n")

# unique function
def unique(string):

    # definisikan list untuk menampung angka unik
    unique = []

    # cari menggunakan count dan masukkan ke dalam list unique
    for i in string:
        if string.count(i) == 1:
            unique.append(int(i))

    # kembalikan list unique
    return unique


# input string
n = input()

# panggil dan cetak unique function
print(unique(n))


print("\n=== Penjumlahan Angka ===\n")

# function untuk penjumlahan 2 bilangan dalam list
def jumlah(li, target):

    # nested loop untuk menambahkan dua bilangan
    for i in li:
        for j in li:
            if int(i) + int(j) == target and int(i) != int(j):
                return [li.index(i), li.index(j)]
                ''' keluar atau kembalikan langsung nilai dari function setelah 
                 mendapat penambahan pertama '''


# input dan casting
s = list(map(int, input("List\t: ").removeprefix("[").removesuffix("]").split(",")))
n = int(input("Target\t: "))

# panggil function jumlah
print(jumlah(s, n))


print("\n=== Total Kemunculan ===\n")

# most appear function untuk assign ke dict
def most_appear(li):
    dict = {}
    for i in li:
        # dict input: kemunculan
        dict[i[1:-1]] = li.count(i)
    
    # panggil dan kembalikan nilai dari hasil function urutin
    return urutin(dict)

# function urutin untuk mengurutkan mulai dari yang terkecil kemunculannya dahulu
def urutin(dict):

    # buat temporary list kosong untuk menyimpan key
    li, hasil = [], []

    # sort menurut kemunculannya
    se = list(dict.values())
    se.sort()

    # masukkan ke list sesuai urutan kemunculannya
    for i in range(len(se)):
        for k in dict:
            if dict[k] == se[i] and k not in li:
                li.append(k)
                
        # append hasil
        hasil.append("{}: {}".format(li[i], dict[li[i]]))
    
    # kembalikan hasil akhir pengurutan
    return hasil

# input dan casting
s = input("List\t: ").removeprefix("[").removesuffix("]").split(", ")

# panggil dan cetak iterasi function most appear
[print(i) for i in most_appear(s)]