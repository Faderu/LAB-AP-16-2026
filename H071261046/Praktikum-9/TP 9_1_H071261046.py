class Pemain:
    def __init__ (self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id = id_pemain
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
        performa = self.status_performa()
        print(f"| {no+1:<3} | {self.nama:<8} | {self.id:<13} | {self.role:<18} | {skor:<18.2f} | {performa:<15} |")
        

print ("=== SISTEM PENILAIAN PERFORMA PEMAIN\n")
jumlah_pemain = int(input("Masukkan jumlah pemain: "))
daftar_pemain = []

for i in range(jumlah_pemain):
    print()
    print("-- Data pemain ke-",i+1,"--")
    nama = input("Nama: ")
    id = input("ID Pemain: ")
    role = input("Role: ")
    nilai_kill = int(input("Nilai Kill: "))
    nilai_assist = int(input("Nilai Assist: "))
    nilai_objective = int(input("Nilai Objective: "))

    data_objek = Pemain (nama, id, role, nilai_kill, nilai_assist, nilai_objective)
    daftar_pemain.append(data_objek)

print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
print("=" * 94)
print(f"| {"No":<3} | {"Nama":<8} | {"ID Pemain":<13} | {"Role":<18} | {"Skor Akhir":<18} | {"Status":<15} |")
print("=" * 94)
for i, x in enumerate(daftar_pemain):
    x.tampilkan_data(i)
print("=" * 94)


