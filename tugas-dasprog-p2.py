# Menghitung keliling tabung = 2πr
# Menghitung volume tabung = πr²t
# Menghitung luas tabung = 2πr²

# Keterangan

# K = Keliling tabung (cm)
# L = Luas tabung (cm2)
# V = Volume tabung (cm3)
# π(phi) = 22/7 atau 3,14
# r = Jari-jari / setengah diameter (cm)
# t = Tinggi (cm)

phi = 3.14
r = int(input("Masukkan jari-jari tabung (cm) : "))
t = int(input("Masukkan tinggi tabung (cm) : "))

K = 2 * phi * r
V = phi * r * r * t
L = 2 * phi * r * r 

print(f"Keliling = {round(K)} cm")
print(f"Luas = {round(L)} cm2")
print(f"Volume = {round(V)} cm3")
