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
    hasil_pencarian = []

    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil_pencarian.append(buku)

    if hasil_pencarian:
        print(f"Ditemukan {len(hasil_pencarian)} buku:")

        for nomor, buku in enumerate(hasil_pencarian, start=1):
            print(
                f"{nomor}. {buku['judul']} - {buku['penulis']} "
                f"| Rp{buku['harga']} | Stok: {buku['stok']}"
            )
    else:
        print("Buku dengan kata kunci tersebut tidak ditemukan.")


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:
                print("Update gagal. Stok tidak boleh menjadi negatif.")
                return

            buku["stok"] = stok_baru

            if jumlah >= 0:
                print(
                    f"Stok '{buku['judul']}' bertambah {jumlah}. "
                    f"Stok sekarang: {buku['stok']}"
                )
            else:
                print(
                    f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. "
                    f"Stok sekarang: {buku['stok']}"
                )

            return

    print("Buku tidak ditemukan.")


def ringkasan_inventaris(inventaris):
    jumlah_jenis = len(inventaris)
    total_stok = 0
    total_nilai_aset = 0

    for buku in inventaris:
        total_stok += buku["stok"]
        total_nilai_aset += buku["harga"] * buku["stok"]

    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)
    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_nilai_aset}")

    if inventaris:
        buku_termahal = max(inventaris, key=lambda buku: buku["harga"])
        print(
            f"Buku termahal     : {buku_termahal['judul']} "
            f"(Rp{buku_termahal['harga']})"
        )
    else:
        print("Buku termahal     : Belum ada buku.")

    print("=" * 40)


inventaris = []

print("=" * 40)
print("SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("=" * 40)

while True:
    print("\nMenu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")

        try:
            harga = int(input("Harga: Rp"))
            stok = int(input("Stok awal: "))

            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif.")
            else:
                tambah_buku(inventaris, judul, penulis, harga, stok)

        except ValueError:
            print("Harga dan stok harus berupa angka bulat.")

    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)

    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")

        try:
            jumlah = int(
                input("Jumlah perubahan (positif=tambah, negatif=kurang): ")
            )
            update_stok(inventaris, judul, jumlah)

        except ValueError:
            print("Jumlah perubahan stok harus berupa angka bulat.")

    elif pilihan == "4":
        ringkasan_inventaris(inventaris)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan tidak valid. Masukkan angka 1 sampai 5.")