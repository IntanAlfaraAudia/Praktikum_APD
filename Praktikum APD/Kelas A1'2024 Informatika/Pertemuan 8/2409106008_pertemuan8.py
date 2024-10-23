#if:

#list = [1,2,3]

# print(list)

# x = 0 
# assert x != 0 

# X = 12 
# x.append(10)

# import os
# os.system("pause")

# dict = {
#     'key' : 1
# }

# print{dicgt['lele']}

# x = ?

# print(x)

# num = 10
# print('hello' + num)

# if num == 10:
# print(num)

# x = 1 
# y = 0 
# print(x/y)

# try: 
#     angka = int(input("masukkan angka: "))
# except ValueError:
#     print("input salah")
# except TypeError:
    #code
# else:
#     print("berhasil")
# finally: 
#     print("Finale") #selalu dijalankan setelah blok try 

# try:
#     nama = str(input("nama anda: "))
#     if len(nama) > 5: 
#         ralse ValueError ("nama tidak boleh lebih dari 5 karakter")

# except ValueError as e : 
#     print(e)  

# try:
#     nim = int(input("masukkan nim anda: "))

#     if not nim: 
#         raise ValueError("nim tidak boleh kosong")
#     if not nim.isdigit()
#         raise TypeError ("nim harus berupa angka")
#     if len(nim) != 10
#         raise ValueError ("nim harus 10 digit")
    
# except TypeError as T:
#     print(T)
# except ValueError as E:
#     print(E)

# else:
#     print(f"nim anda adalah{nim}")

# finally
#     print("program selesai...")

path = './folder_ini/data.txt'
file = open(path)

with open(path,'r') as file:
    konten = file.read()
    print(konten)
    for i in file:
        print(i, end= ' ')

path = './folder_ini/data.json'

# with open(path, 'W') as file:
#     file.write('Shandy, 20,pria\n')
#     file.write('yuyun,19,wanita')

# with open(path, 'r') as file:
#     konten = file.read()
#     print(konten)

try:
    with open(path, 'r') as file:
    konten = file.read()
    print(konten)
except FileNotFoundError:
    with.open(path,'w') as file : 
    file.write('Shandy, 20,pria\n')
    file.write('yuyun,19,wanita')
