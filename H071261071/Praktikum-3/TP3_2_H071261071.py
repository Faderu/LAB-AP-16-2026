print("=== Setup denah Bioskop NontonYuk ===")
while True:
    try:
        jumlah_baris = int(input("Masukkan jumlah baris: "))

        if jumlah_baris <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue

        break
    except ValueError:
        print("Input baris harus berupa angka!")

while True:
    try:
        jumlah_kursi = int(input("Masukkan jumlah kursi per baris: "))

        if jumlah_kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue

        break
    except ValueError:
        print("Input kursi harus berupa angka!")

print("\n=== Daftar Kursi Tersedia ===")

for baris in range(1, jumlah_baris + 1):
    for kursi in range(1, jumlah_kursi + 1): 

        # Kursi 13 selalu dilewati di semua baris
        if kursi == 13:
            continue

        # Baris 1 hanya menampilkan kursi ganjil
        if baris == 1 and kursi % 2 == 0:
            continue

        print(f"Baris {baris} - Kursi {kursi}")