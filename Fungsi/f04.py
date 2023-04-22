def validasiNama(namaJin,user):
    for i in range(102):
        if user[i]!=[0,0,0] and i!=0 and i!=1 and user[i][0]==namaJin  :
            return True,i
    else:
        return False,-1
    
def hapusjin(users):
    namaJin=input("Masukkan username jin : ")
    valid,index=validasiNama(namaJin,users)
    if valid:
        jawaban=input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
        if jawaban=="Y" or jawaban=="y":
            users[index]=[0,0,0]
            return users
        elif jawaban=="N" or jawaban=="n":
            print(f"Proses menghapus jin bernama {namaJin} dicancel oleh pengguna\n")
            return users
        else: 
            print("Input tidak valid")
            return users
    else:
        print("Tidak ada jin dengan username tersebut.\n")
        return users

