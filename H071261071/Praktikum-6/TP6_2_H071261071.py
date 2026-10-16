def daftar_kandidat(kandidat_set, nama):
    nama_kandidat = nama.capitalize()

    if nama_kandidat in kandidat_set:
        print(f"'{nama_kandidat}' sudah terdaftar.")
        return False

    kandidat_set.add(nama_kandidat)
    print(f"'{nama_kandidat}' berhasil didaftarkan sebagai kandidat!")
    return True


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih_kecil = nama_pemilih.lower()

    if nama_pemilih_kecil in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
        return False

    kandidat_dipilih = None

    for kandidat in kandidat_set:
        if kandidat.lower() == pilihan.lower():
            kandidat_dipilih = kandidat
            break

    if kandidat_dipilih is None:
        print("Kandidat yang dipilih tidak terdaftar. Suara tidak dicatat.")
        return False

    rekap_suara[nama_pemilih_kecil] = kandidat_dipilih
    print(
        f"Suara '{nama_pemilih}' untuk '{kandidat_dipilih}' "
        "berhasil dicatat!"
    )
    return True


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in kandidat_set:
        perolehan[kandidat] = 0

    for kandidat_dipilih in rekap_suara.values():
        perolehan[kandidat_dipilih] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    print("=" * 40)
    print("HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)

    for kandidat, jumlah_suara in perolehan.items():
        print(f"{kandidat}: {jumlah_suara} suara")

    total_suara = sum(perolehan.values())
    print(f"Total suara masuk: {total_suara}")

    if total_suara == 0:
        print("Belum ada suara yang masuk.")
    else:
        suara_tertinggi = max(perolehan.values())
        pemenang = [
            kandidat
            for kandidat, jumlah in perolehan.items()
            if jumlah == suara_tertinggi
        ]

        if len(pemenang) > 1:
            print("Hasil SERI antara:", ", ".join(pemenang))
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(
                f"PEMENANG: {pemenang[0]} "
                f"dengan {suara_tertinggi} suara!"
            )

    print("=" * 40)


kandidat_set = set()
rekap_suara = {}

print("=" * 40)
print("SISTEM PEMILIHAN KETUA KELAS")
print("=" * 40)

print("\n--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")

    if nama == "":
        break

    daftar_kandidat(kandidat_set, nama)

while len(kandidat_set) < 2:
    print("Minimal harus ada 2 kandidat. Silakan daftarkan kandidat lagi.")
    nama = input("Masukkan nama kandidat: ")

    if nama != "":
        daftar_kandidat(kandidat_set, nama)

print("Kandidat terdaftar:", kandidat_set)

print("\n--- FASE PEMUNGUTAN SUARA ---")

while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")

    if nama_pemilih == "":
        break

    print("Kandidat yang tersedia:", kandidat_set)
    pilihan = input("Pilih kandidat: ")

    berikan_suara(
        rekap_suara,
        kandidat_set,
        nama_pemilih,
        pilihan
    )

perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)