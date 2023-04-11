import Fungsi.CSV_Parser as parser

def validasiPassword(password):
    if parser.length(password)>=5 and parser.length(password)<=25:
        return True
    else:
        print("Password panjangnya harus 5-25 karakter!")
        return False
def validasiNama(namaJin,user_csv):
    for i in range(parser.length(user_csv)):
        if user_csv[i][0]==namaJin :
            print(f"Username {namaJin} sudah diambil!")
            return False
    else:
        return True
    
def hitungList(user_csv:list[str]):
    count=0
    for i in range (parser.length(user_csv)):
        if user_csv[i][0] != -1 :
            count+=1
    return count


def summonjin(user_csv:list[str]):
    if hitungList(user_csv) >102 :
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        print("Jenis jin yang dapat dipanggil :\n(1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n(2) Pembangun - Bertugas membangun candi")
        jenisJin=int(input("Masukkan nomor jenis jin yang ingin dipanggil : "))
        if jenisJin==1:
            print("\nMemilih jin “Pengumpul”.")
            namaJin=input("Masukkan username jin : ")
            while not validasiNama(namaJin,user_csv) :
                namaJin=input("Masukkan username jin : ")     
            else:
                password=input("Masukkan password jin : ")
                while not validasiPassword(password):
                    password=input("Masukkan password jin : ")
                else:
                    print("\nMengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...\n")
                    user_csv=parser.append(user_csv,[namaJin,password,"jin_pengumpul"])
                    return user_csv
        elif jenisJin==2:
            print("\nMemilih jin “Pengumpul”.")
            namaJin=input("Masukkan username jin : ")
            while not validasiNama(namaJin,user_csv) :
                namaJin=input("Masukkan username jin : ")     
            else:
                password=input("Masukkan password jin : ")
                while not validasiPassword(password):
                    password=input("Masukkan password jin : ")
                else:
                    print("\nMengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...\n")
                    user_csv=parser.append(user_csv,[namaJin,password,"jin_pembangun"])
                    return user_csv
        else:
            print(f"\nTidak ada jenis jin bernomor \"{jenisJin}\"!\n")
            return user_csv








# # while not valid :
# #             password=input("Masukkan password jin:")
# #             if not (parser.length(password)>=5 and parser.length(password)<=25): 
# #                 valid=True
