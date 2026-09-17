#program 2
jarak = float(input("Masukkan jarak pengiriman (km):  "))
express_input = str(input("layanan express (ya/tidak): ")).lower().strip()
if jarak < 5:
    harga = 10000
elif 5 <= jarak <= 20:
    harga = 20000
elif jarak > 20:
    harga = 35000
express = 15000 if express_input=="ya" else 0
tarif = harga + express
print ("Total tarif pengiriman: ", tarif)
