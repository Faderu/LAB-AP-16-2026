ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    pos = ALFABET.find(ch.lower())
    if pos == -1:                         
        return ch
    huruf = ALFABET[(pos + k) % 26]       
    if ch == ch.upper():                  
        return huruf.upper()
    return huruf

def mesin_enkripsi(teks, k):
    hasil = ""
    for c in teks:
        hasil += cek_sandi(c, k)
    return hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)       

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        pesan = mesin_dekripsi(sandi, k)
        if pesan.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan))
    return hasil

sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kunci = input("Masukkan kata kunci target: ")
print("\nOutput Deskripsi:", retas_sandi(sandi, kunci))