# nama =  ["celio","shandy","farel","ghazali","vito","yuyun","adri","rizal","adi","ifnu"]

# print(nama[3])
# print("sebelum: ")
# print(nama)
# print("")
# print("sesudah")
# nama.insert(2,"afrizal")
# print(nama)
# nama[4]= "fufufafa"
# print(nama)
# hapus = nama.pop(2)
# print(nama)
# print(hapus)

# print(nama(2:0))
# print(nama(2:4))
# print(nama[1:9:2])

# nama =  ["celio","shandy","farel","ghazali","vito","yuyun","adri","rizal","adi","ifnu"]
# matkul = ["APD","APL","BASDAT","STRUKDAT","WEB","JARKOM"]
# data = nama+matkul

# data = ["farel","celio",[1,2,["hai",23,2.3,True]]]
# print(data[2][2][0])

# matkul = [1,2,3,4,[5,6,7,[2,3,4]]]
# print(matkul[4][::-1])

# matkul = [1,2,3,4,]
# for i in matkul:
#     print(i, end= ' ')

# matkul = [[1,2,3],[4,5,6]]
# for i in matkul:
#     for j in i:
#         print(j)

# matkul = [[1,2,3],[4,5,6],[7,8,9]]
# for i in matkul:
#     print(i)

# nama = ('farel','rizal','shandy','rijal')
# print(nama[1])

# mahasiswa = (69, "informatika","2209106044","aldy septian")
# print(mahasiswa[0:3])


# print( 
# """
# ===========================
# |   DATA MAHASISWA A24    |
# ===========================
# |    1. TAMBAH DATA       |           
# |    2. TAMPILKAN DATA    |          
# |    3. UBAH DATA         |     
# |    4. HAPUS DATA        |      
# |    5. KELUAR            |  
# ===========================
# """
# )

# data_mahasiswa = []
# while True:
#     pilih = int(input("PILIH : "))
#     if pilih == 1:
#         nama = input("NAMA : ")
#         nim = input("NIM : ")
#         kelas = input("KELAS : ")
#         data_mahasiswa.append([nama,nim,kelas])
#     elif pilih == 2:
#         for i in range(len(data_mahasiswa)):
#             print(f"\n Data Mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i][0]}\nNIM : {data_mahasiswa[i][1]}\nKELAS : {data_mahasiswa[i][2]}")
#     elif pilih == 3:
#         nama_lama = input("Nama Baru : ")
#         for i in range(len(data_mahasiswa)):
#             if data_mahasiswa[i][0] == nama_lama:
#                 nama_baru = input("NAMA : ")
#                 nim_baru = input("NIM : ")
#                 kelas_baru = input("KELAS : ")
#                 data_mahasiswa[i][0] = nama_baru
#                 data_mahasiswa[i][1] = nim_baru
#                 data_mahasiswa[i][2] = kelas_baru
#     elif pilih == 4:
#         nama_lama = input("Nama yang ingin dihapus")
#         for i in range(len(data_mahasiswa)):
#             if data_mahasiswa[i][0] == nama_lama:
#                 del data_mahasiswa[i]
#     elif pilih == 5:
#         print("Terima Kasih Telah Mengakses Data Mahasiswa")
#         break
#     else:
#         print("Anda Salah Input") 