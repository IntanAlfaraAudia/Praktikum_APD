users = {
    "intan": {"password": "intan123", "role": "admin"}
}

reservations = {
    1: {"nama_user": "Alfara", "layanan": "Paket Hair care", "tanggal": "10 Oktober", "waktu": "14:00"},
    2: {"nama_user": "Meiga", "layanan": "Paket Facial", "tanggal": "11 Oktober", "waktu": "10:00"},
    3: {"nama_user": "Tasya", "layanan": "Paket Body Massage", "tanggal": "11 Oktober", "waktu": "15:30"},
    4: {"nama_user": "Zahra", "layanan": "Paket Aromatherapy", "tanggal": "12 Oktober", "waktu": "11:00"},
    5: {"nama_user": "Aulia", "layanan": "Paket Manicure", "tanggal": "12 Oktober", "waktu": "16:00"}
}

paket_SPA = {
    1: "Paket Hair Care",
    2: "Paket Facial",
    3: "Paket Body Massage",
    4: "Paket Aromatherapy",
    5: "Paket Manicure & Pedicure",
    6: "Paket Body Scrub",
    7: "Paket Reflexology",
    8: "Paket Hot Stone Massage",
    9: "Paket Sauna",
    10: "Paket Anti-Aging"
}

penguna = None

def tampilkan_paket_spa():
    print("\n--- PILIH PAKET SPA ---")
    for key, value in paket_SPA.items():
        print(f"{key}. {value}")

def tampilkan_menu():
    print("\n=== SISTEM MANAJEMEN RESERVASI SPA ===")
    print("1. Registrasi")
    print("2. Login")
    print("3. Keluar")

def tambah_reservasi(nama_pengguna, layanan, tanggal, waktu):
    reservation_id = len(reservations) + 1
    reservations[reservation_id] = {
        "nama_user": nama_pengguna,
        "layanan": layanan,
        "tanggal": tanggal,
        "waktu": waktu
    }
    print("Reservasi berhasil ditambahkan!")

def ubah_reservasi():
    try:
        nomor_res = int(input("Masukkan nomor reservasi yang ingin diubah: "))
        if nomor_res in reservations:
            nama_baru = input("Nama baru (lanjutkan jika tidak ingin mengganti): ")
            tampilkan_paket_spa()
            layanan_baru_idx = input("Paket baru (lanjutkan jika tidak ingin mengganti): ")
            tanggal_baru = input("Tanggal baru (lanjutkan jika tidak ingin mengganti): ")
            waktu_baru = input("Waktu baru (lanjutkan jika tidak ingin mengganti): ")

            if nama_baru:
                reservations[nomor_res]["nama_user"] = nama_baru
            if layanan_baru_idx.isdigit() and int(layanan_baru_idx) in paket_SPA:
                reservations[nomor_res]["layanan"] = paket_SPA[int(layanan_baru_idx)]
            if tanggal_baru:
                reservations[nomor_res]["tanggal"] = tanggal_baru
            if waktu_baru:
                reservations[nomor_res]["waktu"] = waktu_baru
            print("Reservasi berhasil diubah.")
        else:
            print("Nomor reservasi tidak valid.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan nomor reservasi dengan benar.")

def hapus_reservasi():
    try:
        nomor_res = int(input("Masukkan nomor reservasi yang ingin dihapus: "))
        if nomor_res in reservations:
            del reservations[nomor_res]
            print("Reservasi berhasil dihapus.")
        else:
            print("Reservasi tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Masukkan nomor reservasi yang benar.")

def lihat_reservasi():
    print("\n--- DAFTAR RESERVASI ---")
    if reservations:
        for res_id, reservation in reservations.items():
            print(f"{res_id}. {reservation}")
    else:
        print("Belum ada reservasi.")

while True:
    tampilkan_menu()
    pilihan = input("Pilih opsi (1/2/3): ")
    
    if pilihan == "1":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username in users:
            print("Username sudah terdaftar.")
        else:
            users[username] = {"password": password, "role": "user"}
            print("Registrasi berhasil!")
    
    elif pilihan == "2":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        pengguna = users.get(username)
        if pengguna and pengguna["password"] == password:
            print(f"Login berhasil! Selamat datang, {username}!")
            if pengguna["role"] == "admin":
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
                    try:
                        if sub_pilihan == "1":
                            nama_user = input("Nama pengguna: ")
                            tampilkan_paket_spa()
                            layanan_idx = int(input("Pilih nomor layanan: "))
                            if layanan_idx not in paket_SPA:
                                raise ValueError("Nomor layanan tidak valid.")
                            layanan = paket_SPA.get(layanan_idx)
                            tanggal = input("Tanggal reservasi: ")
                            waktu = input("Waktu reservasi: ")
                            tambah_reservasi(nama_user, layanan, tanggal, waktu)

                        elif sub_pilihan == "2":
                            lihat_reservasi()

                        elif sub_pilihan == "3":
                            ubah_reservasi()

                        elif sub_pilihan == "4":
                            hapus_reservasi()

                        elif sub_pilihan == "5":
                            print("Logout berhasil.")
                            pengguna = None
                            break
                        else:
                            print("Pilihan tidak valid.")
                    except ValueError as e:
                        print(f"Error: {e}")
                
            elif pengguna["role"] == "user":
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
                        lihat_reservasi()
                    elif sub_pilihan == "2":
                        print("Logout berhasil.")
                        pengguna = None
                        break
                    else:
                        print("Pilihan tidak valid.")
        else:
            print("Username atau password salah.")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan sistem.")
        break
    else:
        print("Pilihan tidak valid.")
