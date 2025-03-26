n = int(input("Masukkan Jumlah Pendaftar : "))
for i in range (1,n+1) :
    n+1==True
    print(f"Input Data Pendaftar {i}")
    nama=input("Nama : ")
    matkul=input("Mata Kuliah : ")
    v=0
    while v <= 0 :
        wawancara = float(input("Hasil Penilaian Wawancara (Rentang nilai 1-100) : "))
        if 0<= wawancara <=100 :
            v+=1
        else :
            print("Inputkan ulang nilai anda")
 
    w=0
    while w <= 0 :
        tes_tulis= float(input("Penilaian Test Tulis (Rentang nilai 1-100) : "))
        if 0<= tes_tulis <=100 :
            w+=1
        else :
            print("Inputkan ulang nilai anda")
    x=0 
    while x <= 0 :
        mengajar= float(input("Penilaian Menngajar (Rentang nilai 1-100) :"))
        if 0<= mengajar <=100 :
            x+=1
        else :
            print("Inputkan ulang nilai anda")
    n+2==False
    nilai=0
    nilai += (wawancara + tes_tulis + mengajar) / 3
    print (f"Rata rata nilai pendaftar : {nilai}")
    if nilai > 80 :
        print("Prediket : Lulus")
    else : 
        print("Prediket : Tidak Lulus" )
    print (" ")
