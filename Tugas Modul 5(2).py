no_pelanggan = []
nama_pelanggan = []
total_belanja = []

while True:
    print("\nMenu Utama")
    print("\n1. Update Data")
    print("2. Hapus Data")
    print("3. Cetak Data")
    print("4. Keluar")
    pilih = input("\nPilihan menu (1-4): ")

    if pilih == '1':
        print("\nTambah Data Pelanggan")
        no = input("No Pelanggan: ")
        nama = input("Nama Pelanggan: ")
        belanja = int(input("Masukkan Total Belanja: "))

        no_pelanggan.append(no)
        nama_pelanggan.append(nama)
        total_belanja.append(belanja)

        print("\nData berhasil ditambahkan!")

    elif pilih == '2':
        print("\nHapus Data Pelanggan")
        no = input("Masukkan No Pelanggan yang akan dihapus: ")
        if no in no_pelanggan:
            index = no_pelanggan.index(no)
            no_pelanggan.pop(index)
            nama_pelanggan.pop(index)
            total_belanja.pop(index)
            print("Data berhasil dihapus.\n")
        else:
            print("\nData tidak ditemukan.")

    elif pilih == '3':
        print("\nData Pelanggan")
        if len(no_pelanggan) == 0:
            print("Belum ada data.\n")
        else:
            print("No Pelanggan" + "    " + "Nama Pelanggan" + "   " + "Total Belanja")
            for i in range(len(no_pelanggan)):
                print(f"{no_pelanggan[i]}               {nama_pelanggan[i]}            Rp{total_belanja[i]}")
            print()

    elif pilih == '4':
        print("Terima kasih. Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")