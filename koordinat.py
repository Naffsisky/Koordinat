      # Nama  : Prinafsika
      # NIM   : 21081010278

import pyfiglet
import numpy as np
import matplotlib.pyplot as plt

intro = pyfiglet.figlet_format("Koordinat", font = "standard")
intronama = pyfiglet.figlet_format('By : Naff', font = "slant")

print(intro)
print(intronama)
print('|--------------------------------------|')
print('| PERHITUNGAN KUADRAN DALAM KOORDINAT  |')
print('|--------------------------------------|')

x = int(input("Masukkan Koordinat X : "))
y = int(input("Masukkan Koordinat Y : "))

if (x >0 and y >0) :
    print("Koordinat anda berada pada : KUADRAN I")
elif(x <0 and y >0):
    print("Koordinat anda berada pada : KUADRAN II")
elif(x <0 and y <0):
    print("Koordinat anda berada pada : KUADRAN III");
elif(x >0 and y <0):
    print("Koordinat anda berada pada : KUADRAN IV")
elif(x ==0 and y ==0):
    print("Koordinat anda berada pada : TITIK PUSAT")

plt.scatter(x, y)
plt.scatter(0, 0)

plt.plot(-x,x and -y,y)
plt.show()