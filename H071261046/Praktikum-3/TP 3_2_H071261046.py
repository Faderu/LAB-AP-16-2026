print("Setup Denah Bioskop NontonYuk")
while True:
    baris_input = input("Masukkan jumlah baris :")

    try:
        jumlah_baris = int(baris_input)
    except ValueError:
        print("Input baris harus berupa angka!")
        continue

    if jumlah_baris <= 0:
        print("Jumlah baris harus lebih dari 0!")
        continue

    while True:
        kursi_input = input("Masukkan jumlah kursi per baris: ")
        try:
            jumlah_kursi = int(kursi_input)
        except ValueError:
            print("Input kursi harus berupa angka!")
            continue

        if jumlah_kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
        else:
            break
        


    print(" Daftar Kursi Tersedia ")

    for baris in range(1, jumlah_baris + 1):
        if baris == 1:
            # Baris VVIP: hanya nomor ganjil
            for kursi in range(1, jumlah_kursi + 1, 2):
                if kursi == 13:
                    continue
                print(f"Baris {baris} - Kursi {kursi}")
        else:
            # Baris reguler: semua nomor
            for kursi in range(1, jumlah_kursi + 1):
                if kursi == 13:
                    continue
                print(f"Baris {baris} - Kursi {kursi}")
    break

