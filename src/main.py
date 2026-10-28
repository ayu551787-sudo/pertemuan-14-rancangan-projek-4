from data_io import baca_data, simpan_laporan
from analisis import validasi_nilai, hitung_statistik, tentukan_ketuntasan
from utilitas import tampilkan_pesan

def main():
    path_input = "../data/nilai_contoh.txt"
    path_output = "../output/laporan_nilai.txt"
    kkm = 75
    
    data = baca_data(path_input)
    
    if not data:
        tampilkan_pesan("Data kosong atau file tidak ditemukan.")
    elif not validasi_nilai(data):
        tampilkan_pesan("Validasi gagal! Ada nilai di luar rentang 0-100.")
    else:
        statistik = hitung_statistik(data)
        status = tentukan_ketuntasan(data, kkm)
        
        print("--- HASIL ANALISIS ---")
        print(f"Rata-rata: {statistik['rata_rata']}")
        print(f"Nilai Min: {statistik['minimum']}")
        print(f"Nilai Max: {statistik['maksimum']}")
        print(f"Siswa Tuntas (>= {kkm}): {status['tuntas']}")
        print(f"Siswa Belum Tuntas: {status['belum_tuntas']}")
        
        simpan_laporan(path_output, statistik, status)

if __name__ == "__main__":
    main()