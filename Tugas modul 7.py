pemakaian_kwh=int(input("Masukkan Jumlah Pemakaian (kwh)  : "))
golongan=int(input("Masukkan Golongan Tarif          : "))

def hitung_tagihan_listrik(pemakaian_kwh, golongan):
    if golongan == 1:
        tarif_pertama = 1500
        tarif_selanjutnya = 2000
    elif golongan == 2:
        tarif_pertama = 2500
        tarif_selanjutnya = 3000
    elif golongan == 3:
        tarif_pertama = 4000
        tarif_selanjutnya = 5000
    elif golongan == 4:
        tarif_pertama = 5000
        tarif_selanjutnya = 7000
    else:
        tarif_pertama = 4000
        tarif_selanjutnya = 5000

    if pemakaian_kwh <= 100:
        total = pemakaian_kwh * tarif_pertama
    else:
        total = 100 * tarif_pertama + (pemakaian_kwh - 100) * tarif_selanjutnya
    return total

print(f"Tagihan {pemakaian_kwh} kwh dengan golongan {golongan} : Rp {hitung_tagihan_listrik(pemakaian_kwh,golongan)}")