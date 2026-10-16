def format_durasi(detik):
    menit = detik // 60
    sisa = detik % 60
    return f"{menit}:{sisa:02d}"


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    genre = genre.capitalize()
    lagu = (judul, artis, genre, durasi)

    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    print("=" * 57)
    print(f"{'No':<4}{'Judul':<22}{'Artis':<16}{'Genre':<9}{'Durasi'}")
    print("=" * 57)

    total_detik = 0

    for i, lagu in enumerate(playlist, start=1):
        judul, artis, genre, durasi = lagu
        print(f"{i:<4}{judul:<22}{artis:<16}{genre:<9}{format_durasi(durasi)}")
        total_detik += durasi

    print("=" * 57)
    print(f"Total durasi playlist: {total_detik // 60} menit {total_detik % 60} detik")


def filter_genre(playlist, genre_target):
    hasil = [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]
    return hasil


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak valid.")
    else:
        lagu = playlist.pop(nomor - 1)
        print(f"Lagu '{lagu[0]}' berhasil dihapus!")


def statistik_playlist(playlist, genre_set):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    distribusi = {}

    for lagu in playlist:
        genre = lagu[2]
        if genre in distribusi:
            distribusi[genre] += 1
        else:
            distribusi[genre] = 1

    terpanjang = playlist[0]
    terpendek = playlist[0]

    for lagu in playlist:
        if lagu[3] > terpanjang[3]:
            terpanjang = lagu
        if lagu[3] < terpendek[3]:
            terpendek = lagu

    print("=" * 40)
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)
    print(f" Total lagu      : {len(playlist)}")
    print(f" Jumlah genre    : {len(genre_set)}")
    print(f" Daftar genre    : {genre_set}")
    print(" Distribusi genre:")

    for genre in distribusi:
        print(f"   {genre:<8}: {'#' * distribusi[genre]} ({distribusi[genre]})")

    print(f" Lagu terpanjang : {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f" Lagu terpendek  : {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("=" * 40)


playlist = []
genre_set = set()

print("=" * 40)
print(" PLAYLIST MUSIK - PLAYTUNE")
print("=" * 40)

while True:
    print("\nMenu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        judul = input("Judul lagu: ")
        artis = input("Artis: ")
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")

        try:
            durasi = int(input("Durasi (dalam detik): "))

            if durasi <= 0:
                print("Durasi harus berupa angka positif.")
            else:
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)

        except ValueError:
            print("Error! Durasi harus berupa angka bulat.")

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        if len(playlist) == 0:
            print("Playlist masih kosong.")
        else:
            print(f"Genre tersedia: {genre_set}")
            genre_target = input("Masukkan genre yang ingin difilter: ")

            hasil = filter_genre(playlist, genre_target)

            if len(hasil) == 0:
                print(f"Tidak ada lagu bergenre '{genre_target}'.")
            else:
                print(f"Lagu bergenre '{genre_target}':")
                for i, lagu in enumerate(hasil, start=1):
                    print(f" {i}. {lagu[0]} - {lagu[1]} ({format_durasi(lagu[3])})")

    elif pilihan == "4":
        if len(playlist) == 0:
            print("Playlist masih kosong.")
        else:
            tampilkan_playlist(playlist)

            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))
                hapus_lagu(playlist, nomor)

                genre_set.clear()
                for lagu in playlist:
                    genre_set.add(lagu[2])

            except ValueError:
                print("Error! Nomor lagu harus berupa angka bulat.")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-6.")