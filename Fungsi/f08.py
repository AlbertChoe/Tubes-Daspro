import Fungsi.f07 as f07 
import Fungsi.BonusRNG as RNG
def batchkumpul(users,bahan_bangunan):
    totalBahan=[0,0,0]
    totalJin=0
    valid=False
    for i in range (102):
        if users[i]!=0 and users[i][2]=="jin_pengumpul":
            valid=True
            break
    if valid:
        for i in range (102):
            if  users[i]!=[0,0,0] and users[i][2]=="jin_pengumpul":
                pasir,batu,air = RNG.RNGKumpul()  
                bahan_bangunan[0][2] =int(bahan_bangunan[0][2])+ pasir
                bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) +batu
                bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) +air
                totalJin+=1
                totalBahan[0]+=pasir
                totalBahan[1]+=batu
                totalBahan[2]+=air
        print(f"Mengerahkan {totalJin} jin untuk mengumpulkan bahan")
        print(f"Jin menemukan total {totalBahan[0]} pasir, {totalBahan[1]} batu, dan {totalBahan[2]} air.\n")
        return bahan_bangunan
    else:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.\n")
        return bahan_bangunan


#Bagian Bangun
# def validasiNama(username,jinBangun):
#     for i in range(100):
#         if jinBangun[i][0]==username :
#             return True,i
#     else:
#         return False,-1

def batchbangun (users,bahan_bangunan,candi):
    arrayRandom=[0 for i in range (100)]
    totalJin,totPasir,totBatu,totAir=0,0,0,0
    for i in range (102):
        if users[i][2]=="jin_pembangun":
            totalJin+=1
            pasir,batu,air=RNG.RNGBangun()
            arrayRandom[i]=[users[i][0],pasir,batu,air]
            totPasir+=pasir
            totBatu+=batu
            totAir+=air
    if totalJin==0: #jika tidak ada jin yang bisa bangun
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.\n")
        return bahan_bangunan,candi
    else:  #jika ada jin yang bisa bangun
        print(f"Mengerahkan {totalJin} jin untuk membangun candi dengan total bahan {totPasir} pasir, {totBatu} batu, dan {totAir} air")
        # mengecek jumlah bahan apakah cukup atau tidak
        print(arrayRandom)
        if totPasir<int(bahan_bangunan[0][2]) and totBatu<int(bahan_bangunan[1][2]) and totAir<int(bahan_bangunan[1][2]): 
            print(f"Jin berhasil membangun total {totalJin} candi\n")
            for i in range(totalJin):
                ArrayNumber=0
                for j in range (100):
                    if arrayRandom[j]!=0 :
                        ArrayNumber=j
                        break
                for j in range (100):
                    if candi[j]==[0,0,0,0,0]:
                        candi[j]=[j+1,arrayRandom[ArrayNumber][0],arrayRandom[ArrayNumber][1],arrayRandom[ArrayNumber][2],arrayRandom[ArrayNumber][3]]  
                        print(candi)
                        break  
                bahan_bangunan[0][2]=int(bahan_bangunan[0][2])-arrayRandom[ArrayNumber][1]            
                bahan_bangunan[1][2]=int(bahan_bangunan[1][2])-arrayRandom[ArrayNumber][2]            
                bahan_bangunan[2][2]=int(bahan_bangunan[2][2])-arrayRandom[ArrayNumber][3]  
                arrayRandom[ArrayNumber]=0                         
            return bahan_bangunan,candi
        #jika bahan tidak cukup
        else:
            print(f"Bangun gagal. Kurang {totPasir-int(bahan_bangunan[0][2])} pasir, {totBatu-int(bahan_bangunan[1][2])} batu, {totAir-int(bahan_bangunan[2][2])}")
            return bahan_bangunan,candi

            