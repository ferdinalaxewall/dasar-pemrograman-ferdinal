import pandas as pd

# Data
list_kelas = ("Exclusive", "Business", "Economic") 
list_b = (185000, 285000, 275000) 
list_s = (156000, 235000, 225000) 
list_f = (110000, 190000, 185000)
list_nama_pemesan = []
list_kelas_pesanan = []
list_jenis_kereta = []
list_tarif = []
list_penumpang = []
list_currency_total_harga = []
list_total_harga = []
total_pendapatan = 0

# Functions
def divider(sum):
    return "=" * sum

def currencyFormat(number):
    return "Rp. {:,},-".format(number)

def validasiKelas(kelas):
    if((kelas > 0) & (kelas <= 3)):
        return list_kelas[kelas-1]
    else:
        input_kelas = int(input(f"Mohon Pilih Kelas [1 - 3] : "))
        return validasiKelas(input_kelas)

def validasiJenisKereta(jenis, kelas):
    jenis = jenis.upper()
    if jenis == "B":
        return {
            "jenis" : "Bogowonto",
            "tarif" : list_b[kelas-1]
        }
    
    elif jenis == "S":
        return {
            "jenis" : "Senja Utama",
            "tarif" : list_s[kelas-1]
        }
        
    elif jenis == "F":
        return {
            "jenis" : "Fajar Utama",
            "tarif" : list_f[kelas-1]
        }
    else:
        input_jenis = input("Mohon Pilih Jenis Kereta [B/S/F] : ")
        return validasiJenisKereta(input_jenis, kelas)

def validasiPenumpang(penumpang):
    if(penumpang > 0):
        return penumpang
    else:
        print("Jumlah Penumpang Minimal 1!")
        input_penumpang = int(input("Jumlah Penumpang : "))
        return validasiPenumpang(input_penumpang)

def addPadIntoColumn(array_key, ref):
    for key in array_key:
        ref[key] = ref[key].str.pad(20, side='left')

# Menampilkan Data Referensi ke DataFrame Pandas
tarif = {
    "Kelas" : list_kelas,
    "Bogowonto (B)" : list_b,
    "Senja Utama (S)" : list_s,
    "Fajar Utama (F)" : list_f
}

data_tarif = pd.DataFrame(tarif).set_index('Kelas')
data_tarif[['Bogowonto (B)', 'Senja Utama (S)', 'Fajar Utama (F)']] = data_tarif[['Bogowonto (B)', 'Senja Utama (S)', 'Fajar Utama (F)']].apply(
    lambda series: series.apply(lambda value: currencyFormat(value))
)

print(divider(50))
print(data_tarif)
print(divider(50))

print("Tarif Kereta Jakarta - Yogyakarta \n")

# Form Pengisian Data
jumlah_data = int(input("Jumlah Data : "))
tanggal_input = input("Tanggal Input : ")

# Form akan ditampilkan sesuai dengan jumlah data yang di inputkan
for i in range(jumlah_data):
    print(divider(50))
    print(f"Data Ke-{i+1}")

    # Input Nama Pemesan
    list_nama_pemesan.append(input("Nama Pemesan : "))
    
    # Input Kelas Kereta
    kelas = int(input(f"Pilih Kelas [1 - 3] : "))
    list_kelas_pesanan.append(validasiKelas(kelas))

    # Input Jenis Kereta
    jenis = input("Pilih Jenis Kereta [B/S/F] : ")
    harga = validasiJenisKereta(jenis, kelas)['tarif']

    list_jenis_kereta.append(validasiJenisKereta(jenis, kelas)['jenis'])
    list_tarif.append(currencyFormat(harga))

    # Input Jumlah Penumpang    
    jumlah_penumpang = int(input("Jumlah Penumpang : "))
    list_penumpang.append(validasiPenumpang(jumlah_penumpang))

    # Total Harga
    list_total_harga.append(harga * validasiPenumpang(jumlah_penumpang))
    list_currency_total_harga.append(currencyFormat(harga * validasiPenumpang(jumlah_penumpang)))

# Menghitung Jumlah Pendapatan Per-Hari
for j in range(jumlah_data):
    total_pendapatan += list_total_harga[j]

# Menapilkan Data Pemesanan Kereta ke DataFrame Pandas
data_pemesanan_kereta = {
    "Nama Pemesan" : list_nama_pemesan,
    "Kelas Kereta" : list_kelas_pesanan,
    "Jenis Kereta" : list_jenis_kereta,
    "Jenis Kereta" : list_jenis_kereta,
    "Tarif Per Seat" : list_tarif,
    "Jumlah Penumpang" : list_penumpang,
    "Total Harga" : list_currency_total_harga
}

data_pemesanan = pd.DataFrame(data_pemesanan_kereta)
addPadIntoColumn(['Nama Pemesan', 'Kelas Kereta', 'Jenis Kereta', 'Tarif Per Seat', 'Total Harga'], data_pemesanan)
data_pemesanan.index += 1

print(f"\n\n Tanggal : {tanggal_input}")
print(divider(125))
print(data_pemesanan)
print(divider(125))
print(f"Total Pendapatan per-hari : {currencyFormat(total_pendapatan)} \n")    
