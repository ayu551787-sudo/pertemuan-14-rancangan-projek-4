def baca_data(path):
    """Membaca file nilai dan mengembalikan dalam bentuk list angka."""
    data = []
    try:
        with open(path, "r") as file:
            for baris in file:
                nilai = baris.strip()
                if nilai:
                    data.append(float(nilai))
    except FileNotFoundError:
        print(f"File {path} tidak ditemukan.")
    return data

def simpan_laporan(path, statistik, status):
    """Menulis hasil statistik dan status ketuntasan ke file teks."""
    with open(path, "w") as file:
        file.write("--- LAPORAN ANALISIS NILAI KELAS ---\n")
        file.write(f"Rata-rata : {statistik['rata_rata']}\n")
        file.write(f"Minimum   : {statistik['minimum']}\n")
        file.write(f"Maksimum  : {statistik['maksimum']}\n")
        file.write(f"Tuntas    : {status['tuntas']}\n")
        file.write(f"Belum     : {status['belum_tuntas']}\n")
    print(f"Laporan berhasil disimpan ke {path}")