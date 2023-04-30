def validasiPassword(password : str) ->bool: 
    if len(password)>=5 and len(password)<=25: #if untuk mengecek panjang password
        return True
    else: #jika panjang password tidak memenuhi
        print("Password panjangnya harus 5-25 karakter!") 
        return False
    
def validasiNama(namaJin : str,user_csv : list) -> tuple: #Fungsi untuk mengecek nama di dalam array user apakah sudah ada atau belum
    for i in range(102): #mengecek dalam array user apakah ada nama yang sama
        if user_csv[i]==["0","0","0"]:
            continue
        elif user_csv[i][0]==namaJin : #jika username sudah ada maka return False
            print(f"Username {namaJin} sudah diambil!")
            return False
    else: #jika tidak ada di dalam user maka return True
        return True
    
def hitungList(user_csv : list) -> int: #fungsi untuk menghitung array user sudah terisi berapa
    count=0 #inisialisasi
    for i in range (102): #for loop untuk mencari yang sudah berisi
        if user_csv[i] != ["0","0","0"]   :
            count+=1
    return count #return


def summonjin(user_csv : list) -> list:
    if hitungList(user_csv) >102 : #jika panjang list sudah melebihi 102
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        return user_csv
    else: #jika tidak melebihi 102
        print("Jenis jin yang dapat dipanggil :\n(1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n(2) Pembangun - Bertugas membangun candi")
        jenisJin=input("Masukkan nomor jenis jin yang ingin dipanggil : ") #input
        if jenisJin=="1":  #jika user memilih 1
            print("\nMemilih jin “Pengumpul”.")
            namaJin=input("Masukkan username jin : ") #input
            while validasiNama(namaJin,user_csv)==False : #memvalidasi nama 
                namaJin=input("Masukkan username jin : ")     
            password=input("Masukkan password jin : ") #input
            while validasiPassword(password)==False: #memvalidasi password
                password=input("Masukkan password jin : ")
            else: #jika password sudah benar
                print("\nMengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...\n")
                for i in range(102): #for loop untuk mengupdate array user
                    if user_csv[i]==["0","0","0"]: 
                        user_csv[i]=[namaJin,password,"jin_pengumpul"]
                        return user_csv
        elif jenisJin=="2": #jika user memilih 2
            print("\nMemilih jin “Pembangun”.")
            namaJin=input("Masukkan username jin : ") #input
            while validasiNama(namaJin,user_csv)==False : #memvalidasi nama
                namaJin=input("Masukkan username jin : ")     
            else:
                password=input("Masukkan password jin : ") #input
                while validasiPassword(password)==False: #memvalidasi password
                    password=input("Masukkan password jin : ")
                else:
                    print("\nMengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...\n")
                    for i in range(102): #for loop untuk mengupdate array user
                        if user_csv[i]==["0","0","0"]:
                            user_csv[i]=[namaJin,password,"jin_pembangun"]
                            return user_csv
        else: #jika tidak menerima input antara 1 atau 2
            print(f"\nTidak ada jenis jin bernomor \"{jenisJin}\"!\n")
            return user_csv
