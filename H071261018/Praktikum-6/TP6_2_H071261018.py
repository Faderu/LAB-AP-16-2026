def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()

    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebelumnya!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih = nama_pemilih.lower()
    kandidat = pilihan.capitalize()

    if pemilih in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
    elif kandidat not in kandidat_set:
        print(f"Error! Kandidat '{kandidat}' tidak terdaftar. Suara tidak dicatat.")
    else:
        rekap_suara[pemilih] = kandidat
        print(f"Suara '{nama_pemilih}' untuk '{kandidat}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    daftar = list(kandidat_set)
    daftar.sort()

    for kandidat in daftar:
        perolehan[kandidat] = 0

    for pemilih in rekap_suara:
        pilihan = rekap_suara[pemilih]
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    print("=" * 40)
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)

    total_suara = 0

    for kandidat in perolehan:
        print(f" {kandidat}: {perolehan[kandidat]} suara")
        total_suara += perolehan[kandidat]

    print(f"Total suara masuk: {total_suara}")

    if total_suara == 0:
        print("Belum ada suara masuk, pemenang belum dapat ditentukan.")
    else:
        tertinggi = 0
        for kandidat in perolehan:
            if perolehan[kandidat] > tertinggi:
                tertinggi = perolehan[kandidat]

        pemenang = []
        for kandidat in perolehan:
            if perolehan[kandidat] == tertinggi:
                pemenang.append(kandidat)

        if len(pemenang) > 1:
            print(f"Hasil SERI antara: {', '.join(pemenang)}")
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")

    print("=" * 40)


kandidat_set = set()
rekap_suara = {}

print("=" * 40)
print(" SISTEM PEMILIHAN KETUA KELAS")
print("=" * 40)

print("--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()

    if nama == "":
        if len(kandidat_set) < 2:
            print("Minimal harus ada 2 kandidat! Silakan tambah kandidat.")
        else:
            break
    else:
        daftar_kandidat(kandidat_set, nama)

print(f"Kandidat terdaftar: {kandidat_set}")

print("\n--- FASE PEMUNGUTAN SUARA ---")

while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()

    if nama_pemilih == "":
        break

    print(f"Kandidat yang tersedia: {kandidat_set}")
    pilihan = input("Pilih kandidat: ").strip()

    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)