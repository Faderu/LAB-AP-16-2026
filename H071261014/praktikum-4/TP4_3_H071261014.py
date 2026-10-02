def hitung_mundur(n):
    print(n)
    if n == 0:
        print("Luncurkan!")
    else:
        hitung_mundur(n - 1)


while True:
    angka_awal = int(input("Masukkan angka awal hitung mundur: "))
    if angka_awal < 0:
        print("Input tidak valid, angka tidak boleh negatif.")
    else:
        break

hitung_mundur(angka_awal)