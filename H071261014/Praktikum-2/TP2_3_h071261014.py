# nomor 3
nilai = float(input("Masukkan nilai tes: "))
# pengalaman = float(input("Masukkan pengalaman kerja: "))

# if nilai >= 80:
#     print("Lolos ke Tahap Wawancara")

# elif nilai >= 65 and pengalaman >= 2:
#     print("Lolos Bersyarat")

# else:
#     print("Tidak Lolos")
#elif 0 <= presentase <= 10:

if nilai >= 80:
    print("lolos ke tahap wawancara")

else:
    pengalaman = float(input("Masukkan pengalaman kerja: "))
    if 65 <= nilai <= 80 and pengalaman >= 2:
        print("lolos bersyarat")


    else:
        print("tidak lolos")

#if nilai >= 65 and nilai <= 80
        