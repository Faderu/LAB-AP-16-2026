print("--- Setup Denah Bioskop NontonYuk ---")

while True:
    baris_input = input("Masukkan jumlah baris: ")
    try:
        n_baris = int(baris_input)
    except ValueError:
        print("Input baris harus berupa angka!\n")
        continue

    if n_baris <= 0:
        print("Jumlah baris harus lebih dari 0!\n")
        continue
    else:
        break

m_kursi = int(input("Masukkan jumlah kursi per baris: "))

print("\n--- Daftar Kursi Tersedia ---")

for baris in range(1, n_baris + 1):
    for kursi in range(1, m_kursi + 1):
        if kursi == 13:
            continue
        if baris == 1 and kursi % 2 == 0:
            continue

        print(f"Baris {baris} - Kursi {kursi}")