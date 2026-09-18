# nilai_tes = int(input("Masukkan nilai tes: "))
# pengalaman_kerja = int(input("Masukkan pengalaman kerja (tahun): "))

# if nilai_tes >= 80:
#     print("Lolos ke Tahap Wawancara")
# elif nilai_tes >= 65 and pengalaman_kerja >= 2:
#     print("Lolos Bersyarat")
# else:
#     print("Tidak Lolos")\

nilai_tes = int(input("masukkan nilai tes tertulis"))

if nilai_tes >= 80:
    print("lolos ke tahap wawancara")
elif nilai_tes < 80 and nilai_tes >= 65:
    pengalaman_kerja = int(input("masukkan pengalaman kerja (tahun)"))
    if pengalaman_kerja >= 2:
        print("Lolos bersyarat")
    else:
        print("tidak lolos")
else:
    print("tidak lolos")
