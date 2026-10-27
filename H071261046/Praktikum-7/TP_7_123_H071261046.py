import os
import random
from datetime import datetime
 
FOLDER = "invoices"
FILE_HISTORY = "trx_history.txt"

# SOAL 1: Membuat invoice
 
def buat_folder():
    try:
        os.mkdir(FOLDER)
    except IOError:
        pass  
 
 
def ambil_inisial(nama):
    inisial = ""
    for kata in nama.split():
        inisial = inisial + kata[0].upper()
    return inisial
 
 
def buat_id_transaksi(nama_kasir, waktu):
    inisial = ambil_inisial(nama_kasir)
    tanggal_waktu = waktu.strftime("%y%m%d%H%M")  
    acak = random.randint(100, 999)
    return inisial + tanggal_waktu + str(acak)
 
 
def input_angka(pesan):
    while True:
        try:
            angka = int(input(pesan))
            if angka > 0:
                return angka
            print("Angka harus lebih dari 0!")
        except ValueError:
            print("Input harus berupa angka!")
 
 
def simpan_invoice(id_trx, nama_kasir, waktu, daftar_belanja, total):
    filename = FOLDER + "/" + id_trx + ".txt"
    try:
        with open(filename, 'w') as f:
            f.write("=" * 50 + "\n")
            f.write("INVOICE BELANJA\n")
            f.write("=" * 50 + "\n")
            f.write("ID Transaksi : " + id_trx + "\n")
            f.write("Kasir        : " + nama_kasir + "\n")
            f.write("Waktu        : " + waktu.strftime("%Y-%m-%d %H:%M:%S") + "\n")
            f.write("-" * 50 + "\n")
            f.write("Produk | Harga x Jumlah = Subtotal\n")
            f.write("-" * 50 + "\n")
            for item in daftar_belanja:
                nama = item[0]
                harga = item[1]
                jumlah = item[2]
                subtotal = harga * jumlah
                f.write(nama + " | " + str(harga) + " x " + str(jumlah)
                        + " = " + str(subtotal) + "\n")
            f.write("-" * 50 + "\n")
            f.write("TOTAL : Rp. " + str(total) + "\n")
            f.write("=" * 50 + "\n")
            f.write("Terima kasih sudah berbelanja!\n")
        print("File " + filename + " created successfully.")
        return True
    except IOError:
        print("Error: could not create file " + filename)
        return False
 
 
def transaksi_baru():
    print("\n--- TRANSAKSI BARU ---")
    nama_kasir = input("Nama kasir: ").strip()
    if nama_kasir == "":
        print("Nama kasir tidak boleh kosong!")
        return
 
    daftar_belanja = [] 
    total = 0
 
    while True:
        nama_produk = input("Nama produk: ").strip()
        harga = input_angka("Harga produk: ")
        jumlah = input_angka("Jumlah dibeli: ")
 
        daftar_belanja.append([nama_produk, harga, jumlah])
        total = total + harga * jumlah
 
        lagi = input("Tambah produk lain? (y/n): ").lower()
        if lagi != "y":
            break
 
    waktu = datetime.now()
    id_trx = buat_id_transaksi(nama_kasir, waktu)
 
    berhasil = simpan_invoice(id_trx, nama_kasir, waktu, daftar_belanja, total)
    if berhasil:
        catat_riwayat(waktu, id_trx, total)  
        print("\nTransaksi berhasil!")
        print("ID Transaksi : " + id_trx)
        print("Total        : Rp. " + str(total))
 
# SOAL 2: Mencari dan menampilkan invoice
 
def cari_invoice():
    print("\n--- CARI INVOICE ---")
    id_trx = input("Masukkan ID transaksi: ").strip().upper()
    filename = FOLDER + "/" + id_trx + ".txt"
    try:
        with open(filename, 'r') as f:
            contents = f.read()
        print()
        print(contents)
    except IOError:
        print("Error: could not read file " + filename)

 
# SOAL 3: Mencatat riwayat transaksi
 
def siapkan_file_riwayat():
    garis = "=" * 60
    try:
        with open(FILE_HISTORY, 'x') as f:
            f.write(garis + "\n")
            f.write("| Waktu | ID Transaksi | Nominal Transaksi |\n")
            f.write(garis + "\n")
    except IOError:
        pass 
 
 
def catat_riwayat(waktu, id_trx, total):
    garis = "=" * 60
    try:
        with open(FILE_HISTORY, 'a') as f:
            f.write("| " + waktu.strftime("%Y-%m-%d %H:%M:%S")
                    + " | " + id_trx
                    + " | Rp. " + str(total) + " |\n")
            f.write(garis + "\n")
    except IOError:
        print("Error: could not append to file " + FILE_HISTORY)
 

# PROGRAM UTAMA
 
if __name__ == '__main__':
    buat_folder()
    siapkan_file_riwayat()
 
    while True:
        print("\n===== APLIKASI KASIR =====")
        print("1. Transaksi baru")
        print("2. Cari invoice")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
 
        if pilihan == "1":
            transaksi_baru()
        elif pilihan == "2":
            cari_invoice()
        elif pilihan == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")