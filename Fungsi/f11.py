def hancurkancandi(candi):
    id_candi = input("Masukkan ID candi: ")
    for i in range(100):
        if candi[i][0] == id_candi:
            konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? ")
            if konfirmasi == "Y":
                candi[i] = [0,0,0,0,0]
                print("\nCandi telah berhasil dihancurkan.")
            else:
                print("\nPenghancuran candi dibatalkan")
            return candi
    print("Tidak ada candi dengan ID tersebut.")
    return candi