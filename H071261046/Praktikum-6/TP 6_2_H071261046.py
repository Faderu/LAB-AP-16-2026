def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()
    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebagai kandidat!")
        return False
    kandidat_set.add(nama)  
    print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")
    return True


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pilihan = pilihan.capitalize()
    pemilih = nama_pemilih.lower()

    if pilihan not in kandidat_set:
        print(f"Error: Kandidat '{pilihan}' tidak ada! Suara tidak dicatat.")
        return False
    if pemilih in rekap_suara: 
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
        return False

    rekap_suara[pemilih] = pilihan  
    print(f"Suara '{nama_pemilih}' untuk '{pilihan}' berhasil dicatat!")
    return True


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0
    for pemilih in rekap_suara:
        pilihan = rekap_suara[pemilih]
        perolehan[pilihan] += 1
    return perolehan


def tampilkan_hasil(perolehan):
    print("=" * 40)
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)

    daftarNama = list(perolehan)
    daftarNama.sort()

    total = 0
    suaraTertinggi = 0
    for nama in daftarNama:
        print(f" {nama}: {perolehan[nama]} suara")
        total += perolehan[nama]
        if perolehan[nama] > suaraTertinggi:
            suaraTertinggi = perolehan[nama]
    print(f"Total suara masuk: {total}")

    pemenang = [nama for nama in daftarNama if perolehan[nama] == suaraTertinggi]

    if len(pemenang) > 1:
        print(f"Hasil SERI antara: {', '.join(pemenang)}")
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {suaraTertinggi} suara!")
    print("=" * 40)


def main():
    kandidatSet = set()
    rekapSuara = {}

    print("=" * 40)
    print(" SISTEM PEMILIHAN KETUA KELAS")
    print("=" * 40)

    print("--- FASE PENDAFTARAN KANDIDAT ---")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
        if nama == "":
            if len(kandidatSet) < 2:
                print("Minimal harus ada 2 kandidat sebelum lanjut!")
                continue
            break
        daftar_kandidat(kandidatSet, nama)
    print(f"Kandidat terdaftar: {kandidatSet}")

    print("--- FASE PEMUNGUTAN SUARA ---")
    while True:
        namaPemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
        if namaPemilih == "":
            break
        print(f"Kandidat yang tersedia: {kandidatSet}")
        pilihan = input("Pilih kandidat: ").strip()
        berikan_suara(rekapSuara, kandidatSet, namaPemilih, pilihan)

    perolehan = hitung_suara(rekapSuara, kandidatSet)
    tampilkan_hasil(perolehan)


main()