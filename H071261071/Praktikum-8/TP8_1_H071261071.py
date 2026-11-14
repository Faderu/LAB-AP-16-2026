import re

def validasi_nim(nim):
    if re.match(r"^H071\d{6}$", nim):
        return True
    else:
        return False

def validasi_email(email):
    pola_email = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if re.match(pola_email, email):
        return True
    else:
        return False

def validasi_telepon(telepon):
    if re.match(r"^\d{10,13}$", telepon):
        return True
    else:
        return False

print("=== Validasi Data Mahasiswa ===")

nim = input("Masukkan NIM      : ")
email = input("Masukkan Email    : ")
telepon = input("Masukkan No. Telp : ")

status_nim = validasi_nim(nim)
status_email = validasi_email(email)
status_telepon = validasi_telepon(telepon)

print("\n--- Hasil Validasi ---")
print("NIM        :", "Valid" if status_nim else "Tidak Valid")
print("Email      :", "Valid" if status_email else "Tidak Valid")
print("No. Telepon:", "Valid" if status_telepon else "Tidak Valid")

if status_nim and status_email and status_telepon:
    print("\nData mahasiswa berhasil diverifikasi!")