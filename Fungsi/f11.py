def hancurkancandi(candi : list)-> list:
    id_candi = int(input("Masukkan ID candi: "))
    for i in range(100):
        if candi[i]!=["0","0","0","0","0"] and  int(candi[i][0]) == id_candi: #mengecek apakah id candi valid
            konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? ").lower()
            if konfirmasi == "y":
                candi[i] = ["0","0","0","0","0"]
                print("\nCandi telah berhasil dihancurkan.")
                for x in range (99):#looping untuk mencari id candi yang dihancurkan dan menggeser candi yang disebelahnya
                    for y in range (99-i):
                        if candi[x+1]!=["0","0","0","0","0"] and candi[x]==["0","0","0","0","0"]:
                            candi[x+1][0]=str(int(candi[x+1][0])-1)#proses pengurangan
                            candi[x],candi[x+1]=candi[x+1],candi[x]#proses penggeseran
                return candi
            elif konfirmasi == "n":
                print("\nPenghancuran candi dibatalkan")
                return candi
            else:
                print("\nInput tidak valid.\n")
                return candi
    print("Tidak ada candi dengan ID tersebut.\n")
    return candi