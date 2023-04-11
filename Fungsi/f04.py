import Fungsi.CSV_Parser as parser
def validasiNama(namaJin,user):
    for i in range(parser.length(user)):
        if user[i][0]==namaJin and i!=0 and i!=1 and i!=2 :
            return True,i
    else:
        return False,-1
    
def hapusjin(users):
    namaJin=input("Masukkan username jin : ")
    valid,index=validasiNama(namaJin,users)
    if valid:
        jawaban=input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
        if jawaban=="Y" or jawaban=="y":
            users[index][0],users[index][1],users[index][2]= -1,-1,-1
            return users
        else:
            print(f"Proses menghapus jin bernama {namaJin} dicancel oleh pengguna\n")
            return users
    else:
        print("Tidak ada jin dengan username tersebut.\n")
        return users

