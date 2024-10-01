username  = input("buat user dengan nama depan atau nama panggilan: ")
password  = int(input("buat passoword dengan 3 angka NIM terakhir: "))
login_salah = 0 
max_login = 3

while login_salah < max_login: 
    User = input("\nMasukkan nama depan anda atau nama panggilan: ")
    Pass = int(input("Masukkan password anda: "))
    if User == username and Pass == password: 
        print("login berhasil")
        break
    else: 
        print("login gagal")
        login_salah += 1
        if login_salah == max_login :
            print ("login gagal 3 kali. Program dihentikan")
            exit()

while True: 
    print("\nPilih jenis kelamin: ")
    print("1.Pria")
    print("2.Wanita")
    jenis_kelamin = int(input("Pilihan 1/2: "))

    bb = float(input("\nMasukkan berat badan (dalam gram): "))
    tb = float(input("Masukkan tinggi badan (dalam KM): "))
    umur = int(input("Masukkan umur: "))

    if jenis_kelamin == 1:
        bmr = (0.01 * bb) + (625000 * tb) - (5 * umur) + 5
    elif jenis_kelamin == 2: 
        bmr = (0.01 * bb) + (625000 * tb) - (5 * umur) - 161
    else: 
        print ("tidak valid")

    print("""
    Level Aktivitas Harian: 
    1. Aktivitas Minimal (jarang bergerak)
    2. Aktivitas Sedang (olahraga 1-3 minggu sekali)
    3. Aktivitas Tinggi (olahraga 4-7 kali minggu sekali)
    """)

    pilihan_aktivitas = int(input("Pilihan 1/2/3: "))

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

    lanjut = input ("\nApakah anda ingin mengulang program? (ya/tidak): ")
    if lanjut != "ya": 
        print("Terima kasih! Program diberhentikan")
        break