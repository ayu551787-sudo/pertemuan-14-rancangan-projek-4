# Dokumen Pengujian (Test Case)

1. **Uji Coba Baca Data Normal:**
   * Input: `data/nilai.txt` berisi nilai valid (0-100).
   * Ekspektasi: Program membaca seluruh baris dengan benar dan menghasilkan perhitungan statistik yang akurat.

2. **Uji Coba Validasi Gagal:**
   * Input: File teks yang berisi angka `-5` atau `105`.
   * Ekspektasi: Program menghentikan proses analisis dan menampilkan pesan error validasi.