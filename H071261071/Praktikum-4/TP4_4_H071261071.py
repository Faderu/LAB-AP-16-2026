def konversi_suhu(suhu, asal, tujuan):
    skala_valid = {"C", "F", "K"}

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
        hasil = (celsius * 9 / 5) + 32
    else:
        hasil = celsius + 273.15

    return hasil


print("=== Konversi Suhu ===")

while True:
    masukan_suhu = input(
        "Masukkan suhu (atau 'selesai' untuk keluar): "
    ).strip()

    if masukan_suhu.lower() == "selesai":
        break

    try:
        suhu = float(masukan_suhu)
        asal = input("Skala asal (C/F/K): ").strip().upper()
        tujuan = input("Skala tujuan (C/F/K): ").strip().upper()

        hasil = konversi_suhu(suhu, asal, tujuan)

        print(f"Hasil: {suhu} {asal} = {hasil} {tujuan}")

    except ValueError as e:
        print(e)