ALFABET = "abcdefghijklmnopqrstuvwxyz"


def bersihkan_teks(teks):
    hasil = ""
    for ch in teks:
        if ch.lower() in ALFABET:
            hasil = hasil + ch
    return hasil.lower()


def cek_palinrome(teks):
    terbalik = ''.join(reversed(teks))
    if teks == terbalik:
        return (True, -1)
    for i in range(len(teks)):
        if teks[i] != terbalik[i]:
            return (False, i)


def inti_palinrome(teks):
    terbaik = {"teks": "", "panjang": 0, "indeks_awal": 0}
    n = len(teks)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = teks[i:j]
            simetris, indeks_beda = cek_palinrome(sub)
            if simetris and len(sub) > terbaik["panjang"]:
                terbaik = {"teks": sub, "panjang": len(sub), "indeks_awal": i}
    return terbaik


teks_asli = input("Masukkan teks prasasti: ")
bersih = bersihkan_teks(teks_asli)

print()
print("Teks Bersih:", bersih)
print("Output Terharap:", inti_palinrome(bersih))