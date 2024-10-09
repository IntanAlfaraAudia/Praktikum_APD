# Daftar_Buku = {
#     #Key        #Value
#     "Buku1" : "Harry Poter",
#     "Buku2" : "Percy Jakson",
#     "Buku3" : "Twilight"
# }

# print(Daftar_Buku["Buku2"])
# print(Daftar_Buku)
# print(Daftar_Buku["Buku1"])

# games = dict(Sekiro = "Action", Pokemon = "Advanture", Valorant = "FPS")
# print(games)

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : { #dictionary
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#         }
# }

# print(Biodata["KRS"][1])
# print(Biodata.get("Nama"))

# print(Biodata["Alamat"])
# print(Biodata.get("Alamat", "Kosong bang"))

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : { #dictionary
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"

#     }
# }
# for i, j in Biodata.items():
#     print(f"Key = {i} dan Value = {j}")

# for i in (Biodata):
#     print(Biodata)

# Film = {
#         "Avenger Endgame" : "Action",
#         "Sherlock Holmes" : "Mystery",
#         "The Conjuring" : "Horror"
#         }
# Film["ZombieLand"] = "Comedy"
# Film.update({"Hour" : "Thriller"})
# print(Film)

# Film = {
#         "Avenger Endgame" : "Action",
#         "Sherlock Holmes" : "Mystery",
#         "The Conjuring" : "Horror"
#         }
# print(Film)
# del Film["The Conjuring"]
# hapus = Film.pop("The conjuring")
# print(Film)
# print(f"Key yang dihapus = {hapus}")

# key = "Apel", "Jeruk", "Mangga"
# value = 1

# buah = dict.fromkeys(key, value)
# print(buah)

# Film = {
#         "Avenger Endgame" : "Action",
#         "Sherlock Holmes" : "Mystery",
#         "The Conjuring" : "Horror"
#         }

# for i in Film.values():
#     print(i, end=" ")

# print(Film)
# print("Film: ", Film.setdefault("oldbook", "horor"))
# print(Film)

# Musik = {
#     "The Chainsmoker" : ["All we Know", "The Paris"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")

# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for i, j in mahasiswa.items():
#     print(f"ID : {i}")
#     for i_a, j_a in j.items():
#         print(f"{i_a} : {j_a}")

# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
#     print("")

# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }

# print(f"sebelum : {mahasiswa}")
# mahasiswa[101]["Angkatan"] = 2023
# print(f"sedudah : {mahasiswa}")

# biodata = { 
#     "nama" : "intan",
#     "nim" : "2409106008",
#     "umur" : "18",
#     "alamat" : "paser", 
#     "jurusan" : "informatika"
# }

# print(biodata.get("nim"))
# biodata.update({"umur" : "20"})
# print(biodata)

# Biodata = {}

# while True:
#     print("1. Tambah")
#     print("2. Tampilakan")
#     print("3. Exit")
#     pilihan =  int(input("(1/2/3) : "))

#     if pilihan == 1:
#         nama = input("Masukkan nama :")
#         umur = input("Masukkan umur :")
#         alamat = input("Masukkan alamat :")

#         Biodata[nama] = { 
#             'Umur' : umur,
#             'Alamat' : alamat
#         }

#     elif pilihan == 2:
#         for nama, info in Biodata.items():
#             print(f"Nama : {nama}")
#             print(f"Umur : {info['Umur']}")
#             print(f"Alamat : {info['Alamat']}")
#     elif pilihan == 3:
#         print("exit ...")
#         break

#     else:
#         print("Invalid ... ... ")