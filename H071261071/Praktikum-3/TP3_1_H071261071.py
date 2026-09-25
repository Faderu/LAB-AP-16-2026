while True:
    try:
        jumlah_item = int(input("Masukkan jumlah item: "))
    except:
        print("Input harus berupa angka!")
        continue

    if jumlah_item < 0:
        print("Jumlah tidak boleh negatif")

    elif jumlah_item > 100:
        print("Maksimal 100 item per transaksi!")

    elif jumlah_item == 0:
        print("Toko ditutup. Sesi rekap selesai.")
        break

    print(f"Transaksi {jumlah_item} item berhasil!")