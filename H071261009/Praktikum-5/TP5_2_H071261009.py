ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_kata(teks, kata):
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    daftar = []
    start = 0
    while True:
        i = teks_kecil.find(kata_kecil, start)
        if i == -1:
            break
        daftar.append(i)
        start = i + 1
    return daftar


def cek_batas_kata(teks, i, panjang):
    if i == 0:
        sebelum_ok = True
    else:
        sebelum_ok = ALFABET.find(teks[i - 1].lower()) == -1

    akhir = i + panjang
    if akhir >= len(teks):
        sesudah_ok = True
    else:
        sesudah_ok = ALFABET.find(teks[akhir].lower()) == -1

    return sebelum_ok and sesudah_ok


def sensor_kata(teks, kata, simbol):
    panjang = len(kata)
    hasil = ""
    posisi = 0
    daftar_indeks = []

    for i in cek_kata(teks, kata):
        if cek_batas_kata(teks, i, panjang):
            hasil = hasil + teks[posisi:i] + simbol * panjang
            posisi = i + panjang
            daftar_indeks.append(i)

    hasil = hasil + teks[posisi:]
    return (hasil, len(daftar_indeks), daftar_indeks)


teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")[:1]

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
print(f"Hasil Teks: {hasil}")
print(f"Jumlah: {jumlah} | Indeks: {indeks}")