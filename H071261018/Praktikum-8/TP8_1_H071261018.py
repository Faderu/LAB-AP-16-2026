import re

def validasi_nim(nim):
    pola = r"^H071\d{6}$"
    #apakah sebuah string cocok dengan pattern mulai dari awal string. 
    hasil = re.match(pola, nim)
    if hasil:
        return True
    else:
        return False

def validasi_email(email):
    pola = r"^\w+@\w+\.[a-zA-Z]{2,}$"
    hasil = re.match(pola, email)
    if hasil:
        return True
    else:
        return False

def validasi_telepon(telepon):
    pola = r"^\d{10,13}$"
    hasil = re.match(pola, telepon)
    if hasil:
        return True
    else:
        return False

print("=== Validasi Data Mahasiswa ===")
print()
nim = input("Masukkan NIM      : ").strip()  
email = input("Masukkan Email    : ").strip()
telepon = input("Masukkan No. Telp : ").strip()

nim_ok = validasi_nim(nim)
email_ok = validasi_email(email)
telepon_ok = validasi_telepon(telepon)

print()
print("--- Hasil Validasi ---")
if nim_ok:
    print("NIM         : Valid")
else:
    print("NIM         : Format NIM tidak valid!")
if email_ok:
    print("Email       : Valid")
else:
    print("Email       : Format email tidak valid!")
if telepon_ok:
    print("No. Telepon : Valid")
else:
    print("No. Telepon : Nomor telepon tidak valid!")

print()
if nim_ok and email_ok and telepon_ok:
    print("Data mahasiswa berhasil diverifikasi!")