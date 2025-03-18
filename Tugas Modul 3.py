n = int(input("Masukkan nilai n (Partisi) : "))
a = 1
b = 3
x_0 = 1
fx = 0 
delta_x = (b-a)/n
for a in range (n) :
    x_i =  x_0 + delta_x 
    x_0 = x_i
    fx_i = (x_i**2) + (2*x_i)
    fx = fx + fx_i
luas_daerah = fx * delta_x
print (f"Luas Daerah dari fungsi x^2+2x dengan batas daerah x=1 dan x=3 dan jumlah partisi n = {n} adalah {luas_daerah:.2f}")


