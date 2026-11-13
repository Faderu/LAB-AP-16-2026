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
        status = self.status_performa()
        print(f"| {no:<2} | {self.nama:<10} | {self.id_pemain:<11} | "
              f"{self.role:<9} | {skor:<10.2f} | {status:<14} |")


def main():
    print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
    jumlah = int(input("\nMasukkan jumlah pemain: "))

    daftar_pemain = []  # list untuk menyimpan objek Pemain

    # Perulangan input data pemain
    for i in range(1, jumlah + 1):
        print(f"\n-- Data Pemain ke-{i} --")
        nama = input("Nama: ")
        id_pemain = input("ID Pemain: ")
        role = input("Role: ")
        nilai_kill = float(input("Nilai Kill: "))
        nilai_assist = float(input("Nilai Assist: "))
        nilai_objective = float(input("Nilai Objective: "))

        pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
        daftar_pemain.append(pemain)

    # Menampilkan rekapitulasi dalam bentuk tabel
    header = f"| {'No':<2} | {'Nama':<10} | {'ID Pemain':<11} | {'Role':<9} | {'Skor Akhir':<10} | {'Status':<14} |"
    garis = "=" * len(header)

    print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
    print(garis)
    print(header)
    print(garis)
    for no, pemain in enumerate(daftar_pemain, start=1):
        pemain.tampilkan_data(no)
    print(garis)


main()