def deteksi_anomali_email(email):
    masalah = []

    if email.count("@") != 1:
        return ["Harus memiliki tepat satu karakter @."]

    local, domain = email.split("@")

    if local == "" or domain == "":
        masalah.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")
    if " " in email:
        masalah.append("Tidak boleh mengandung spasi.")
    if local.startswith(".") or local.endswith(".") or ".." in local:
        masalah.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")
    if "." not in domain:
        masalah.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        masalah.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")
    if not (email.endswith(".com") or email.endswith(".id") or email.endswith(".ac.id")):
        masalah.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return masalah

def cetak_daftar(daftar_email_valid, karakter_border):
    terpanjang = 0
    for email in daftar_email_valid:
        terpanjang = max(terpanjang, len(email))

    garis = "+" + karakter_border * (terpanjang + 2) + "+"
    hasil = garis + "\n"
    for email in daftar_email_valid:
        hasil += "| " + email.ljust(terpanjang) + " |\n"   
    return hasil + garis

print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ") or "="
print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")

email_valid = []
while True:
    email = input("Masukkan email: ")
    if email.strip().lower() == "tutup":
        break

    masalah = deteksi_anomali_email(email)
    if not masalah and email in email_valid:
        masalah.append("Email sudah terdaftar (Duplikat).")

    if masalah:
        print(">> Email DITOLAK karena:")
        for pesan in masalah:
            print("   -", pesan)
    else:
        email_valid.append(email)
        print(">> Email VALID!")

print("\n--- HASIL EMAIL VALID ---")
print(cetak_daftar(email_valid, border))