def hitung_statistik(*nilai):
    rata_rata = sum(nilai) / len(nilai)
    return rata_rata, max(nilai), min(nilai)


daftar_nilai = []
while True:
    masukan = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if masukan == "":
        break
    angka = float(masukan)
    if angka == int(angka):
        angka = int(angka) 
    daftar_nilai.append(angka)

if len(daftar_nilai) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata_rata, tertinggi, terendah = hitung_statistik(*daftar_nilai)
    print(f"Rata-rata kelas: {rata_rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")