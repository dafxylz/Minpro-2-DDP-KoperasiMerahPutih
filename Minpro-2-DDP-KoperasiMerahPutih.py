
import os
import pwinput
from prettytable import PrettyTable

akun = {
    "admin": ["123", "admin"],
    "user": ["123", "user"]
}

jenis = ("Kecil", "Sedang", "Besar")
jumlah = (1000000, 3000000, 5000000)
pinjaman = []

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("=== LOGIN KOPERASI ===")
    user = input("Username: ")
    password = pwinput.pwinput("Password: ")

    if user not in akun or password != akun[user][0]:
        print("Login gagal!")
        input("Enter...")
        continue

    role = akun[user][1]

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n=== MENU", role.upper(), "===")

        if role == "user":
            print("1. Pilih Pinjaman")
            print("2. Bayar Pinjaman")
            print("3. Lihat Pinjaman")
            print("4. keluar")
        else:
            print("1. Tambah Peminjam")
            print("2. Hapus Peminjam")
            print("3. Lihat Peminjam")
            print("4. keluar")

        menu = input("Pilih: ")

        if role == "user":
            if menu == "1":
                for i in range(3):
                    print(i + 1, jenis[i], jumlah[i])

                try:
                    p = int(input("Pilih: "))

                    if 1 <= p <= 3:
                        pinjaman.append({
                            "nama": user,
                            "jenis": jenis[p-1],
                            "jumlah": jumlah[p-1],
                            "bayar": 0
                        })
                        print("Pinjaman berhasil!")
                    else:
                        print("Pilihan salah!")
                except:
                    print("Masukkan angka!")

            elif menu == "2":
                if pinjaman:
                    try:
                        bayar = int(input("Bayar: "))
                        data = pinjaman[0]
                        sisa = data["jumlah"] - data["bayar"]

                        if 0 < bayar <= sisa:
                            data["bayar"] += bayar
                            print("Pembayaran berhasil!")
                        else:
                            print("Jumlah pembayaran salah!")
                    except:
                        print("Masukkan angka!")
                else:
                    print("Belum ada pinjaman.")

            elif menu == "3":
                if pinjaman:
                    tabel = PrettyTable(
                        ["No", "Nama", "Jenis", "Pinjaman", "Bayar", "Sisa"]
                    )

                    for i, data in enumerate(pinjaman, 1):
                        tabel.add_row([
                            i,
                            data["nama"],
                            data["jenis"],
                            data["jumlah"],
                            data["bayar"],
                            data["jumlah"] - data["bayar"]
                        ])

                    print(tabel)
                else:
                    print("Belum ada pinjaman.")

            elif menu == "4":
                break

        else:
            os.system("cls" if os.name == "nt" else "clear")
            if menu == "1":
                os.system("cls" if os.name == "nt" else "clear")
                nama = input("Nama peminjam: ")

                for i in range(3):
                    print(i + 1, jenis[i], jumlah[i])

                try:
                    p = int(input("Pilih: "))
                    if 1 <= p <= 3:
                        pinjaman.append({
                            "nama": nama,
                            "jenis": jenis[p-1],
                            "jumlah": jumlah[p-1],
                            "bayar": 0
                        })
                        print("Pinjaman berhasil ditambahkan!")
                    else:
                        print("Pilihan salah!")
                except:
                    print("Masukkan angka!")

            elif menu == "2":
                os.system("cls" if os.name == "nt" else "clear")
                if pinjaman:
                    for i, data in enumerate(pinjaman, 1):
                        print(i, data["nama"], data["jenis"])

                    try:
                        h = int(input("Hapus nomor: "))

                        if 1 <= h <= len(pinjaman):
                            pinjaman.pop(h-1)
                            print("Berhasil dihapus!")
                        else:
                            print("Nomor tidak ada!")
                    except:
                        print("Masukkan angka!")
                else:
                    print("Belum ada pinjaman.")

            elif menu == "3":
                os.system("cls" if os.name == "nt" else "clear")
                if pinjaman:
                    tabel = PrettyTable(
                        ["No", "Nama", "Jenis", "Pinjaman", "Bayar", "Sisa"]
                    )

                    for i, data in enumerate(pinjaman, 1):
                        tabel.add_row([
                            i,
                            data["nama"],
                            data["jenis"],
                            data["jumlah"],
                            data["bayar"],
                            data["jumlah"] - data["bayar"]
                        ])

                    print(tabel)
                else:
                    print("Belum ada pinjaman.")

            elif menu == "4":
                break

        input("\nTekan Untuk Melanjutkan...")
