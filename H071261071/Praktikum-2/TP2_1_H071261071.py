tingkat_kepedasan = int(input("Masukkan persentase cabai: "))

if tingkat_kepedasan >= 0 and tingkat_kepedasan <= 10:
    print("Level aman")
elif tingkat_kepedasan >= 11 and tingkat_kepedasan <= 40:
    print("Level sedang")
elif tingkat_kepedasan >= 41 and tingkat_kepedasan <= 70:
    print("Level Pedas")
elif tingkat_kepedasan > 70 and tingkat_kepedasan <= 100:
    print("Level Ekstrem")
else:
    print("Tidak Valid")