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
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)

    if len(hasil) == 0:
        print("Buku tidak ditemukan.")
    else:
        print(f"Ditemukan {len(hasil)} buku:")
        for i in range(len(hasil)):
            buku = hasil[i]
            print(f" {i + 1}. {buku['judul']} - {buku['penulis']} | "
                  f"Rp{buku['harga']} | Stok: {buku['stok']}")
    return hasil


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stokBaru = buku["stok"] + jumlah
            if stokBaru < 0:
                print(f"Gagal! Stok tidak mencukupi. Stok saat ini: {buku['stok']}")
                return False
            buku["stok"] = stokBaru  
            if jumlah >= 0:
                print(f"Stok '{buku['judul']}' bertambah {jumlah}. Stok sekarang: {buku['stok']}")
            else:
                print(f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. Stok sekarang: {buku['stok']}")
            return True
    print(f"Error: Buku '{judul}' tidak ditemukan!")
    return False


def ringkasan_inventaris(inventaris):
    jumlahJenis = len(inventaris)
    totalStok = 0
    totalAset = 0
    termahal = None

    for buku in inventaris:
        totalStok += buku["stok"]
        totalAset += buku["harga"] * buku["stok"]
        if termahal is None or buku["harga"] > termahal["harga"]:
            termahal = buku

    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)
    print(f"Jumlah jenis buku : {jumlahJenis}")
    print(f"Total seluruh stok: {totalStok}")
    print(f"Total nilai aset : Rp{totalAset}")
    if termahal is not None:
        print(f"Buku termahal : {termahal['judul']} (Rp{termahal['harga']})")
    else:
        print("Buku termahal : -")
    print("=" * 40)


def utama():
    inventaris = []  

    print("=" * 40)
    print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("=" * 40)

    while True:
        print("Menu:")
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
                harga = int(input("Harga: "))
                stok = int(input("Stok awal: "))
                if harga < 0 or stok < 0:
                    print("Error: Harga dan stok tidak boleh negatif!")
                else:
                    tambah_buku(inventaris, judul, penulis, harga, stok)
            except ValueError:
                print("Error: Harga dan stok harus berupa angka!")

        elif pilihan == "2":
            kataKunci = input("Masukkan kata kunci judul: ")
            cari_buku(inventaris, kataKunci)

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


utama()