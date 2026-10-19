def deteksi_anomali_email(email):
    pelanggaran = []

    if email.count("@") != 1:
        pelanggaran.append("Harus memiliki tepat satu karakter @.")
        return pelanggaran

    posisi_at = email.find("@")
    local = email[:posisi_at]
    domain = email[posisi_at + 1:]

    if local == "" or domain == "":
        pelanggaran.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if email.count(" ") > 0:
        pelanggaran.append("Tidak boleh mengandung spasi.")

    if local.startswith(".") or local.endswith(".") or local.find("..") != -1:
        pelanggaran.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    if domain.count(".") == 0:
        pelanggaran.append("Bagian domain wajib memiliki minimal satu titik.")

    if domain.find("..") != -1 or domain.endswith("."):
        pelanggaran.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    if not (email.endswith(".com") or email.endswith(".id") or email.endswith(".ac.id")):
        pelanggaran.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return pelanggaran


def cetak_daftar(daftar_email_valid, karakter_border):
    lebar = 0
    for email in daftar_email_valid:
        if len(email) > lebar:
            lebar = len(email)

    garis = "+" + karakter_border * (lebar + 2) + "+"

    hasil = garis
    for email in daftar_email_valid:
        hasil = hasil + "\n" + "| " + email + " " * (lebar - len(email)) + " |"
    hasil = hasil + "\n" + garis
    return hasil


print("--- Sistem Pencatatan email valid ---")
karakter_border = input("Masukkan border dengan karakter bebas: ")

print()
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_valid = []
while True:
    email = input("Masukkan email: ")
    if email == "tutup":
        break

    masalah = deteksi_anomali_email(email)
    if email in daftar_valid:
        masalah.append("Email sudah terdaftar (Duplikat).")

    if len(masalah) == 0:
        daftar_valid.append(email)
        print(">> Email VALID!")
    else:
        print(">> Email DITOLAK karena:")
        for pesan in masalah:
            print("   - " + pesan)

print()
print("--- HASIL EMAIL VALID ---")
print(cetak_daftar(daftar_valid, karakter_border))