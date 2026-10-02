def konversi_suhu(suhu, asal, tujuan):
    if asal not in ("C", "F", "K") or tujuan not in ("C", "F", "K"):
        raise ValueError
    
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

    return hasil

print("Konversi Suhu")
while True:
    masukan = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if masukan == "selesai":
        break
    suhu = float(masukan)
    asal = input("Skala asal (C/F/K): ").upper()
    tujuan = input("Skala tujuan (C/F/K): ").upper()
    try:
        hasil = konversi_suhu(suhu, asal, tujuan)
        print(f"Hasil: {suhu} {asal} = {hasil} {tujuan}")
    except ValueError:
        print("Error: Skala suhu tidak dikenali.")