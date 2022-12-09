import pandas as pd
from datetime import date

class Referensi:
    def __init__(self):
        self.data_kelas = ('Exclusive', 'Business', 'Economic')
        self.data_b = (185000, 285000, 275000) 
        self.data_s = (156000, 235000, 225000) 
        self.data_f = (110000, 190000, 185000)
    
    def tampilkan_referensi(self):
        referensi = {
            "Kelas" : self.data_kelas,
            "Bogowonto (B)" : self.data_b,
            "Senja Utama (S)" : self.data_s,
            "Fajar Utama (F)" : self.data_f
        }

        tabel_referensi = pd.DataFrame(referensi)

        print(self.garis())
        print("Tarif Kereta Jakarta - Yogyakarta".center(75))
        print(self.garis())
        print(tabel_referensi)
        print(self.garis())

    def ambil_data_kelas(self, index):
        return self.data_kelas[index]

    def ambil_data_b(self, index):
        return self.data_b[index]

    def ambil_data_s(self, index):
        return self.data_s[index]

    def ambil_data_f(self, index):
        return self.data_f[index]
    
    def garis(self, jumlah_garis = 75):
        return "="*jumlah_garis 

class Data(Referensi):
    data_nama = []
    data_kelas_pesanan = []
    data_jenis_kereta = []
    data_tarif = []
    data_penumpang = []
    data_jumlah_harga = []
    data_total_pendapatan = 0

    def __init__(self):
        super().__init__()
    
    def set_data(self, nama, kelas_pesanan, jenis_kereta, tarif, penumpang, jumlah_harga):
        self.data_nama.append(nama)
        self.data_kelas_pesanan.append(kelas_pesanan)
        self.data_jenis_kereta.append(jenis_kereta)
        self.data_tarif.append(tarif)
        self.data_penumpang.append(penumpang)
        self.data_jumlah_harga.append(jumlah_harga)
    
    def set_total_pendapatan(self):
        self.data_total_pendapatan = sum(self.data_jumlah_harga)

    def get_data(self):
        return {
            "Nama Pemesan" : self.data_nama,
            "Kelas" : self.data_kelas_pesanan,
            "Jenis Kereta" : self.data_jenis_kereta,
            "Tarif Per Seat" : self.data_tarif,
            "Jumlah Penumpang" : self.data_penumpang,
            "Total Harga" : self.data_jumlah_harga,
        }
    
    def tampilkan_data(self, tanggal):
        print("\n", self.garis(100), "\n")
        print("Data Pemesanan Kereta".center(100))
        print(f"\nTanggal : {tanggal}")
        print(self.garis(100))
        data = self.get_data()
        tabel_data = pd.DataFrame(data)
        print(tabel_data)
        print(self.garis(100))

        self.set_total_pendapatan()
        print(f"Total Pendapatan : Rp. {self.data_total_pendapatan}")
    
# Menampilkan Data Referensi dari Class Referensi
referensi = Referensi()
referensi.tampilkan_referensi()
data = Data()

# Validasi Form
def validasi_kelas_kereta(kelas):
    if((kelas > 0) & (kelas <= 3)):
        return referensi.data_kelas[kelas-1]
    else:
        raise ValueError('Kelas yang anda masukkan salah, tolong masukkan Kelas [1,2,3]')
        
def validasi_jenis_kereta(jenis, kelas):
    jenis = jenis.upper()
    if jenis == "B":
        return {
            "jenis" : "Bogowonto",
            "tarif" : referensi.data_b[kelas-1]
        }
    
    elif jenis == "S":
        return {
            "jenis" : "Senja Utama",
            "tarif" : referensi.data_s[kelas-1]
        }
        
    elif jenis == "F":
        return {
            "jenis" : "Fajar Utama",
            "tarif" : referensi.data_f[kelas-1]
        }
    else:
        raise ValueError('Jenis Kereta yang anda masukkan salah, tolong masukkan Jenis Kereta [B/S/F]')

def form_input(i, jumlah_data):
    try:
        print(referensi.garis())
        print(f"Data Ke - {i+1}")

        nama = input("Nama Pemesan : ")
        input_kelas = int(input("Pilih Kelas [1/2/3] : "))
        kelas = validasi_kelas_kereta(input_kelas)
        input_jenis = input("Pilih Jenis Kereta [B/S/F] : ")
        jenis = validasi_jenis_kereta(input_jenis, input_kelas)
        tarif = jenis['tarif']
        penumpang = int(input("Jumlah Penumpang : "))
        jumlah_harga = tarif * penumpang

        data.set_data(nama, kelas, jenis['jenis'], tarif, penumpang, jumlah_harga)
    except ValueError:
        print(ValueError('Input yang anda masukkan salah, mohon mulai dari awal'))
        form_input(i, jumlah_data)

# Form Pengisian Data
print("Form Penginputan Data".center(75))
tanggal_input = f"Tanggal Input : {date.today().strftime('%d %B %Y')}"
print(tanggal_input)
jumlah_data = int(input("Jumlah Data : "))

for i in range(jumlah_data):
    form_input(i, jumlah_data)

data.tampilkan_data(date.today().strftime('%d %B %Y'))