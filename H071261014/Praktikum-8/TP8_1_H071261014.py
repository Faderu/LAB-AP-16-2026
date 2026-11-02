import re


def validasi_nim(nim):
    return re.fullmatch(r"H071[0-9]{6}", nim) is not None


def validasi_email(email):
    pola = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
    return re.fullmatch(pola, email) is not None


def validasi_telepon(telp):
    return re.fullmatch(r"[0-9]{10,13}", telp) is not None


def main():
    print("=== Validasi Data Mahasiswa ===\n")

    nim = input("Masukkan NIM      : ")
    email = input("Masukkan Email    : ")
    telp = input("Masukkan No. Telp : ")

    nim_ok = validasi_nim(nim)
    email_ok = validasi_email(email)
    telp_ok = validasi_telepon(telp)

    print("\n--- Hasil Validasi ---")
    print("NIM         :", "Valid" if nim_ok else "Format NIM tidak valid!")
    print("Email       :", "Valid" if email_ok else "Format email tidak valid!")
    print("No. Telepon :", "Valid" if telp_ok else "Nomor telepon tidak valid!")

    if nim_ok and email_ok and telp_ok:
        print("\nData mahasiswa berhasil diverifikasi!")


main()