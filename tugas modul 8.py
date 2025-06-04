FILE_NAME = "catatan.txt"

def tampilkan_menu():
    print("\n--- MENU UTAMA ---")
    print("1. Lihat catatan yang tersedia")
    print("2. Buat catatan baru")
    print("3. Exit")

def buat_catatan():
    judul = input("Masukkan judul catatan: ")
    isi = input("Masukkan isi catatan: ")
    simpan_catatan(judul, isi)
    print("Catatan berhasil disimpan.")

def simpan_catatan(judul, isi):
    with open(FILE_NAME, "a") as file:
        file.write(f"{judul}\n{isi}\n###\n")

def baca_catatan():
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.read().split("###\n")
            catatan = {}
            for entry in lines:
                if entry.strip():
                    bagian = entry.strip().split("\n", 1)
                    if len(bagian) == 2:
                        judul, isi = bagian
                        catatan[judul] = isi
            return catatan
    except FileNotFoundError:
        return {}

def lihat_catatan():
    catatan = baca_catatan()
    if not catatan:
        print("Tidak ada catatan yang tersedia.")
        return

    print("\nDaftar judul catatan:")
    for judul in catatan:
        print(f"- {judul}")

    pilihan = input("Masukkan judul catatan yang ingin dilihat: ")
    if pilihan in catatan:
        print(f"\nIsi catatan '{pilihan}':\n{catatan[pilihan]}")
    else:
        print("Data tidak ditemukan.")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == "1":
            lihat_catatan()
        elif pilihan == "2":
            buat_catatan()
        elif pilihan == "3":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

main()