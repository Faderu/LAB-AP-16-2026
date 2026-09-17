#program 1
persentase_cabai = int(input("Masukkan persentase:"))
if 0 <= persentase_cabai <= 10:
    print ("Level Aman")
elif 11 <= persentase_cabai < 41:
    print ("Level Sedang")
elif 41<= persentase_cabai < 71:
    print ("Level Pedas")
elif 71 <= persentase_cabai <= 100:
    print ("Level Ekstrem")
else :
    print ("Input tidak valid")