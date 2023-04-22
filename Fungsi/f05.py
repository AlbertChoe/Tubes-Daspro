def ubah (users):
    username= input("Masukkan username jin : ")
    counter = 0
    for i in range (102) :
        if users[i]!=[0,0,0] and (username == users[i][0]):
            counter = 1
            if (users[i][2]== "jin_pengumpul"):
                persetujuan=input("\nJin ini bertipe 'Pengumpul'. Yakin ingin mengubah ke tipe 'Pembangun' (Y/N)? ")
                if (persetujuan == "Y") or persetujuan=="y":
                    users[i][2] = "jin_pembangun"
                    print("Jin telah berhasil diubah.")
                    return users
                elif (persetujuan =="N") or persetujuan=="n":
                    print("Jin tidak jadi diubah")
                    return users
                else :
                    print("input invalid (Y/N)")  
                    return users              
            elif (users[i][2]== "jin_pembangun"):
                persetujuan=input("\nJin ini bertipe 'Pembangun'. Yakin ingin mengubah ke tipe 'Pengumpul' (Y/N)? ")
                if (persetujuan == "Y")or persetujuan=="y":
                    users[i][2] = "jin_pengumpul"
                    print("Jin telah berhasil diubah.")
                    return users
                elif (persetujuan =="N")or persetujuan=="n":
                    print ( "Jin tidak jadi diubah")
                    return users
                else :
                    print("input invalid (Y/N)")
                    return users
            else:
                print("id terdaftar namun bukan jin pengumpul maupun pembangun")
                return users
    if (counter == 0): # Jika username jin tidak tersedia
        print("Tidak ada jin dengan username tersebut.")
        return users
