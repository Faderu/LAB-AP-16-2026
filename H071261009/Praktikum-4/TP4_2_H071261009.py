def ubah_angka(teks: str) -> int | float:
    try:
        return int(teks)
    except ValueError:
        return float(teks)


def rekap_nilai(*nilai: int | float) -> tuple[float, int | float, int | float]:
    rata = sum(nilai) / len(nilai)
    return rata, max(nilai), min(nilai)


daftar_nilai = []
while True:
    masukan = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if masukan == "":
        break
    daftar_nilai.append(ubah_angka(masukan))

if len(daftar_nilai) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = rekap_nilai(*daftar_nilai)
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")