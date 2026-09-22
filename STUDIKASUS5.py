tarif_parkir = {
    "mobil": 5000,
    "motor": 3000
}

# MENGHITUNG BIAYA PARKIR
def hitung_biaya_parkir(jenis_kendaraan, lama_parkir):
    """
    Parameter:
    - jenis_kendaraan (str): 'mobil' atau 'motor'
    - lama_parkir (int/float): lama parkir dalam jam

    Return:
    - total_biaya (int/float): total biaya parkir
    """
    jenis_kendaraan = jenis_kendaraan.lower()  

    # MENENTUKAN TARIF
    if jenis_kendaraan == "mobil":
        tarif_per_jam = tarif_parkir["mobil"]
    elif jenis_kendaraan == "motor":
        tarif_per_jam = tarif_parkir["motor"]
    else:
        return None  # jenis kendaraan tidak dapat dikenali

    # Jika parkir kurang dari 1 jam, tetap dihitung 1 jam (pembulatan ke atas)
    import math
    jam_dihitung = math.ceil(lama_parkir)

    total_biaya = tarif_per_jam * jam_dihitung
    return total_biaya


# MENGHITUNG DURASI JAM MASUK DAN JAM KELUAR
def hitung_durasi(jam_masuk, jam_keluar):
    """
    jam_masuk dan jam_keluar berupa string format 'HH:MM'
    Return: durasi dalam jam (float)
    """
    from datetime import datetime

    format_waktu = "%H:%M"
    masuk = datetime.strptime(jam_masuk, format_waktu)
    keluar = datetime.strptime(jam_keluar, format_waktu)

    selisih = keluar - masuk
    durasi_jam = selisih.total_seconds() / 3600
    return durasi_jam


# DATA KENDARAAN YANG PARKIR
data_kendaraan = [
    {"jenis": "Mobil", "jam_masuk": "08:00", "jam_keluar": "10:00"},
    {"jenis": "Motor", "jam_masuk": "09:00", "jam_keluar": "11:00"},
]

print("=" * 55)
print("STRUK BIAYA PARKIR")
print("=" * 55)

# MEMPROSES SETIAP KENDARAAN
for kendaraan in data_kendaraan:
    jenis = kendaraan["jenis"]
    masuk = kendaraan["jam_masuk"]
    keluar = kendaraan["jam_keluar"]

    lama_parkir = hitung_durasi(masuk, keluar)
    total_biaya = hitung_biaya_parkir(jenis, lama_parkir)

    print(f"Jenis Kendaraan   : {jenis}")
    print(f"Jam Masuk         : {masuk}")
    print(f"Jam Keluar        : {keluar}")
    print(f"Lama Parkir       : {lama_parkir:.0f} jam")
    print(f"Total Biaya       : Rp{total_biaya:,}")
    print("-" * 55)