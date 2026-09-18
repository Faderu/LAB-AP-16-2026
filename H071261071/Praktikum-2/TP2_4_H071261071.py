tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ").title()
waktu = input("Masukkan waktu (Pagi/Malam): ").title()
tipe_pengunjung = input("Masukkan tipe pengunjung (Anak/Dewasa): ").title()

match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            print("Paket Rekomendasi: Paket A")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case "Pegunungan":
        if waktu == "Pagi" and tipe_pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket B")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case "Kota":
        if waktu == "Malam":
            print("Paket Rekomendasi: Paket C")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa" and tipe_pengunjung == "Anak":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case _:
        print("Tujuan wisata tidak valid")