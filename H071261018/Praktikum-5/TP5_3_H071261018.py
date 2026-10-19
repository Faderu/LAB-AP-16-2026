ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_sandi(ch, k):
    posisi = ALFABET.find(ch.lower())
    if posisi == -1:
        return ch
    huruf_baru = ALFABET[(posisi + k) % 26]
    if ch == ch.upper():
        return huruf_baru.upper()
    return huruf_baru.lower()


def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil = hasil + cek_sandi(ch, k)
    return hasil


def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)


def retas_sandi(sandi, kata_kunci):
    hasil_valid = []
    for k in range(26):
        pesan = mesin_dekripsi(sandi, k)
        if pesan.lower().find(kata_kunci.lower()) != -1:
            hasil_valid.append((k, pesan))
    return hasil_valid


sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukkan kata kunci target: ")

print()
print("Output Deskripsi:", retas_sandi(sandi, kata_kunci))