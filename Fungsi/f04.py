def validasiNama(namaJin : str, user :list ) -> tuple: #untuk mengecek nama dalam user list
    for i in range(102):
        if user[i]!=["0","0","0"] and i!=0 and i!=1 and user[i][0]==namaJin  :
            return True,i
    else:
        return False,-1
    
def hapusjin(users : list, candi : list) -> tuple:
    namaJin=input("Masukkan username jin : ")
    valid,index=validasiNama(namaJin,users)
    times=0
    if valid:
        jawaban=input(f"Apakah anda yakin ingin menghapus jin dengan {namaJin}  (Y/N)? ")
        if jawaban=="Y" or jawaban=="y":
            users[index]=["0","0","0"]
            for i in range (100): #looping untuk mencari berapa candi yang dibuat oleh jin tersebut
                if candi[i][1]==namaJin:
                    candi[i]=["0","0","0","0","0"] 
                    times+=1
            for x in range (times):
                for i in range (99):# looping untuk menghapus candi yang dibuat dan menggeser candi yang berada di sebelahnya 
                    for j in range (99-i):
                        if candi[i+1]!=["0","0","0","0","0"] and candi[i]==["0","0","0","0","0"]: 
                            candi[i+1][0]=str(int(candi[i+1][0])-1)#proses pengurangan id candi
                            candi[i],candi[i+1]=candi[i+1],candi[i]#proses penggeseran
            print(f"Jin telah berhasil dihapus dari alam gaib.\n")
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

