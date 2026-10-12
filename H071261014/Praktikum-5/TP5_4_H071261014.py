def deteksi_anomali_email(email):
    error = []

    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return 

    local, domain = email.split("@")

    if local == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if " " in email:
        error.append("Tidak boleh mengandung spasi.")

    if local.startswith(".") or local.endswith(".") or ".." in local:
        error.append("Bagian local tidak boleh diawali atau diakhiri titik, atau mengandung titik berurutan.")

    if "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    if not email.lower().endswith((".com", ".id", ".ac.id")):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    terpanjang = 0
    for email in daftar_email_valid:
        if len(email) > terpanjang:
            terpanjang = len(email)

    lebar = terpanjang + 2  
    garis = "+" + karakter_border * lebar + "+"

    baris = [garis]
    for email in daftar_email_valid:
        baris.append("| " + email.ljust(terpanjang) + " |")
    baris.append(garis)

    return "\n".join(baris)


print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")
if border == "":
    border = "="

print()
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_valid = []

while True:
    email = input("Masukkan email: ")

    if email.strip().lower() == "tutup":
        break

    anomali = deteksi_anomali_email(email)

    if not anomali:
        for tersimpan in daftar_valid:
            if tersimpan.lower() == email.lower():
                anomali.append("Email sudah terdaftar (Duplikat).")
                break

    if anomali:
        print(">> Email DITOLAK karena:")
        for pesan in anomali:
            print("   - " + pesan)
    else:
        daftar_valid.append(email)
        print(">> Email VALID!")

print()
print("--- HASIL EMAIL VALID ---")
if daftar_valid:
    print(cetak_daftar(daftar_valid, border))
else:
    print("(Tidak ada email valid)")