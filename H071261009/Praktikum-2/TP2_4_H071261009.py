tujuan = str(input("Masukkan tujuan (Pantai/Pengunungan/Kota): ")).capitalize()
waktu = str(input("Masukkan waktu (Pagi/Malam): ")).capitalize()
tipe_pengunjung = str(input("Masukkan tipe pengunjung (Anak/Dewasa):")).capitalize()

match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            paket = "A"
        elif waktu == "Malam" and tipe_pengunjung =="Dewasa":
            paket = "Paket C"
        else: 
            paket = "Tidak ada paket yang cocok"
    case "Pengunungan":
        if waktu == "Pagi" and tipe_pengunjung == "Dewasa" :
            paket = "Paket B"
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa" :
            paket = "Paket C"
        else:
            paket = "Tidak ada paket yang cocok"
    case "Kota":
        if waktu == "Malam":
            paket = "Paket C"
        else:
            paket = "Tidak ada Paket yang cocok"
    case _ :
        paket = "tidak ada pake yang cocok"

print("Paket Rekomendasi:", paket)

        