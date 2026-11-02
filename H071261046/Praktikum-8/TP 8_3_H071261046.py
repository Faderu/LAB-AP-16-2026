import re

def bersihkan_nomor(nomor):
    return re.sub(r"[\s-]", "", nomor)

def cek_nomor_valid(nomor_bersih):
    return re.fullmatch(r"[\d]{10,13}", nomor_bersih) is not None

print("=== Pembersihan Data Nomor Telepon ===")
print()

while True:
    try:
        jumlah = int(input("Masukkan jumlah data: "))
    except ValueError:
        print("Jumlah harus berupa angka bulat!")
        continue
    if jumlah <= 0:
        print("Jumlah harus lebih dari 0!")
        continue
    break

data_sebelum = []
data_sesudah = []
nomor_valid = []
for i in range(jumlah):
    print()
    nomor = input(f"Nomor ke-{i + 1}: ")
    nomor_bersih = bersihkan_nomor(nomor)
    data_sebelum.append(nomor)
    data_sesudah.append(nomor_bersih)
    if cek_nomor_valid(nomor_bersih):
        nomor_valid.append(nomor_bersih)

print()
print("--- Hasil Pembersihan ---")
for i in range(jumlah):
    print()
    print(f"Data {i + 1}:")
    print(f"Sebelum : {data_sebelum[i]}")
    print(f"Sesudah : {data_sesudah[i]}")
    if cek_nomor_valid(data_sesudah[i]):
        print("Status  : Valid")
    else:
        print("Status  : Tidak valid")

print()
print(f"Jumlah nomor valid: {len(nomor_valid)}")