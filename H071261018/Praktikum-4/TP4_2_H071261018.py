def hitung_statistik(*args):
    rata = sum(args) / len(args)
    tertinggi = max(args)
    terendah =min(args)
    return rata, tertinggi, terendah

daftar_nilai = []
while True:
    teks_nilai = input ("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if teks_nilai == "":
        break
    try:
        nilai = int(teks_nilai)
    except ValueError:
        nilai = float(teks_nilai)

    daftar_nilai.append(nilai)
if not daftar_nilai:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = hitung_statistik(*daftar_nilai)
    print(f"Rata-rata kelas:  {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")
    
