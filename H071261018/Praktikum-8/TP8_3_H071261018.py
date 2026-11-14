import re

def bersihkan_nomor(nomor):
    return re.sub(r"[\s-]", "", nomor)

def validasi_nomor(nomor):
    pola = r"^\d{10,13}$"
    hasil = re.match(pola, nomor)
    if hasil:
        return True
    else:
        return False

print("=== Pembersihan Data Nomor Telepon ===")
print()
jumlah = int(input("Masukkan jumlah data: "))
print()

data_sebelum = []
data_sesudah = []
nomor_valid = []

for i in range(jumlah):
    nomor = input("Nomor ke-" + str(i + 1) + ": ")
    print()
    bersih = bersihkan_nomor(nomor)
    data_sebelum.append(nomor)
    data_sesudah.append(bersih)
    if validasi_nomor(bersih):
        nomor_valid.append(bersih)

print("--- Hasil Pembersihan ---")
print()
for i in range(jumlah):
    print("Data " + str(i + 1) + ":")
    print("Sebelum :", data_sebelum[i])
    print("Sesudah :", data_sesudah[i])
    if validasi_nomor(data_sesudah[i]):
        print("Status  : Valid")
    else:
        print("Status  : Tidak valid")
    print()
print("Jumlah nomor valid:", len(nomor_valid))