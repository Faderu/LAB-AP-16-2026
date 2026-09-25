print("=== Setup Denah Bioskop NontonYuk === ")

while True:
    teks_baris = input("Masukkan jumlah baris: ")
    try:
        n_baris = int(teks_baris)
    except ValueError:
        print("Input baris harus berupa angka!")
        continue
    if n_baris <= 0:
        print("Jumlah baris harus lebih dari 0!")
        continue
    break
n_kursi = int(input("Masukkan jumlah kursi per baris: ")) 
print()
print("=== Daftar Kursi Tersedia ===")
for baris in range(1, n_baris + 1):
    for kursi in range(1, n_kursi + 1):
        if kursi == 13:
            continue
        if baris == 1:
            if kursi % 2 == 1:
                print(f"Baris {baris} - kursi {kursi}")
        else:
            print(f"Baris {baris} - Kursi {kursi}")
