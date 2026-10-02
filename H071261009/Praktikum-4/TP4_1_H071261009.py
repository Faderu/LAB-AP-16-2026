def hitung_subtotal(harga: int, jumlah: int, status_member: bool = False) -> int:
    subtotal = harga * jumlah
    if status_member:
        subtotal = subtotal * 0.9
    return subtotal
 
print("Selamat datang di Kasir Minimarket!")
status = input("Apakah Anda member? (y/n): ").strip().lower()
member = status == "y" 
 
total = 0
while True:
    nama = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if nama == "":
        break
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))
    subtotal = hitung_subtotal(harga, jumlah, member)
    print(f"Subtotal {nama}: Rp{subtotal}")
    total += subtotal
 
print(f"Total belanja: Rp{total}")