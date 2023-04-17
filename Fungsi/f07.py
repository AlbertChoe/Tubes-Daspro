import random

def ubah ():
    if username[2] != "bandung_bondowoso":
        print("Hanya dapat diakses oleh bandung bondowoso")
        return None
    username= input("Masukkan username jin : ")
    counter = 0
    for i in range (len(users)) :
        if (username == users[i][0]):
            counter = 1
            if (users[i][2]== "jin_pengumpul"):
                print("")
                print ("Jin ini bertipe 'Pengumpul'. Yakin ingin mengubah ke tipe 'Pembangun' (Y/N)?" )
                persetujuan = input()
                if (persetujuan == "Y"):
                    users[i][2] = "jin_pembangun"
                    print("Jin telah berhasil diubah.")
                    break
                elif (persetujuan =="N"):
                    print("Jin tidak jadi diubah")
                    break
                else :
                    print("input invalid (Y/N)")  
                    break              
            elif (users[i][2]== "jin_pembangun"):
                print("")
                print ("Jin ini bertipe 'Pembangun'. Yakin ingin mengubah ke tipe 'pengumpul' (Y/N)?" )
                persetujuan = input()
                if (persetujuan == "Y"):
                    users[i][2] = "jin_pengumpul"
                    print("Jin telah berhasil diubah.")
                    break
                elif (persetujuan =="N"):
                    print ( "Jin tidak jadi diubah")
                    break
                else :
                    print("input invalid (Y/N)")
                    break
            else:
                print("id terdaftar namun bukan jin pengumpul maupun pembangun")
    if (counter == 0): # Jika username jin tidak tersedia
        print("Tidak ada jin dengan username tersebut.")