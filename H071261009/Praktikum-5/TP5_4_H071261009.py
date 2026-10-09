def deteksi_anomali_email(email):
    masalah = []

    # Aturan 1: tepat satu @
    if email.count("@") != 1:
        masalah.append("Harus memiliki tepat satu karakter @.")
        return masalah

    posisi = email.find("@")
    local = email[:posisi]
    domain = email[posisi + 1:]

    if len(local) == 0 or len(domain) == 0:
        masalah.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if email.count(" ") > 0:
        masalah.append("Email tidak boleh mengandung spasi.")

    if local.startswith(".") or local.endswith(".") or local.find("..") != -1:
        masalah.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    if domain.count(".") == 0:
        masalah.append("Bagian domain wajib memiliki minimal satu titik.")
    if domain.find("..") != -1 or domain.endswith("."):
        masalah.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    # Aturan 7: domain resmi
    if not (email.endswith(".com") or email.endswith(".id") or email.endswith(".ac.id")):
        masalah.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return masalah


def cetak_daftar(daftar_email_valid, karakter_border):
    if len(daftar_email_valid) == 0:
        return "(Tidak ada email valid)"

    terpanjang = 0
    for email in daftar_email_valid:
        if len(email) > terpanjang:
            terpanjang = len(email)

    garis = "+" + karakter_border * (terpanjang + 2) + "+"
    hasil = garis
    for email in daftar_email_valid:
        spasi = " " * (terpanjang - len(email))
        hasil = hasil + "\n| " + email + spasi + " |"
    hasil = hasil + "\n" + garis
    return hasil


print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")[:1]
if border == "":
    border = "="

print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_valid = []
while True:
    email = input("Masukkan email: ")
    if email.lower() == "tutup":
        break

    masalah = deteksi_anomali_email(email)

    if len(masalah) == 0:
        for e in daftar_valid:
            if e.lower() == email.lower():
                masalah.append("Email sudah terdaftar (Duplikat).")

    if len(masalah) > 0:
        print(">> Email DITOLAK karena:")
        for m in masalah:
            print(f"   - {m}")
    else:
        daftar_valid.append(email)
        print(">> Email VALID!")

print("\n--- HASIL EMAIL VALID ---")
print(cetak_daftar(daftar_valid, border))