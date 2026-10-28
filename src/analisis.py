def validasi_nilai(data):
    """Memeriksa apakah semua nilai berada di rentang 0-100."""
    for n in data:
        if n < 0 or n > 100:
            return False
    return True

def hitung_statistik(data):
    """Menghitung rata-rata, minimum, dan maksimum."""
    if not data:
        return {"rata_rata": 0, "minimum": 0, "maksimum": 0}
    
    total = sum(data)
    rata_rata = total / len(data)
    minimum = min(data)
    maksimum = max(data)
    
    return {
        "rata_rata": round(rata_rata, 2),
        "minimum": minimum,
        "maksimum": maksimum
    }

def tentukan_ketuntasan(data, kkm=75):
    """Menghitung jumlah siswa tuntas dan belum tuntas berdasarkan KKM."""
    tuntas = 0
    belum_tuntas = 0
    for n in data:
        if n >= kkm:
            tuntas += 1
        else:
            belum_tuntas += 1
            
    return {
        "tuntas": tuntas,
        "belum_tuntas": belum_tuntas
    }