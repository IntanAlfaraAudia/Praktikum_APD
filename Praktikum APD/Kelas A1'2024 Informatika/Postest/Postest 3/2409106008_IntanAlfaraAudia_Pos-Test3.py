print ("pilih jenis kelamin")
print ("1. pria")
print ("2. wanita")
jenis_kelamin = int(input("pilihan 1/2: "))
bb = float(input("\nmasukkan berat badan (dalam gram): "))
tb = float(input("masukkan tinggi badan (dalam KM): "))
umur = int(input("masukkan umur: "))


if jenis_kelamin == 1:
    bmr = (0.01 * bb) + (625000 * tb) - (5 * umur) + 5 
elif jenis_kelamin == 2: 
    bmr = (0.01 * bb) + (625000 * tb) - (5 * umur) - 161
else: 
    print ("tidak valid")

print("""
Level Aktivitas Harian
1. Aktivitas Minimal (jarang bergerak)
2. Aktivitas Sedang (olahraga 1-3 minggu sekali)
3. Aktivitas Tinggi (olahraga 4-7 kali minggu sekali)
""")
pilihan_aktivitas = int(input("pilihan 1/2/3: "))

if pilihan_aktivitas == 1:
    level_aktivitas = 1.25
elif pilihan_aktivitas == 2:
    level_aktivitas = 1.36
elif pilihan_aktivitas == 3:
    level_aktivitas = 1.72
else: 
    print("tidak valid")

tdee = bmr * level_aktivitas

print("\nKebutuhan Kalori Harian: ", tdee)