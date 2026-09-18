jarak = int(input( "Masukkan jarak pengiriman (km): "))
express = input("Layanan express (ya/tidak): ")

if 0 <= jarak < 5 :
    jarak = 10000
elif 5 <= jarak <= 20:
    jarak = 20000
else :
    jarak = 35000
layanan = 15000 if express == "ya" else 0
tarif = jarak + layanan
print("Total tarif pengiriman: Rp", tarif)
