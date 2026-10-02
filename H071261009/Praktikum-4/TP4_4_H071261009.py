def konversi_suhu(suhu: float, asal: str, tujuan: str) -> float:
    skala_valid = ("C", "F", "K")
    if asal not in skala_valid or tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")

    if asal == "C":
        celsius = suhu
    elif asal == "F":
        celsius = (suhu - 32) * 5 / 9
    else:
        celsius = suhu - 273.15

    if tujuan == "C":
        hasil = celsius
    elif tujuan == "F":
        hasil = celsius * 9 / 5 + 32
    else:
        hasil = celsius + 273.15

    return round(hasil, 2)


print("=== Konversi Suhu ===")
while True:
    teks_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if teks_suhu.strip().lower() == "selesai":
        break

    skala_asal = input("Skala asal (C/F/K): ").strip().upper()
    skala_tujuan = input("Skala tujuan (C/F/K): ").strip().upper()

    try:
        suhu = float(teks_suhu)
    except ValueError:
        print("Error: Suhu harus berupa angka.")
        continue

    try:
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
    except ValueError as e:
        print(e)
    else:
        print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")