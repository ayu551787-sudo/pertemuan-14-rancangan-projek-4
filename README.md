
# Pertemuan 14 - Perancangan Proyek Program Sederhana

**Mata Kuliah:** Algoritma dan Pemrograman  
**Nama:** Ayu Syarifatu Zahra  
**NIM:** 2225250043  
**Kelas:** 3B  
**Kelompok:** 4 
**Tahun Ajaran:** 2026/2027 Ganjil  

## 1. Judul Proyek

Program Rekap dan Analisis Nilai kuis Matematika Kelas

## 2. Latar Belakang

Pengolahan nilai siswa merupakan salah satu kegiatan penting dalam pembelajaran matematika. Guru perlu menghitung rata-rata, menentukan nilai tertinggi dan terendah, serta mengetahui jumlah siswa yang sudah mencapai ketuntasan belajar.

Pengolahan nilai secara manual membutuhkan waktu dan berisiko menimbulkan kesalahan perhitungan.

Oleh karena itu, dirancang program sederhana menggunakan Python untuk membantu guru mengolah data nilai siswa secara otomatis, akurat, dan terstruktur.

## 3. Tujuan Proyek

Tujuan perancangan proyek ini adalah:

1. Membuat rancangan program pengolahan nilai matematika.
2. Mempermudah guru dalam menghitung statistik nilai siswa.
3. Menentukan status ketuntasan berdasarkan KKM.
4. Mengurangi kesalahan dalam pengolahan nilai.
5. Menyimpan hasil rekap nilai ke dalam file teks.
6. Menerapkan konsep Python yang telah dipelajari.

## 4. Pengguna Program

Pengguna utama program ini adalah guru matematika.

Program dirancang untuk membantu guru membaca data nilai, menghitung statistik kelas, menentukan status ketuntasan, dan menyimpan laporan hasil belajar.

## 5. Ruang Lingkup Proyek

### Fitur Wajib

1. Membaca data nilai siswa dari file.
2. Memvalidasi nilai dengan rentang 0–100.
3. Menghitung rata-rata nilai.
4. Menentukan nilai minimum dan maksimum.
5. Menghitung jumlah siswa tuntas dan belum tuntas.
6. Menyimpan hasil rekap ke file teks.

### Fitur Tambahan

1. Menampilkan statistik berdasarkan kategori.
2. Menampilkan pesan kesalahan jika data tidak valid.
3. Menampilkan ringkasan nilai pada terminal.

### Batasan Proyek

- Program dibuat menggunakan bahasa Python.
- Program dijalankan melalui terminal VS Code.
- Data disimpan dalam file teks.
- Program tidak menggunakan antarmuka grafis.
- Program tidak menggunakan database eksternal.

## 6. Analisis Kebutuhan

### Kebutuhan Fungsional

| ID | Kebutuhan | Prioritas |
|---|---|---|
| F01 | Membaca data nilai siswa | Wajib |
| F02 | Memvalidasi nilai 0–100 | Wajib |
| F03 | Menghitung rata-rata, minimum, maksimum | Wajib |
| F04 | Menentukan status ketuntasan | Wajib |
| F05 | Menyimpan laporan hasil analisis | Wajib |
| F06 | Menampilkan statistik tambahan | Tambahan |

### Kebutuhan Nonfungsional

1. Program mudah dijalankan melalui terminal.
2. Pesan kesalahan mudah dipahami.
3. Nama fungsi dan variabel jelas.
4. Data contoh tidak menggunakan informasi pribadi nyata.
5. Program dapat diuji menggunakan test case yang sama.

## 7. Input, Proses, dan Output (IPO)

| Komponen | Keterangan |
|---|---|
| Input | Data nama dan nilai siswa dari file |
| Proses | Membaca data, validasi, perhitungan statistik, dan penentuan ketuntasan |
| Output | Rata-rata, nilai minimum, maksimum, jumlah tuntas, jumlah belum tuntas, dan laporan |

### Contoh Input

```text
ayu,80
paji,75
ruto,90
dami,55
mashi,60
sahi,100
klara,45
cipa,85
```

### Contoh Output

```text
=== REKAP NILAI MATEMATIKA ===

Rata-rata : 73.75
Minimum   : 45.0
Maksimum  : 100.0
Tuntas    : 5
Belum     : 3
```

KKM 75 digunakan sebagai contoh rancangan proyek.

## 8. Algoritma Program

Langkah-langkah algoritma:

