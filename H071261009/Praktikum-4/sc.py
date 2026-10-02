# Buatkan fungsi rumus Keliling dan Luas lingkaran
# Parameter jari-jari, parameter berupa inputan 
def rumus_luas(r):
    luas = 3.14 * r * r
    return luas 

def Rumus_keliling(r):
    keliling = 2 * 3.14* r
    return keliling 

jjl = float(input("masukkan jari jari luas: ")) 
jjk = float(input("masukkan jari jari keliling: "))

print("Hasil Luas Lingkaran: ", rumus_luas(jjl))
print("Hasil Keliling lingkaran :", Rumus_keliling(jjk))
















