import re


def validasi_username(username):
    return re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{4,11}", username) is not None


def main():
    username_valid = []

    print("=== Registrasi Username ===")
    print("Ketik 'SELESAI' untuk mengakhiri.")

    while True:
        print()
        username = input("Masukkan username: ")

        if username == "SELESAI":
            break

        if validasi_username(username):
            print("Username tersedia.")
            username_valid.append(username)
        else:
            print("Username tidak valid!")

    print("\n=== Rekapitulasi ===")
    print("Username valid:")

    if username_valid:
        for i, nama in enumerate(username_valid, start=1):
            print(f"{i}. {nama}")
    else:
        print("(tidak ada)")

    print(f"\nJumlah username valid: {len(username_valid)}")


main()