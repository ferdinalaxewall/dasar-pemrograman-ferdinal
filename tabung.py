#program menghitung tabung
from re import T


print("\n")
print("\t\tMenghitung Tabung")
print("\t\t--------------------")
r = int(input("Masukkan jari-jari tabung (cm) : ")) #variabel
t = int(input("Masukkan tinggi tabung (cm) : "))
phi = 3.14 #konstanta

keliling_alas = 2 * phi * r 
volume_tabung = phi * r * r * T
luas_tabung = 2 * phi * r * r 


print("\n")
print("keliling tabung adalah " +str(round(keliling_alas,)) + " cm")
print("luas tabung adalah " +str(round(volume_tabung,)) + " cm2")
print("volume tabung adalah " +str(round(luas_tabung,)) + " cm3")
