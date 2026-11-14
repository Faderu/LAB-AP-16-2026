import re

def validasi_username(username):
    pola = r"^[a-zA-Z][a-zA-Z0-9_]{4,11}$"
    hasil = re.match(pola, username)
    if hasil:
        return True
    else:
        return False

daftar_valid = []

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")
print()

while True:
    username = input("Masukkan username: ")
    if username == "SELESAI":
        break
    if validasi_username(username):
        print("Username tersedia.")
        daftar_valid.append(username)
    else:
        print("Username tidak valid!")
    print()

print()
print("=== Rekapitulasi ===")
print("Username valid:")
nomor = 1 #untuk penomoran daftar mulai dari 1
for nama in daftar_valid:
    print(str(nomor) + ". " + nama) # contohnya 1. Yuarnintia
    nomor += 1
print()
print("Jumlah username valid:", len(daftar_valid))