persamaan = int(input("Masukkan jumlah persamaan (2/3) : "))
variabel = int(input("Masukkan jumlah variabel (1/2/3): "))

if persamaan != variabel:
    if persamaan > variabel:
        print("SPL tidak memiliki, (lebih banyak persamaan dari variabel).")
    else:
        print("SPL memiliki banyak solusi (tak hingga), (lebih banyak variabel dari persamaan).")
else:
    A = []
    B = []

    print(f"Masukkan koefisien dan konstanta dari {persamaan} persamaan   :")
    for i in range(persamaan):
        row = []
        for j in range(variabel):
            row.append(float(input(f"Koefisien x{j+1} di persamaan {i+1}: ")))
        A.append(row)
        B.append(float(input(f"Konstanta di persamaan {i+1}   : ")))

    if variabel == 2:
        detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    elif variabel == 3:
        detA = (A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
              - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
              + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]))
    else:
        print("Jumlah variabel tidak didukung.")

    if detA == 0:
        print("Determinan 0: SPL tidak memiliki solusi unik.")
    else:
        hasil = []
        for i in range(variabel):
            Ai = []
            for j in range(persamaan):
                baris = A[j][:]
                baris[i] = B[j]
                Ai.append(baris)
            if variabel == 2:
                detAi = Ai[0][0]*Ai[1][1] - Ai[0][1]*Ai[1][0]
            else:
                detAi = (Ai[0][0]*(Ai[1][1]*Ai[2][2] - Ai[1][2]*Ai[2][1])
                       - Ai[0][1]*(Ai[1][0]*Ai[2][2] - Ai[1][2]*Ai[2][0])
                       + Ai[0][2]*(Ai[1][0]*Ai[2][1] - Ai[1][1]*Ai[2][0]))
            hasil.append(detAi / detA)

        print("SPL memiliki solusi tunggal, Solusi SPL:")
        for i in range(variabel):
            print(f"x{i+1} = {hasil[i]}")