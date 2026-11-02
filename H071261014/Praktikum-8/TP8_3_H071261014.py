import re

def bersihkan_nomor(nomor):
    return re.sub(r"[ -]", "", nomor)


def validasi_telepon(nomor):
    return re.fullmatch(r"[0-9]{10,13}", nomor) is not None


def main():
    print("=== Pembersihan Data Nomor Telepon ===\n")

    jumlah = int(input("Masukkan jumlah data: "))

    data_sebelum = []
    data_sesudah = []
    nomor_valid = []

    for i in range(1, jumlah + 1):
        print()
        nomor = input(f"Nomor ke-{i}: ")
        data_sebelum.append(nomor)
        data_sesudah.append(bersihkan_nomor(nomor))

    print("\n--- Hasil Pembersihan ---")

    for i in range(jumlah):
        sebelum = data_sebelum[i]
        sesudah = data_sesudah[i]

        print(f"\nData {i + 1}:")
        print(f"Sebelum : {sebelum}")
        print(f"Sesudah : {sesudah}")

        if validasi_telepon(sesudah):
            print("Status  : Valid")
            nomor_valid.append(sesudah)
        else:
            print("Status  : Tidak valid")

    print(f"\nJumlah nomor valid: {len(nomor_valid)}")


main()