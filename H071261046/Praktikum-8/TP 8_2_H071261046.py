import re

def validasi_username(username):
    return re.fullmatch(r"[A-Za-z][\w_]{4,11}", username) is not None

username_valid = []

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")

while True:
    print()
    username = input("Masukkan username: ")
    if username.strip().upper() == "SELESAI":
        break
    if validasi_username(username):
        username_valid.append(username)
        print("Username tersedia.")
    else:
        print("Username tidak valid!")

print()
print("=== Rekapitulasi ===")
print("Username valid:")
if len(username_valid) == 0:
    print("(tidak ada)")
else:
    nomor = 0
    for nama in username_valid:
        nomor += 1
        print(f"{nomor}. {nama}")
print()
print(f"Jumlah username valid: {len(username_valid)}")