def validasiNama(namaJin,user):
    for i in range(102):
        if user[i]!=[0,0,0] and i!=0 and i!=1 and user[i][0]==namaJin  :
            return True,i
    else:
        return False,-1
    
def hapusjin(users,candi):
    namaJin=input("Masukkan username jin : ")
    valid,index=validasiNama(namaJin,users)
    times=0
    if valid:
        jawaban=input(f"Apakah anda yakin ingin menghapus jin dengan {namaJin}  (Y/N)? ")
        if jawaban=="Y" or jawaban=="y":
            users[index]=[0,0,0]
            for i in range (100):
                if candi[i][1]==namaJin:
                    candi[i]=[0,0,0,0,0]
                    times+=1
            print(candi)
            for x in range (times):
                for i in range (99):
                    for j in range (99-i):
                        if candi[i+1]!=[0,0,0,0,0] and candi[i]==[0,0,0,0,0]:
                            candi[i+1][0]=int(candi[i+1][0])-1
                            candi[i],candi[i+1]=candi[i+1],candi[i]
            print(candi)
            return users,candi
        elif jawaban=="N" or jawaban=="n":
            print(f"Proses menghapus jin bernama {namaJin} dicancel oleh pengguna\n")
            return users,candi
        else: 
            print("Input tidak valid")
            return users,candi
    else:
        print("Tidak ada jin dengan username tersebut.\n")
        return users,candi

