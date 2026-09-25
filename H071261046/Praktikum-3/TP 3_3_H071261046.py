while True:
    kursi_input = input("Masukkan maksimal kursi bus: ")
    try:
        sisa_kursi = int(kursi_input)
    except ValueError:
        print("Input jumlah kursi harus berupa angka!")
        continue

    if sisa_kursi <= 0:
        print("Jumlah kursi harus lebih dari 0!")
        continue
    break

print("Sistem Reservasi PO BUS Dimulai")

total_pendapatan = 0

while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")
    umur_input = input("Masukkan umur penumpang: ")

    try:
        umur = int(umur_input)
    except ValueError:
        print("Input umur harus berupa angka!")
        continue

    if umur < 0:
        print("Umur tidak valid!")
        continue

    elif 0 <= umur <= 5:
        harga = 0
        print(f"Kategori: Balita - Tiket Gratis (Rp {harga})")
    elif 6 <= umur <= 12:
        harga = 50000
        print(f"Kategori: Anak - Harga: Rp {harga:,}".replace(",", "."))
    else:
        harga = 100000
        print(f"Kategori: Dewasa - Harga: Rp {harga:,}".replace(",", "."))

    total_pendapatan += harga
    sisa_kursi -= 1

print("Semua Kursi Terisi")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")
