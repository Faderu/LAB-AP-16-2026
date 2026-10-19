def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    genre = genre.capitalize()

    # Satu lagu disimpan sebagai tuple.
    lagu = (judul, artis, genre, durasi)

    playlist.append(lagu)
    genre_set.add(genre)

    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def format_durasi(durasi_detik):
    menit = durasi_detik // 60
    detik = durasi_detik % 60

    return f"{menit}:{detik:02d}"


def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist masih kosong.")
        print("Total durasi playlist: 0 menit 0 detik")
        return

    print("=" * 75)
    print(f"{'No':<5}{'Judul':<30}{'Artis':<20}{'Genre':<12}{'Durasi'}")
    print("=" * 75)

    total_durasi = 0

    for nomor, lagu in enumerate(playlist, start=1):
        judul, artis, genre, durasi = lagu
        total_durasi += durasi

        print(
            f"{nomor:<5}{judul:<30}{artis:<20}{genre:<12}"
            f"{format_durasi(durasi)}"
        )

    total_menit = total_durasi // 60
    sisa_detik = total_durasi % 60

    print("=" * 75)
    print(
        f"Total durasi playlist: "
        f"{total_menit} menit {sisa_detik} detik"
    )


def filter_genre(playlist, genre_target):
    return [
        lagu
        for lagu in playlist
        if lagu[2].lower() == genre_target.lower()
    ]


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak valid.")
        return False

    lagu_dihapus = playlist.pop(nomor - 1)
    print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus!")
    return True


def statistik_playlist(playlist, genre_set):
    print("=" * 40)
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)
    print(f"Total lagu   : {len(playlist)}")

    if not playlist:
        print("Jumlah genre : 0")
        print("Playlist belum memiliki lagu.")
        print("=" * 40)
        return

    # Perbarui set genre agar sesuai dengan lagu yang masih ada.
    genre_set.clear()
    for lagu in playlist:
        genre_set.add(lagu[2])

    print(f"Jumlah genre : {len(genre_set)}")
    print("Daftar genre :", genre_set)

    # Dictionary untuk menyimpan jumlah lagu pada setiap genre.
    distribusi = {}

    for genre in genre_set:
        distribusi[genre] = 0

    for lagu in playlist:
        genre = lagu[2]
        distribusi[genre] += 1

    print("Distribusi genre:")
    for genre, jumlah in distribusi.items():
        print(f"{genre}: {'#' * jumlah} ({jumlah})")

    lagu_terpanjang = max(playlist, key=lambda lagu: lagu[3])
    lagu_terpendek = min(playlist, key=lambda lagu: lagu[3])

    print(
        f"Lagu terpanjang: {lagu_terpanjang[0]} "
        f"({format_durasi(lagu_terpanjang[3])})"
    )
    print(
        f"Lagu terpendek : {lagu_terpendek[0]} "
        f"({format_durasi(lagu_terpendek[3])})"
    )
    print("=" * 40)


playlist = []
genre_set = set()

print("=" * 40)
print("PLAYLIST MUSIK - PLAYTUNE")
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

        while True:
            try:
                durasi = int(input("Durasi (dalam detik): "))

                if durasi <= 0:
                    print("Durasi harus lebih dari 0.")
                    continue

                break

            except ValueError:
                print("Durasi harus berupa angka bulat.")

        tambah_lagu(
            playlist,
            genre_set,
            judul,
            artis,
            genre,
            durasi
        )

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        print("Genre tersedia:", genre_set)
        genre_target = input("Masukkan genre yang ingin difilter: ")
        hasil_filter = filter_genre(playlist, genre_target)

        if hasil_filter:
            print(f"Lagu bergenre '{genre_target}':")

            for nomor, lagu in enumerate(hasil_filter, start=1):
                judul, artis, genre, durasi = lagu
                print(
                    f"{nomor}. {judul} - {artis} "
                    f"({format_durasi(durasi)})"
                )
        else:
            print("Tidak ada lagu untuk genre tersebut.")

    elif pilihan == "4":
        tampilkan_playlist(playlist)

        if playlist:
            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))

                if hapus_lagu(playlist, nomor):
                    # Susun ulang set genre setelah lagu dihapus.
                    genre_set.clear()
                    for lagu in playlist:
                        genre_set.add(lagu[2])

            except ValueError:
                print("Nomor lagu harus berupa angka.")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid. Masukkan angka 1 sampai 6.")