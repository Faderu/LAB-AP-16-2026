def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah

    if adalah_member:
        subtotal = subtotal * 0.90

    return subtotal


print("Selamat datang di Kasir Minimarket!")

jawaban_member = input("Apakah Anda member? (y/n): ").strip().lower()
adalah_member = jawaban_member == "y"

total_belanja = 0

while True:
    nama_barang = input(
        "Masukkan nama barang (kosongkan untuk selesai): "
    ).strip()

    if nama_barang == "":
        break

    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    subtotal = hitung_subtotal(harga, jumlah, adalah_member)

    print(f"Subtotal {nama_barang}: Rp{subtotal:.0f}")
    total_belanja += subtotal

print(f"Total belanja: Rp{total_belanja:.0f}")