#program 4
tujuan = (input("Masukkan tujuan (Pantai/Pegunungan/Kota): ")).capitalize(
)
waktu =  (input("Masukkan waktu (Pagi/Malam): ")).capitalize()
tipe_pengunjung =  (input("Masukkan tipe pengunjung (Anak/Dewasa): ")).capitalize()
paket = "Tidak ada paket yang cocok"
match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            paket = "Paket A"
    case "Pegunungan":
        if waktu == "Pagi" and tipe_pengunjung == "Dewasa":
            paket = "Paket B"
    case "Kota":
        if waktu == "Malam":
            paket = "Paket C"
    case _:
        print (paket)
if waktu == "Malam" and tipe_pengunjung == "Dewasa":
    paket = "Paket C"
print ("Paket Rekomendasi:", paket)