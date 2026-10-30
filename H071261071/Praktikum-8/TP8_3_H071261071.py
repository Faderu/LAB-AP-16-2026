import re

print("=== Pembersihan Data Nomor Telepon ===")

jumlah_data = int(input("Masukkan jumlah data: "))

data_asli = []
data_bersih = []
nomor_valid = []

for i in range(jumlah_data):
    nomor = input(f"\nNomor ke-{i + 1}: ")
    data_asli.append(nomor)

    nomor_bersih = re.sub(r"[ -]", "", nomor)
    data_bersih.append(nomor_bersih)

    if re.match(r"^\d{10,13}$", nomor_bersih):
        nomor_valid.append(nomor_bersih)

print("\n--- Hasil Pembersihan ---")

for i in range(jumlah_data):
    if re.match(r"^\d{10,13}$", data_bersih[i]):
        status = "Valid"
    else:
        status = "Tidak valid"

    print(f"\nData {i + 1}:")
    print(f"Sebelum : {data_asli[i]}")
    print(f"Sesudah : {data_bersih[i]}")
    print(f"Status  : {status}")

print(f"\nJumlah nomor valid: {len(nomor_valid)}")