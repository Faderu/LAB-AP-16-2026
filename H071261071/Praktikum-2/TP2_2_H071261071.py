jarak_pengiriman = int(input("Masukkan jarak pengiriman (km): "))
layanan_express = input("Layanan express (ya/tidak): ")

if jarak_pengiriman < 0:
    print("Jarak pengiriman tidak valid")
elif jarak_pengiriman < 5:
    total_tarif_pengiriman = 10000
    print("Total tarif pengiriman: Rp10.000")
elif jarak_pengiriman <= 20:
    total_tarif_pengiriman = 20000
    print("Total tarif pengiriman: Rp20.000")
else:
    total_tarif_pengiriman = 35000
    print("Total tarif pengiriman: Rp35.000")

layanan_express = 15000 if layanan_express == "ya" else 0
total_tarif_pengiriman = total_tarif_pengiriman + layanan_express
print(f"Total tarif pengiriman: Rp{total_tarif_pengiriman}")