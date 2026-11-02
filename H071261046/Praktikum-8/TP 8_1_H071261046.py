import re

def validasi_nim(nim):
    return re.fullmatch(r"H071\d{6}", nim) is not None

def validasi_email(email):
    pola = r"[\w]+@[\w]+(\.[\w]+)*\.[\w]{2,}"
    return re.fullmatch(pola, email) is not None

def validasi_telepon(telepon):
    return re.fullmatch(r"\d{10,13}", telepon) is not None

def status_teks(hasil, pesan_error):
    if hasil:
        return "Valid"
    else:
        return pesan_error

print("=== Validasi Data Mahasiswa ===")
print()
nim = input("Masukkan NIM : ").strip()
email = input("Masukkan Email : ").strip()
telepon = input("Masukkan No. Telp : ").strip()

nim_valid = validasi_nim(nim)
email_valid = validasi_email(email)
telepon_valid = validasi_telepon(telepon)

print()
print("--- Hasil Validasi ---")
print("NIM         :", status_teks(nim_valid, "Format NIM tidak valid!"))
print("Email       :", status_teks(email_valid, "Format email tidak valid!"))
print("No. Telepon :", status_teks(telepon_valid, "Nomor telepon tidak valid!"))
print()

if nim_valid and email_valid and telepon_valid:
    print("Data mahasiswa berhasil diverifikasi!")