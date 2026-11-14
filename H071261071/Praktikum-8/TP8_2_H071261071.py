import re

def validasi_username(username):
    pola = r"^[A-Za-z][A-Za-z0-9_]{4,11}$"

    if re.match(pola, username):
        return True
    else:
        return False

username_valid = []

while True:
    username = input("Masukkan username (atau SELESAI): ")

    if username.lower() == "selesai":
        break

    if validasi_username(username):
        print("Username tersedia.")
        username_valid.append(username)
    else:
        print("Username tidak valid!")

print("\n--- Rekapitulasi ---")
print("\nUsername valid:")
for username in username_valid:
    print(username)

print("Jumlah username yang valid:", len(username_valid))