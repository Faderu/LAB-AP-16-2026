try:
    n_kursi = int(input("Masukkan maksimal kursi bus: "))
except ValueError:
    print("Input jumlah kursi harus berupa angka!")
    n_kursi = int(input("Masukkan maksimal kursi bus: "))

print("\n--- Sistem Reservasi PO BUS Dimulai ---\n")

sisa_kursi = n_kursi
total_pendapatan = 0

while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")

    try:
        umur = int(input("Masukkan umur penumpang: "))
    except ValueError:
        print("Input umur harus berupa angka!\n")
        continue

    if umur < 0:
        print("Umur tidak valid!\n")
        continue

    elif umur <= 5:
        kategori = "Balita"
        harga = 0
    elif umur <= 12:
        kategori = "Anak"
        harga = 50000
    else:
        kategori = "Dewasa"
        harga = 100000

    harga_format = f"{harga:,}".replace(",", ".")
    print(f"Kategori: {kategori} - Harga: Rp {harga_format}\n")

    total_pendapatan += harga
    sisa_kursi -= 1

print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan:,}".replace(",", "."))