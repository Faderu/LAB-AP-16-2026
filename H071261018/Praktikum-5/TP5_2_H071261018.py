ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_kata(teks, kata):
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    daftar_indeks = []
    i = teks_kecil.find(kata_kecil, 0)
    while i != -1:
        daftar_indeks.append(i)
        i = teks_kecil.find(kata_kecil, i + 1)
    return daftar_indeks


def cek_batas_kata(teks, i, panjang):
    if i > 0 and ALFABET.find(teks[i - 1].lower()) != -1:
        return False
    akhir = i + panjang
    if akhir < len(teks) and ALFABET.find(teks[akhir].lower()) != -1:
        return False
    return True


def sensor_kata(teks, kata, simbol):
    panjang = len(kata)
    hasil = ""
    posisi = 0
    list_indeks_awal = [0]
    for i in cek_kata(teks, kata):
        if cek_batas_kata(teks, i, panjang) and i >= posisi:
            hasil = hasil + teks[posisi:i] + simbol * panjang
            posisi = i + panjang
            list_indeks_awal.append(i)
    hasil = hasil + teks[posisi:]
    return (hasil, len(list_indeks_awal), list_indeks_awal)


teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

teks_tersensor, jumlah, indeks = sensor_kata(teks, kata, simbol)
print("Hasil Teks:", teks_tersensor)
print("Jumlah:", jumlah, "| Indeks:", indeks)