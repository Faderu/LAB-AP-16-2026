print("Rekapitulasi Transaksi Dins Store")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi.")
 
while True:
    item = input("Masukkan jumlah item: ")
 
    try:
        jumlah = int(item)
    except ValueError:
        print("Input harus berupa angka!")
        continue
 
    if jumlah == 0:
        print("Toko ditutup. Sesi rekap selesai.")
        break
    elif jumlah < 0:
        print("Jumlah tidak boleh negatif")
        continue
    elif jumlah > 100:
        print("Maksimal 100 item per transaksi!")
        continue
    else:
        print(f"Transaksi {jumlah} item berhasil!")