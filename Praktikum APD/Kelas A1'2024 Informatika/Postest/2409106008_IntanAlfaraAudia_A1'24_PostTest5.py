users = [["intan", "intan123", "admin"]]
user = []

reservations = [
    ["Alfara", "Paket Hair care", "10 Oktober", "14:00"],
    ["Meiga", "Paket Facial", "11 Oktober", "10:00"],
    ["Tasya", "Paket Body Massage", "11 Oktober", "15:30"],
    ["Zahra", "Paket Aromatherapy", "12 Oktober", "11:00"],
    ["Aulia", "Paket Manicure", "12 Oktober", "16:00"]
]

paket_SPA = [
    "Paket Hair Care",
    "Paket Facial",
    "Paket Body Massage",
    "Paket Aromatherapy",
    "Paket Manicure & Pedicure",
    "Paket Body Scrub",
    "Paket Reflexology",
    "Paket Hot Stone Massage",
    "Paket Sauna",
    "Paket Anti-Aging"
]

while True:
    print("\n=== SISTEM MANAJEMEN RESERVASI SPA ===")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Pilih opsi (1/2/3): ")

    if pilihan == "1":
        print("\n--- REGISTER ---")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if any(user[0] == username for user in users):
            print("Username sudah terdaftar.")
        else:
            users.append([username, password, "user"]) 
            print("Registrasi berhasil!")

    elif pilihan == "2":
        print("\n--- LOGIN ---")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        current_user = next((user for user in users if user[0] == username and user[1] == password), None)
        if current_user:
            print(f"Login berhasil! Selamat datang, {current_user[0]}!")
            if current_user[2] == "admin":
                while True:
                    print(
                    """
                    ===========================
                    |  SISTEM RESERVASI SPA   |
                    ===========================
                    |   1. TAMBAH RESERVASI   |           
                    |   2. LIHAT RESERVASI    |          
                    |   3. UBAH RESERVASI     |     
                    |   4. HAPUS RESERVASI    |      
                    |   5. KELUAR             |  
                    ===========================
                    """
                    )
                    sub_pilihan = input("Pilih opsi (1/2/3/4/5): ")
                    if sub_pilihan == "1":
                        print("\n--- TAMBAH RESERVASI ---")
                        nama_user = input("Nama pengguna: ")
                        print("\n--- PILIH PAKET SPA ---")
                        for i in range(len(paket_SPA)):
                            print(f"{i + 1}. {paket_SPA[i]}")
                        layanan_idx = int(input("Pilih nomor layanan (1-10): ")) - 1
                        layanan = paket_SPA[layanan_idx]
                        tanggal = input("Tanggal reservasi (tanggal bulan): ")
                        waktu = input("Waktu reservasi: ")
                        reservations.append([nama_user, layanan, tanggal, waktu])
                        print("Reservasi berhasil ditambahkan.")
                    elif sub_pilihan == "2":
                        print("\n--- DAFTAR RESERVASI ---")
                        if reservations:
                            for i in range(len(reservations)):
                                print(f"{i + 1}. {reservations[i]}")
                        else:
                            print("Belum ada reservasi.")
                    elif sub_pilihan == "3":
                        print("--- Ubah Reservasi ---")
                        nomor_res = int(input("Masukkan nomor reservasi yang ingin diubah: ")) - 1
                        if 0 <= nomor_res < len(reservations):
                            nama_baru = input("Nama baru (lanjutkan jika tidak ingin mengganti): ")
                            print("\n--- PILIH LAYANAN BARU) ---")
                            for i in range(len(paket_SPA)):
                                print(f"{i + 1}. {paket_SPA[i]}")
                            layanan_baru = input("paket baru (lanjutkan jika tidak ingin mengganti): ")
                            tanggal_baru = input("Tanggal baru (tanggal bulan)(lanjutkan jika tidak ingin mengganti):")
                            waktu_baru = input("Waktu baru (lanjutkan jika tidak ingin mengganti): ")

                            if nama_baru:
                                reservations[nomor_res][0] = nama_baru
                            if layanan_baru:
                                reservations[nomor_res][1] = layanan_baru
                            if tanggal_baru:
                                reservations[nomor_res][2] = tanggal_baru
                            if waktu_baru:
                                reservations[nomor_res][3] = waktu_baru


                    elif sub_pilihan == "4":
                        print("--- Hapus Reservasi ---")
                        nomor_res = int(input("Masukkan nomor reservasi yang ingin dihapus: ")) - 1
                        if 0 <= nomor_res < len(reservations):
                            del reservations[nomor_res]
                            print("Reservasi berhasil dihapus.")
                        else:
                            print("Reservasi tidak ditemukan.")
                    elif sub_pilihan == "5":
                        print("Logout berhasil.")
                        current_user = None
                        break
                    else:
                        print("Pilihan tidak valid.")
            elif current_user[2] == "user":
                while True:
                    print(
                    """
                    ===========================
                    |  SISTEM RESERVASI SPA   |
                    ===========================
                    |   1. LIHAT RESERVASI    |
                    |   2. KELUAR             |
                    ===========================
                    """
                    )
                    sub_pilihan = input("Pilih opsi (1/2): ")
                    if sub_pilihan == "1":
                        print("\n--- DAFTAR RESERVASI ---")
                        if reservations:
                            for i in range(len(reservations)):
                                print(f"{i + 1}. {reservations[i]}")
                        else:
                            print("Belum ada reservasi.")
                    elif sub_pilihan == "2":
                        print("Logout berhasil.")
                        current_user = None
                        break
                    else:
                        print("Pilihan tidak valid.")
    elif pilihan == "3":
        print("Terima kasih telah menggunakan sistem.")
        break
    else :
        print("Tidak valid")

