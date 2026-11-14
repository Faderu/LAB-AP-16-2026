class Pemain:

    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        return (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        return "Perlu Evaluasi"

    def tampilkan_data(self, no):
        skor = self.hitung_skor_akhir()
        print(
            f"| {no:<3} | {self.nama:^12} | {self.id_pemain:<12} | {self.role:<12} "
            f"| {skor:<10.2f} | {self.status_performa():<13} |"
        )


def input_angka(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            if nilai < 0:
                print("Nilai tidak boleh negatif. Coba lagi.")
                continue
            return int(nilai) if nilai.is_integer() else nilai
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")


def input_jumlah(pesan):
    while True:
        try:
            jumlah = int(input(pesan))
            if jumlah > 0:
                return jumlah
            print("Jumlah pemain harus lebih dari 0. Coba lagi.")
        except ValueError:
            print("Input harus berupa bilangan bulat. Coba lagi.")


def main():
    daftar_pemain = []

    print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
    print()
    jumlah = input_jumlah("Masukkan jumlah pemain: ")

    for i in range(1, jumlah + 1):
        print()
        print(f"-- Data Pemain ke-{i} --")
        nama = input("Nama: ")
        id_pemain = input("ID Pemain: ")
        role = input("Role: ")
        nilai_kill = input_angka("Nilai Kill: ")
        nilai_assist = input_angka("Nilai Assist: ")
        nilai_objective = input_angka("Nilai Objective: ")

        pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
        daftar_pemain.append(pemain)

    garis = "=" * 75
    print()
    print("=== REKAPITULASI PERFORMA PEMAIN ===")
    print(garis)
    print(f"| {'No':<3} | {'Nama':<12} | {'ID Pemain':<12} | {'Role':<12} | {'Skor Akhir':<10} | {'Status':<13} |")
    print(garis)
    for no, pemain in enumerate(daftar_pemain, start=1):
        pemain.tampilkan_data(no)
    print(garis)

main()