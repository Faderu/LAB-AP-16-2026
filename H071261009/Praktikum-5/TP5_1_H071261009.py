ALFABET = "abcdefghijklmnopqrstuvwxyz"


def bersihkan_teks(teks):
    hasil = ""
    for ch in teks:
        huruf = ch.lower()
        if ALFABET.find(huruf) != -1:
            hasil = hasil + huruf
    return hasil


def cek_palinrome(teks):
    terbalik = "".join(reversed(teks))
    if teks == terbalik:
        return (True, -1)
    for i in range(len(teks)):
        if teks[i] != terbalik[i]:
            return (False, i)


def inti_palinrome(teks):
    bersih = bersihkan_teks(teks)
    n = len(bersih)
    terbaik = {"teks": "", "panjang": 0, "indeks_awal": -1}

    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = bersih[i:j]
            if len(sub) > terbaik["panjang"]:
                if cek_palinrome(sub)[0]:
                    terbaik = {"teks": sub, "panjang": len(sub), "indeks_awal": i}
    return terbaik


teks = input("Masukkan teks prasasti: ")
print()
print(f"Teks Bersih: {bersihkan_teks(teks)}")
print(f"Output Terharap: {inti_palinrome(teks)}")