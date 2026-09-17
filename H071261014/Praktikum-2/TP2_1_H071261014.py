# nomor 1
presentase = float(input("masukkan presentase cabai: "))

if presentase < 0:
    print("input tidak valid")
elif 0 <= presentase <= 10:
    print("level aman")
elif presentase <= 40:
    print("level sedang")
elif presentase <= 70:
    print("level pedas")
else:
    print("level ekstrem")
