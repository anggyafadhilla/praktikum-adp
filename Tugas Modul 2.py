nama_barang = str(input("Nama Barang      : "))
kuantitas = int(input("Kuantitas        : "))
if nama_barang=="Kemeja" :
    harga_satuan = 80000
elif nama_barang=="Celana" :
    harga_satuan = 65000
elif nama_barang=="Jaket" :
    harga_satuan = 60000
elif nama_barang=="Rok" :
    harga_satuan = 55000
elif nama_barang=="Jilbab Pashmina" :
    harga_satuan = 50000
elif nama_barang=="Blouse" :
    harga_satuan = 55000
elif nama_barang=="Leging" :
    harga_satuan = 50000
elif nama_barang=="Sendal" :
    harga_satuan = 75000
elif nama_barang=="Dasi" :
    harga_satuan = 85000
elif nama_barang=="Baju Kaos" :
    harga_satuan = 90000
harga_total = kuantitas*harga_satuan
if harga_total < 1000000 :
    potongan_harga = 0
elif 1000000 <= harga_total <= 1500000 :
    potongan_harga = harga_total*0.1
elif harga_total>1500000 :
    potongan_harga = harga_total*0.15
total_bayar = harga_total-potongan_harga
print("Harga Satuan     : Rp.",harga_satuan)
print("Harga Total      : Rp.",harga_total)
print("Potongan Harga   : Rp.",potongan_harga)
print("Total Bayar      : Rp.",total_bayar)

