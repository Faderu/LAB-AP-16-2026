while True:
    teks_n = input("Masukkan maksimal kursi bus: ")
    try:
        n_kursi = int(teks_n)
    except ValueError:
        print("Input jumlah kursi harus berupa angka!")
        continue
    break
print()
print("=== Sistem Reservasi PO BUS Dimulai ===")

sisa_kursi = n_kursi
total_pendapatan = 0

while sisa_kursi > 0:
    print()
    print(f"Sisa kursi: {sisa_kursi}")
    teks_umur = input("Masukkan umur penumpang")

    try:
        umur = int(teks_umur)
    except ValueError:
        print("Input umur harus berupa angka")
        continue
    if umur <= 5:
        harga = 0
        print("Kategori: Balita - Tiket Gratis (Rp 0)")
    elif umur <= 12:
        harga = 50000
        print("Kategori: Anak - Harga: Rp 50.000 ")
    else:
        harga = 100000
        print("Ktegori: Dewasa - Harga: Rp 100.000")

total_pendapatan += harga
sisa_kursi -= 1

print()
print("=== Semua Kursi Terisi ===")
print(f"Total Pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")