1. Mulai program.
2. Membaca data nilai siswa dari file.
3. Memeriksa apakah file tersedia.
4. Jika file tidak ditemukan, tampilkan pesan kesalahan.
5. Membaca data baris demi baris.
6. Memvalidasi format dan nilai siswa.
7. Menyimpan data yang valid.
8. Memeriksa apakah terdapat data valid.
9. Menghitung rata-rata, minimum, dan maksimum.
10. Menentukan status ketuntasan berdasarkan KKM.
11. Menghitung jumlah siswa tuntas dan belum tuntas.
12. Menampilkan hasil rekap.
13. Menyimpan laporan ke file teks.
14. Selesai.

## 10. Struktur Program

Program dirancang menggunakan beberapa fungsi agar lebih mudah dipahami dan dikembangkan.

| Fungsi | Tanggung Jawab |
|---|---|
| baca_data() | Membaca data dari file |
| validasi_nilai() | Memeriksa nilai 0–100 |
| hitung_statistik() | Menghitung rata-rata, minimum, maksimum |
| tentukan_status() | Menentukan ketuntasan |
| simpan_laporan() | Menyimpan laporan ke file |
| main() | Mengatur jalannya program |

## 12. Struktur Data

Program menggunakan beberapa struktur data Python.

| Struktur Data | Kegunaan |
|---|---|
| List | Menyimpan kumpulan nilai siswa |
| Dictionary | Menyimpan identitas dan nilai siswa |
| String | Menyimpan nama dan teks laporan |
| File TXT | Menyimpan input dan hasil rekap |

### Contoh Dictionary

```python
data_mahasiswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78},
    "A003": {"nama": "Citra", "nilai": 92}
}
```

## 13. Test Case Awal

Test case disusun sebelum implementasi program untuk memastikan setiap fitur dapat diuji.

| ID | Kategori | Input/Kondisi | Expected Result | Status |
|---|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80 | Belum diuji |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid | Belum diuji |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid | Belum diuji |
| TC04 | Invalid | Nilai 105 | Ditolak dengan pesan validasi | Belum diuji |
| TC05 | Invalid | File tidak ada | FileNotFoundError ditangani | Belum diuji |
| TC06 | Normal | Semua nilai >= KKM | Jumlah tuntas sama dengan jumlah data | Belum diuji |

### Kriteria Keberhasilan

- [ ] Semua fitur wajib berjalan.
- [ ] Semua test case berhasil.
- [ ] Program menangani error yang diprediksi.
- [ ] Output mudah dibaca.
- [ ] README menjelaskan cara menjalankan program.
- [ ] Riwayat commit menunjukkan kontribusi anggota.

## 16. Cara Menjalankan

Pada Pertemuan 14, program masih dalam tahap perancangan dan belum diimplementasikan sepenuhnya.

Setelah implementasi pada Pertemuan 15, program direncanakan dapat dijalankan melalui terminal VS Code menggunakan perintah:

```bash
python src/main.py
```

## 17. Pengelolaan GitHub

Proyek menggunakan GitHub sebagai tempat penyimpanan dokumentasi, kode program, dan riwayat perubahan.

### Nama Repository

```text
proyek-akhir-nama-tim
```

### URL Repository

```text
https://github.com/USERNAME/proyek-akhir-nama-tim
```

### Commit Dokumentasi

```bash
git add README.md proposal.md tests/
git commit -m "docs: menambahkan proposal dan test case proyek"
git push
```

## 18. Refleksi

Pada pertemuan 14, saya mempelajari bahwa sebelum membuat sebuah program, diperlukan perencanaan yang jelas agar proses implementasi dapat berjalan dengan baik.

Hal penting yang saya pahami adalah menentukan masalah, kebutuhan pengguna, fitur program, algoritma, struktur data, dan test case sebelum mulai menulis kode.

Bagian yang paling penting dalam perancangan ini adalah penyusunan algoritma dan test case karena keduanya menjadi pedoman dalam proses implementasi dan pengujian program.

Melalui kegiatan ini, saya juga memahami pentingnya pembagian tugas dan penggunaan GitHub untuk mendukung kerja sama kelompok.

## 19. Kesimpulan

Pertemuan 14 membahas perancangan proyek program sederhana untuk menyelesaikan masalah matematika atau pembelajaran matematika.

Proyek yang dirancang adalah Program Rekap dan Analisis Nilai Matematika Kelas.

Rancangan mencakup identifikasi masalah, analisis kebutuhan, input-proses-output, algoritma, pseudocode, struktur program, struktur data, test case, dan pembagian tugas.

Hasil perancangan ini akan menjadi dasar implementasi, pengujian, dan dokumentasi program pada Pertemuan 15.

## 20. Referensi

1. Bahan Ajar Algoritma dan Pemrograman Pertemuan 14, FKIP Universitas Sultan Ageng Tirtayasa, 2026/2027.
2. Python Software Foundation. Python 3 Documentation.
3. Downey, A. B. (2015). Think Python: How to Think Like a Computer Scientist.
4. GitHub Docs. About Repositories and Collaborative Development.
