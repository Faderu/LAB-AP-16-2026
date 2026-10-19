ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_kata(teks, kata):
    hasil = []
    pos = teks.lower().find(kata.lower())
    while pos != -1:
        hasil.append(pos)
        pos = teks.lower().find(kata.lower(), pos + 1)   
    return hasil

def cek_batas_kata(teks, i, panjang):
    if i > 0 and teks[i - 1].lower() in ALFABET:                       
        return False
    if i + panjang < len(teks) and teks[i + panjang].lower() in ALFABET:  
        return False
    return True

def sensor_kata(teks, kata, simbol):
    hasil = ""
    posisi = 0
    indeks = []
    for i in cek_kata(teks, kata):
        if cek_batas_kata(teks, i, len(kata)):
            hasil += teks[posisi:i] + simbol * len(kata)
            posisi = i + len(kata)
            indeks.append(i)
    hasil += teks[posisi:]                
    return (hasil, len(indeks), indeks)

teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")
hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
print("Hasil Teks:", hasil)
print("Jumlah:", jumlah, "| Indeks:", indeks)