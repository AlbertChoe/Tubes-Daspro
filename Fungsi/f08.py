import Fungsi.f07 as f07 
import Fungsi.BonusRNG as RNG
def batchkumpul(users : list , bahan_bangunan : list) -> list:
    #Inisialisasi
    totalBahan=[0,0,0] #array untuk menampung total bahan yang sudah dikumpul
    totalJin=0
    valid=False
    for i in range (102):
        if users[i]!=0 and users[i][2]=="jin_pengumpul": #untuk mengecek apakah ada jin pengumpul di dalam array user
            valid=True #jika ada maka valid=True
            break
    if valid: #jika ada jin pengumpul
        for i in range (102): #for loop untuk mencari indeks jin pengumpul  
            if  users[i]!=[0,0,0] and users[i][2]=="jin_pengumpul":
                pasir,batu,air = RNG.RNGKumpul()  # assign hasil random number ke variable 
                bahan_bangunan[0][2] =int(bahan_bangunan[0][2])+ pasir #menambah pasir ke dalam array bahan bangunan
                bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) +batu #menambah batu ke dalam array bahan bangunan
                bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) +air #menambah air ke dalam array bahan bangunan
                totalJin+=1 #menambah total jin

                #menghitung total bahan yang sudah ditemukan
                totalBahan[0]+=pasir  
                totalBahan[1]+=batu
                totalBahan[2]+=air
        print(f"Mengerahkan {totalJin} jin untuk mengumpulkan bahan")
        print(f"Jin menemukan total {totalBahan[0]} pasir, {totalBahan[1]} batu, dan {totalBahan[2]} air.\n")
        return bahan_bangunan #mengembalikan array bahan bangunan yang sudah diupdate
    else: #jika tidak ada jin pengumpul
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.\n")
        return bahan_bangunan #mengembalikan array bahan bangunan


#Bagian Bangun
def batchbangun (users : list , bahan_bangunan :  list, candi : list) -> tuple:
    #Inisialisasi
    arrayRandom=[0 for i in range (100)] #array sementara untuk menampung data data dan digunakan untuk mengecek apakah bahan bangunan yang dibutuhkan cukup (100 indeks karena maksimal candi yang bisa dibangun hanya 100)
    totalJin,totPasir,totBatu,totAir=0,0,0,0
    for i in range (102): #untuk mengecek apakah ada jin pembangun di dalam array user
        if users[i][2]=="jin_pembangun": #Jika ada maka
            totalJin+=1 #menambah total jin
            pasir,batu,air=RNG.RNGBangun() #assign hasil random number ke variable
            arrayRandom[i]=[users[i][0],pasir,batu,air] #assign nama dari jin pembangun , pasir, batu, dan air yang dibutuhkan untuk membangun suatu candi

            #Menghitung total bahan yang dibutuhkan
            totPasir+=pasir
            totBatu+=batu
            totAir+=air
    if totalJin==0: #jika tidak ada jin yang bisa bangun
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.\n")
        return bahan_bangunan,candi #mengembalikan array bahan bangunan dan candi
    else:  #jika ada jin yang bisa bangun
        print(f"Mengerahkan {totalJin} jin untuk membangun candi dengan total bahan {totPasir} pasir, {totBatu} batu, dan {totAir} air")
        if totPasir<int(bahan_bangunan[0][2]) and totBatu<int(bahan_bangunan[1][2]) and totAir<int(bahan_bangunan[1][2]): # mengecek jumlah bahan apakah cukup atau tidak
            print(f"Jin berhasil membangun total {totalJin} candi\n")
            for i in range(totalJin): # for loop dengan jumlah jin pembangun yang ada 
                ArrayNumber=0 #inisialisasi untuk mencatat indeks
                for j in range (100): #mengecek semua kemungkinan dari candi yang bisa dibuat
                    if arrayRandom[j]!=0 : #jika indeks ke i tidak sama dengan 0 maka ada candi yang dibangun
                        ArrayNumber=j # assign indeks ke dalam variable
                        break #jika sudah menemukan indeks yang bukan 0 maka break
                for j in range (100): #for loop untuk mengecek semua indeks candi yang masih kosong 
                    if candi[j]==[0,0,0,0,0]: #jika kosong maka akan dibangun candi yang baru, jika sudah penuh maka candi tidak akan dibangun 
                        candi[j]=[j+1,arrayRandom[ArrayNumber][0],arrayRandom[ArrayNumber][1],arrayRandom[ArrayNumber][2],arrayRandom[ArrayNumber][3]]  # mengganti data candi yang kosong menjadi data candi baru
                        break  #setelah mengganti data candi maka keluar
                
                #mengurang bahan bangunan dari setiap candi, baik candi yang dicatat dalam array candi maupun yang tidak dicatat dalam array candi (Karena jika bahan bangunan mencukupi tetapi candi yang dibangun sudah 100, candi akan tetap berhasil dibangun sehingga bahan bangunan akan tetap dikurang)
                bahan_bangunan[0][2]=int(bahan_bangunan[0][2])-arrayRandom[ArrayNumber][1]            
                bahan_bangunan[1][2]=int(bahan_bangunan[1][2])-arrayRandom[ArrayNumber][2]            
                bahan_bangunan[2][2]=int(bahan_bangunan[2][2])-arrayRandom[ArrayNumber][3]  
                arrayRandom[ArrayNumber]=0 #mengganti array random sesuai dengan indeks yang dicari sebelumnya agar menjadi 0 sehingga dalam pencarian selanjutnya tidak terdeteksi kembali   
            return bahan_bangunan,candi #mengembalikan array bahan bangunan dan candi yang sudah diupdate
        else: #jika bahan tidak cukup
            #menghitung setiap bahan yang kurang 
            kurangpasir=totPasir-int(bahan_bangunan[0][2]) 
            kurangbatu=totBatu-int(bahan_bangunan[1][2])
            kurangair=totAir-int(bahan_bangunan[2][2])
            if kurangpasir<0 : #Jika bahan lebih kecil dari 0 maka bahan bangunan yang dimiliki lebih banyak 
                kurangpasir=0
            if kurangbatu<0 : #Jika bahan lebih kecil dari 0 maka bahan bangunan yang dimiliki lebih banyak
                kurangbatu=0
            if kurangair<0 : #Jika bahan lebih kecil dari 0 maka bahan bangunan yang dimiliki lebih banyak
                kurangair=0
            print(f"Bangun gagal. Kurang {kurangpasir} pasir, {kurangbatu} batu, {kurangair} air.\n")
            return bahan_bangunan,candi #mengembalikan array bahan bangunan dan candi yang sudah diupdate

            