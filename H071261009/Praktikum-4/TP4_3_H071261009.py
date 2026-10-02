def hitung_mundur(n: int) -> None:
    print(n)
    if n == 0:
        print("Luncurkan!")
    else:
        hitung_mundur(n - 1)


def minta_angka() -> int:
   
    angka = int(input("Masukkan angka awal hitung mundur: "))
    if angka < 0:
        print("Input tidak valid, angka tidak boleh negatif.")
        return minta_angka()
    return angka


hitung_mundur(minta_angka())