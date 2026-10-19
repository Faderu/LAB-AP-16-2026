alfabet = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    hasil = ""
    for i in teks:
        if i.lower() in alfabet:         
            hasil += i.lower()
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
            potongan = teks[i:j]
            if cek_palinrome(potongan)[0] and len(potongan) > terbaik["panjang"]:
                terbaik = {"teks": potongan, "panjang": len(potongan), "indeks_awal": i}
    return terbaik

teks_bersih = bersihkan_teks(input("Masukkan teks prasasti: "))
print("\nTeks Bersih:", teks_bersih)
print("Output Terharap:", inti_palinrome(teks_bersih))