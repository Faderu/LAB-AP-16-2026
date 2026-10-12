ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    hasil = ""
    for ch in teks:
        kecil = ch.lower()
        if len(kecil) == 1 and kecil in ALFABET:
            hasil += kecil
    return hasil


def cek_palinrome(teks):
    terbalik = "".join(reversed(teks))
    for i in range(len(teks)):
        if teks[i] != terbalik[i]:
            return (False, i)
    return (True, -1)


def inti_palinrome(teks):
    terbaik = {"teks": "", "panjang": 0, "indeks_awal": -1}
    for i in range(len(teks)):
        for j in range(i + 1, len(teks) + 1):
            sub = teks[i:j]
            simetris, _ = cek_palinrome(sub)
            
            if simetris and len(sub) > terbaik["panjang"]:
                terbaik = {"teks": sub, "panjang": len(sub), "indeks_awal": i}

    return terbaik

masukan = input("Masukkan teks prasasti: ")
bersih = bersihkan_teks(masukan)
hasil = inti_palinrome(bersih)

print()
print("Teks Bersih:", bersih)
print("Output Terharap:", hasil)