def hitung_statistik(*nilai):
    rata_rata = sum(nilai) / len(nilai)
    nilai_tertinggi = max(nilai)
    nilai_terendah = min(nilai)

    return rata_rata, nilai_tertinggi, nilai_terendah


daftar_nilai = []

while True:
    masukan = input(
        "Masukkan nilai ujian siswa (kosongkan untuk selesai): "
    ).strip()

    if masukan == "":
        break

    daftar_nilai.append(float(masukan))

if len(daftar_nilai) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = hitung_statistik(*daftar_nilai)

    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi:g}")
    print(f"Nilai terendah: {terendah:g}")