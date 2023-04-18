import Fungsi.CSV_Parser as parser
import Fungsi.f07 as f07 
import Fungsi.BonusRNG as RNG
def batchkumpul(users,bahan_bangunan):
    totalBahan=[0,0,0]
    totalJin=0
    for i in range (parser.length(users)):
        if users[i][2]=="jin_pengumpul":
            pasir,batu,air = RNG.RNGKumpul()  
            bahan_bangunan[1][2] =int(bahan_bangunan[1][2])+ pasir
            bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) +batu
            bahan_bangunan[3][2] = int(bahan_bangunan[3][2]) +air
            totalJin+=1
            totalBahan[0]+=pasir
            totalBahan[1]+=batu
            totalBahan[2]+=air
        if i==(parser.length(users))-1:
            print(f"Mengerahkan {totalJin} jin untuk mengumpulkan bahan")
            print(f"Jin menemukan total {totalBahan[0]} pasir, {totalBahan[1]} batu, dan {totalBahan[2]} air.\n")
            return bahan_bangunan
    else:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.\n")
        return bahan_bangunan


#Bagian Bangun
def validasiNama(username,jinBangun):
    for i in range(parser.length(jinBangun)):
        if jinBangun[i][0]==username :
            return True,i
    else:
        return False,-1



def batchbangun (users,jinBangun,bahan_bangunan,candi):
    arrayRandom=[]
    totalJin,totPasir,totBatu,totAir=0,0,0,0
    for i in range (parser.length(users)):
        if users[i][2]=="jin_pembangun":
            totalJin+=1
            pasir,batu,air=RNG.RNGBangun()
            arrayRandom=parser.append(arrayRandom,[users[i][0],pasir,batu,air])
            totPasir+=pasir
            totBatu+=batu
            totAir+=air
    if parser.length(arrayRandom)==0: #jika tidak ada jin yang bisa bangun
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.\n")
        return jinBangun,bahan_bangunan,candi
    else:  #jika ada jin yang bisa bangun
        print(f"Mengerahkan {totalJin} jin untuk membangun candi dengan total bahan {totPasir} pasir, {totBatu} batu, dan {totAir} air")
        # mengecek jumlah bahan apakah cukup atau tidak
        if totPasir<int(bahan_bangunan[1][2]) and totBatu<int(bahan_bangunan[2][2]) and totAir<int(bahan_bangunan[3][2]): 
            print(f"Jin berhasil membangun total {totalJin} candi\n")
            for i in range(parser.length(arrayRandom)):
                valid,index=validasiNama(arrayRandom[i][0],jinBangun) #mencari dan mencatat index dari jin pembangun di array jinBangun untuk mencatat jumlah candi yang dibangun oleh jin ini
                if valid:
                    jinBangun[index][1]+=1  #jika jin ini sudah pernah membangun candi
                else:
                    jinBangun=parser.append(jinBangun,[arrayRandom[i][0],1]) #jika jin ini belum pernah membangun candi
                #Proses mencatat ke dalam candi
                if parser.length(candi)==1: #jika belum ada candi yang pernah dibangun maka ditambah candi baru
                    candi=parser.append(candi,[1,arrayRandom[i][0],arrayRandom[i][1],arrayRandom[i][2],arrayRandom[i][3]])
                else: #jika sudah pernah ada jin candi yang dibangun
                    count=1 #untuk mencatat id dari candi
                    for j in range (1,parser.length(candi)): 
                        if candi[j][0]==(-1): #untuk mengganti id candi yang sudah dihancurkan menjadi id yang baru(di tengah tengah kosong)
                            candi[j][0],candi[j][1],candi[j][2],candi[j][3],candi[j][4]=j,arrayRandom[i][0],arrayRandom[i][1],arrayRandom[i][2],arrayRandom[i][3]
                            count=0
                            break
                        count+=1
                    else: #untuk mencatat jin baru jika sudah tidak ada yang candi yang dihancurkan 
                        candi=parser.append(candi,[count,arrayRandom[i][0],arrayRandom[i][1],arrayRandom[i][2],arrayRandom[i][3]])
                        count=1
                bahan_bangunan[1][2]=int(bahan_bangunan[1][2])-arrayRandom[i][1]            
                bahan_bangunan[2][2]=int(bahan_bangunan[2][2])-arrayRandom[i][2]            
                bahan_bangunan[3][2]=int(bahan_bangunan[3][2])-arrayRandom[i][3]            
            return jinBangun,bahan_bangunan,candi
        #jika bahan tidak cukup
        else:
            print(f"Bangun gagal. Kurang {totPasir-int(bahan_bangunan[1][2])} pasir, {totBatu-int(bahan_bangunan[2][2])} batu, {totAir-int(bahan_bangunan[3][2])}")
            return jinBangun,bahan_bangunan,candi

            