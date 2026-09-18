nilai = int(input ("Masukkan nilai tes: "))
# pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))

# if nilai >= 80:
#     print ("Lolos ke Tahap Wawancara")
# if nilai >= 65 and pengalaman >= 2:
#     print("Lolos Bersyarat")
# else:
#     print ("Tidak Lolos")

if nilai >= 80 :
    print ("lolos ke tahap wawancara")
elif 65 <= nilai < 80 :
    pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))
    if pengalaman >= 2:
        print ("lolos bersyarat")
    else:
        print ("tidak lolos")
else:
    print ("tidak lolos")