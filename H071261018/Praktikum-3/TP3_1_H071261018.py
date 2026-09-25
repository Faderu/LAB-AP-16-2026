print("=== Rekapitulasi Transaksi Dins Store ===")
print("Ketik '0' untuk menutup toko da mengakhiri sesi. ")

while True:
    print()
    teks_input = input("Masukkan jumlah item: ")

    try: 
        jumlah = int(teks_input)
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
