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
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self, no):
        skor = self.hitung_skor_akhir()
        status = self.status_performa()
        print(f"| {no:<3} | {self.nama:<10} | {self.id_pemain:<11} | {self.role:<10} | {skor:<10.2f} | {status:<14} |")


data_pemain = []

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")

while True:
    try:
        jumlah_pemain = int(input("\nMasukkan jumlah pemain: "))
        if jumlah_pemain <= 0:
            print("Jumlah pemain harus lebih dari 0!")
        else:
            break
    except ValueError:
        print("Input yang anda masukkan tidak valid!")

pemain = 1
while pemain <= jumlah_pemain:
    try:
        print(f"\n-- Data Pemain ke-{pemain} --")
        data_nama = input("Nama: ")
        data_id = input("ID Pemain: ")
        data_role = input("Role: ")
        data_kill = int(input("Nilai Kill: "))
        data_assist = int(input("Nilai Assist: "))
        data_objective = int(input("Nilai Objective: "))
        data_pemain.append(Pemain(data_nama, data_id, data_role, data_kill, data_assist, data_objective))
        pemain += 1
    except ValueError:
        print("Input yang anda masukkan tidak valid!")

print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
print("=" * 77)
print(f"| {'No':<3} | {'Nama':<10} | {'ID Pemain':<11} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<14} |")
print("=" * 77)
for i, isi in enumerate(data_pemain, start=1):
    isi.tampilkan_data(i)
print("=" * 77)