# def salam(salam):
#     print(salam)

# iso = "salam iso"
# salam(iso)

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# def luas_persegi2(sisi):
#     luas = sisi * sisi
#     return luas

# luas = luas_persegi(2)
# print(luas)

# print(luas_persegi(3))
# print(luas)

# membuat variabel global
# Nama = "Informatika"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
# # membuat variabel lokal
# def info():
#     Nama = "Teknik Elektro"
#     Mata_Kuliah = "Pengantar Teknik ELektro"

# def info2():
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)

# # mengakses variabel lokal
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)


# mengakses variabel global
# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)
# memanggil fungsi info
# info()

# fungsi untuk menampilkan semua data

# buku =[]

# def show_data():
#     if len(buku) <= 0:
#         print ("Belum Ada data")
#     else:
#         print("ID", "Nama Buku")
#         for indeks in range(len(buku)):
#             print (indeks, buku[indeks])


# def insert_data():
#     buku_baru = input("judul buku : ")
#     buku.append(buku_baru)
    
# # fungsi untuk edit data
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID buku: "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         buku[indeks] = judul_baru

# # fungsi untuk menghapus data
# def delete_data():
#     show_data()
#     indeks = int (input("masukkan ID buku :  "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         buku.remove(buku[indeks])

# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU: ")
#     print ("\n")
#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print (" pilihan tidak valid")

# while(True):
#     show_menu()

# def square_root(num):
#     precision=0.00001
#     if num < 0:
#         return "angka negatif tidak memiliki akar yang terdefinisi"
#     guess = num / 2.0
#     while abs(guess * guess - num) > precision:
#         return guess 
#     number = float(input("input angka: "))
#     result = square_root(number)
#     print(f"akar baru{number} adalah {result}")

#     import math
#     angka = 49
#     print(math.sqrt(angka))