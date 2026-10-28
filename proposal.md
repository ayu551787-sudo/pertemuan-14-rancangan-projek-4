# Proposal Proyek: Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Latar Belakang
Guru sering kali membutuhkan waktu yang tidak sebentar untuk merekap nilai ujian siswa secara manual, menghitung rata-rata, menentukan nilai tertinggi dan terendah, serta mengecek siapa saja siswa yang belum mencapai Kriteria Ketuntasan Minimal (KKM). Oleh karena itu, dibutuhkan program sederhana berbasis Python untuk mengotomatisasi proses tersebut agar lebih cepat, akurat, dan rapi

## 2. Tujuan Spesifik
* Membaca kumpulan data nilai siswa dari file eksternal secara otomatis
* Memvalidasi bahwa seluruh rentang nilai yang dimasukkan berada pada skala 0 sampai 100
* Menghitung nilai rata-rata kelas, nilai minimum, dan nilai maksimum
* Mengelompokkan jumlah siswa yang tuntas dan belum tuntas berdasarkan KKM yang ditentukan
* Menyimpan hasil laporan rekapitulasi ke dalam file teks agar mudah dicetak atau dibagikan

## 3. Ruang Lingkup Proyek
* **Bahasa Pemrograman:** Python 3.x
* **Format Data Masukan:** File teks (`.txt`) berisi daftar angka nilai siswa.
* **Format Laporan Keluaran:** File teks (`.txt`) ringkasan statistik dan status kelulusan kelas.
* **Batasan:** Program dijalankan secara *command-line* (berbasis teks di terminal) tanpa antarmuka grafis yang rumit, sehingga pas dan realistis untuk diselesaikan dalam waktu proyek pembelajaran

## 4. Pembagian Tugas Tim
* **Anggota 1 (Bagian I/O Data):** Bertanggung jawab membuat fungsi membaca file nilai dan menulis hasil laporan (`src/data_io.py`)
* **Anggota 2 (Bagian Logika Analisis):** Bertanggung jawab membuat fungsi validasi nilai, perhitungan statistik, dan penentuan ketuntasan (`src/analisis.py`)
* **Anggota 3 (Bagian Pengujian & Dokumentasi):** Bertanggung jawab menyusun file *test case* (`tests/test_case.md`) dan merapikan file utama (`src/main.py`)