def hitung_total (harga, barang, member=False):
    total = harga * barang
    if member:
        harga_diskon = harga - (harga*10//100)
        total = harga_diskon * barang
    return total

print ("Selamat datang di Kasir Minimarket!")
status = str(input("Apakah Anda Member? (y/n):"))
if status == "y":
    member = True
elif status == "n":
    member = False
else:
    print ("input tidak valid")
subtotal = 0
while True:
    nama_barang = str(input("Masukkan nama barang (kosongkan untuk selesai):" ))
    if nama_barang == "":
        break
    harga = int(input("Masukkan harga barang: "))
    barang = int(input("Masukkan jumlah barang: "))
    total = hitung_total (harga, barang, member)
    subtotal += total
    print (f"Subtotal {nama_barang}: Rp{total}")
print (f"Total belanja: Rp{subtotal}")

