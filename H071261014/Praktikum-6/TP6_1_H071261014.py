def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):
    hasil = []

    for b in inventaris:
        if kata_kunci.lower() in b["judul"].lower():
            hasil.append(b)

    if len(hasil) == 0:
        print("Buku tidak ditemukan.")
    else:
        print(f"Ditemukan {len(hasil)} buku:")
        for i, b in enumerate(hasil, 1):
            print(f" {i}. {b['judul']} - {b['penulis']} | Rp{b['harga']} | Stok: {b['stok']}")
    return hasil


def update_stok(inventaris, judul, jumlah):
    for b in inventaris:
        if b["judul"].lower() == judul.lower():
            stok_baru = b["stok"] + jumlah
            if stok_baru < 0:
                print(f"Gagal! Stok '{b['judul']}' tidak mencukupi "
                      f"(stok saat ini: {b['stok']}).")
                return False
            b["stok"] = stok_baru
            if jumlah >= 0:
                print(f"Stok '{b['judul']}' bertambah {jumlah}. Stok sekarang: {b['stok']}")
            else:
                print(f"Stok '{b['judul']}' berkurang {abs(jumlah)}. Stok sekarang: {b['stok']}")
            return True

    print(f"Error: Buku '{judul}' tidak ditemukan!")
    return False


def ringkasan_inventaris(inventaris):
    jumlah_jenis = len(inventaris)
    total_stok = 0
    total_aset = 0
    termahal = None

    for b in inventaris:
        total_stok += b["stok"]
        total_aset += b["harga"] * b["stok"]
        if termahal is None or b["harga"] > termahal["harga"]:
            termahal = b

    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)
    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset : Rp{total_aset}")
    if termahal is not None:
        print(f"Buku termahal : {termahal['judul']} (Rp{termahal['harga']})")
    else:
        print("Buku termahal : -")
    print("=" * 40)


def tampilkan_menu():
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")


def main():
    inventaris = []

    print("=" * 40)
    print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("=" * 40)

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            judul = input("Judul buku: ")
            penulis = input("Penulis: ")
            try:
                harga = int(input("Harga: "))
                stok = int(input("Stok awal: "))
                if harga < 0 or stok < 0:
                    print("Error: Harga dan stok tidak boleh negatif!")
                else:
                    tambah_buku(inventaris, judul, penulis, harga, stok)
            except ValueError:
                print("Error: Harga dan stok harus berupa angka!")

        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ")
            cari_buku(inventaris, kata_kunci)

        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ")
            try:
                jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
                update_stok(inventaris, judul, jumlah)
            except ValueError:
                print("Error: Jumlah perubahan harus berupa angka!")

        elif pilihan == "4":
            ringkasan_inventaris(inventaris)

        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break

        else:
            print("Pilihan tidak valid! Masukkan angka 1-5.")


main()