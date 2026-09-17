#program 3
nilai_tes = int(input("Masukkan nilai tes: "))
if nilai_tes >= 80:
    print ("Lolos ke Tahap Wawancara")
elif 65<= nilai_tes <= 80:
    pengalaman = int(input("Masukkan pengalaman kerja: "))
    if pengalaman >= 2:
        print ("Lolos bersyarat")
    else:
        print ("Tidak lulus")
else:
    print ("Tidak lulus")