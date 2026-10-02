def konversi_suhu(suhu, skala_asal, skala_tujuan):
    # Mengubah ke Celcius dulu sebagai acuannya
    if skala_asal == "C":
        celcius = suhu
    elif skala_asal == "F":
        celcius = (suhu - 32) * 5 / 9
    elif skala_asal == "K":
        celcius = suhu - 273.15
    else:
        raise ValueError("Skala suhu tidak dikenali")

    # Mengubah dari Celcius ke skala tujuan 
    if skala_tujuan == "C":
        hasil = celcius 
    elif skala_tujuan == "F":
        hasil = celcius * 9 / 5 + 32
    elif skala_tujuan == "K":
        hasil = celcius + 273.15
    else:
        raise ValueError("Skala suhu tidak dikenali")
    return hasil

print("=== Konversi Suhu ===")

while True:
    teks_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if teks_suhu.lower() == "selesai":
        break

    suhu = float(teks_suhu)
    skala_asal = input("Skala asal (C/F/K): ").upper()
    skala_tujuan = input("Skala tujuan (C/F/K):  ").upper()

    try:
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")
    except ValueError:
        print("Eror: Skala suhu tidak dikenali.")

    
