ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_kata(teks, kata):
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    hasil = []

    if kata_kecil == "":
        return hasil

    start = 0
    while True:
        pos = teks_kecil.find(kata_kecil, start)
        if pos == -1:
            break
        hasil.append(pos)
        start = pos + 1
    return hasil

def cek_batas_kata(teks, i, panjang):
    
    if i > 0 and teks[i - 1].lower() in ALFABET:
        return False

    akhir = i + panjang
    if akhir < len(teks) and teks[akhir].lower() in ALFABET:
        return False

    return True

def sensor_kata(teks, kata, simbol):
    panjang = len(kata)
    semua_indeks = cek_kata(teks, kata)

    hasil = ""
    indeks_tersensor = []
    terakhir = 0  

    for i in semua_indeks:
        
        if i < terakhir:
            continue
        if cek_batas_kata(teks, i, panjang):
            hasil = hasil + teks[terakhir:i] + simbol * panjang
            terakhir = i + panjang
            indeks_tersensor.append(i)

    hasil = hasil + teks[terakhir:]
    return (hasil, len(indeks_tersensor), indeks_tersensor)

teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

teks_tersensor, jumlah, indeks = sensor_kata(teks, kata, simbol)

print("Hasil Teks:", teks_tersensor)
print("Jumlah:", jumlah, "| Indeks:", indeks)