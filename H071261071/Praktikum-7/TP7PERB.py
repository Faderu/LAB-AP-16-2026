from datetime import datetime
from pathlib import Path
import random

FOLDER_INVOICE = Path("invoices")
FILE_RIWAYAT = Path("trx_history.txt")
NAMA_TOKO = "TOKO AQIL"
NAMA_KASIR = "Aqil"


def buat_id_transaksi(waktu):
    inisial = "".join(kata[0] for kata in NAMA_KASIR.split()).upper()
    bagian_waktu = waktu.strftime("%y%m%d%H%M")

    while True:
        angka_acak = random.randint(100, 999)
        id_transaksi = f"{inisial}{bagian_waktu}{angka_acak}"
        file_invoice = FOLDER_INVOICE / f"{id_transaksi}.txt"

        if not file_invoice.exists():
            return id_transaksi


def format_rupiah(nominal):
    return f"Rp{nominal:,}".replace(",", "")


# Membuat transaksi dan invoice
def transaksi_baru():
    waktu = datetime.now()
    daftar_produk = []
    total = 0

    while True:
        nama_produk = input("Masukkan nama produk  : ").strip()

        try:
            harga = int(input("Masukkan harga produk : "))
            jumlah = int(input("Masukkan jumlah produk: "))
        except ValueError:
            print("Harga dan jumlah harus berupa angka.")
            continue

        subtotal = harga * jumlah
        total += subtotal

        daftar_produk.append({
            "nama": nama_produk,
            "harga": harga,
            "jumlah": jumlah,
            "subtotal": subtotal,
        })

        tambah_produk = input("Tambah produk? (y/t) : ").strip().lower()
        print("-" * 70)

        if tambah_produk != "y":
            break

    id_transaksi = buat_id_transaksi(waktu)
    FOLDER_INVOICE.mkdir(exist_ok=True)

    isi_invoice = [
        NAMA_TOKO.center(70),
        "",
        "=" * 70,
        f"Nama kasir       : {NAMA_KASIR}",
        f"Waktu transaksi  : {waktu.strftime('%d/%m/%y %H:%M')}",
        "=" * 70,
        "",
        "Daftar Produk".center(70),
        "",
        "-" * 70,
        f"| {'Nama':20} | {'Harga':12} | {'Jumlah':8} | {'Total':12} |",
        "-" * 70,
    ]

    for produk in daftar_produk:
        isi_invoice.append(
            f"| {produk['nama'][:20]:20} "
            f"| {format_rupiah(produk['harga']):12} "
            f"| {produk['jumlah']:8} "
            f"| {format_rupiah(produk['subtotal']):12} |"
        )

    isi_invoice.extend([
        "-" * 70,
        f"| {'TOTAL':45} | {format_rupiah(total):12} |",
        "-" * 70,
        "",
        "=" * 70,
        "TERIMA KASIH TELAH BERBELANJA".center(70),
        "=" * 70,
    ])

    file_invoice = FOLDER_INVOICE / f"{id_transaksi}.txt"
    file_invoice.write_text("\n".join(isi_invoice), encoding="utf-8")

    catat_riwayat(waktu, id_transaksi, total)

    print("TRANSAKSI BERHASIL")
    print(f"ID transaksi: {id_transaksi}")


# Mencari dan menampilkan invoice
def cari_transaksi():
    id_transaksi = input("Masukkan ID transaksi : ").strip()
    file_invoice = FOLDER_INVOICE / f"{id_transaksi}.txt"

    if file_invoice.exists():
        print()
        print(file_invoice.read_text(encoding="utf-8"))
    else:
        print("Invoice tidak ditemukan.")


# Mencatat transaksi ke file riwayat
def catat_riwayat(waktu, id_transaksi, nominal):
    file_baru = not FILE_RIWAYAT.exists()

    with FILE_RIWAYAT.open("a", encoding="utf-8") as file:
        if file_baru:
            file.write("+" + "-" * 75 + "+\n")
            file.write("|" + "RIWAYAT TRANSAKSI".center(75) + "|\n")
            file.write("+" + "-" * 75 + "+\n")
            file.write(
                f"| {'Waktu':19} | {'ID Transaksi':18} | "
                f"{'Nominal Transaksi':25} |\n"
            )
            file.write("+" + "-" * 75 + "+\n")

        waktu_teks = waktu.strftime("%d/%m/%y %H:%M")
        file.write(
            f"| {waktu_teks:19} | {id_transaksi:18} | "
            f"{format_rupiah(nominal):25} |\n"
        )
        file.write("+" + "-" * 75 + "+\n")


def main():
    print("=" * 70)
    print("SELAMAT DATANG".center(70))
    print("=" * 70)
    print(f"Masukkan nama kasir : {NAMA_KASIR}")
    print("=" * 70)

    while True:
        print("\nPilih opsi:")
        print("1. Transaksi baru")
        print("2. Cari transaksi")
        print("3. Keluar")
        print("=" * 70)

        pilihan = input("Masukkan opsi pilihan : ").strip()

        if pilihan == "1":
            transaksi_baru()
        elif pilihan == "2":
            cari_transaksi()
        elif pilihan == "3":
            print("Aplikasi selesai.")
            break
        else:
            print("Pilihan tidak tersedia.")


if __name__ == "__main__":
    main()