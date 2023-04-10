
def logout(role,username):
    if role==0 and username==0:
        print ("Logout gagal!\nAnda belum login , silahkan login terlebih dahulu sebelum melakukan logout")
        return role,username
    else:
        print("Keluar dari Akun...\nLogout Berhasil")
        role=0
        username=0
        return role,username
