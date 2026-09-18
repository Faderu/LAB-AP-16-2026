# SOAL 2
jarak = int(input("Masukkan jarak pengiriman (km): ")) 
express = input("Layanan express (ya/tidak): ")
if jarak < 5:
     tarif_dasar = 10000
elif jarak <= 20:
     tarif_dasar = 20000
else:
     tarif_dasar = 35000
total = tarif_dasar + 15000 if express == "ya" else 0
print("Total Tarif Pengiriman: Rp", total)
