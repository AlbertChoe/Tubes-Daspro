def logout(role : str ,username :str) ->tuple:
    if role=="0" and username=="0":
        print ("Logout gagal!\nAnda belum login , silahkan login terlebih dahulu sebelum melakukan logout")
    else:
        print("Keluar dari Akun...\nLogout Berhasil")
        role,username="0","0"
        
    return role,username
