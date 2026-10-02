def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal *=  0.9
    return subtotal
print("Selamat datang di kasir Minimarket!")
status = input("Apakah Anda member? (y/n): ")
adalah_member = status.lower() == "y"

total_belanja = 0
while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if nama_barang == "":
        break
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    subtotal = hitung_subtotal(harga, jumlah, adalah_member)
    print(f"Subtotal {nama_barang}: Rp{subtotal:.0f}")

    total_belanja += subtotal
print(f"Total belanja: Rp{total_belanja:.0f}")






