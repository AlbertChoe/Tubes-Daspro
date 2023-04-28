def laporanjin(user : list, bahan : list , candi : list) -> None:
    totJinkumpul,totJinBangun=0,0 #Inisialisasi
    for i in range(102): #mencari setiap jin dalam array user
        if user[i][2]=="jin_pengumpul" :
            totJinkumpul+=1 #jika menemukan jin pembangun maka ditambah
        elif user[i][2]=="jin_pembangun":
            totJinBangun+=1 #jika menemukan jin pembangun maka ditambah
    print(f"> Total Jin: {totJinBangun+totJinkumpul}")
    print(f"> Total Jin Pengumpul: {totJinkumpul}")
    print(f"> Total Jin Pembangun: {totJinBangun}")
    totjin=[0 for i in range (100)] #inisialisasi total jin karena maksimal jin hanya 100 (array sementara untuk menampung namajin dan total candi yang dibuat setiap jin)
    for i in range(100): #for loop untuk mencari candi yang kosong
        if candi[i]!=[0,0,0,0,0]: #jika kosong
            for j in range (100): #for loop untuk mencari username jin
                if totjin[j]!=0 and totjin[j][0]==candi[i][1]: #jika username jin pembangun dari candi sesuai dengan username jin yang dicari sekarang
                    totjin[j][1]+=1 #total candi yang sudah dibangun oleh jin tersebut ditambah 1
                    break #keluar
            else:  #jika tidak menemukan username jin yang diinginkan
                for j in range(100): #for loop untuk mencari tempat yang masih kosong
                    if totjin[j]==0: 
                        totjin[j]=[candi[i][1],1] #mengganti data yang masih kosong menjadi nama jin yang dicari
                        break #keluar
    for i in range (100): #for loop untuk mengecek apakah ada candi yang sudah dibangun
        if totjin[i]!=0:
            dibangun=True
            break 
    else:dibangun=False #jika tidak ada candi yang dibangun
    if dibangun : #jika ada candi yang dibangun 
        #inisialisasi
        max=totjin[0][1] 
        min=totjin[0][1]
        jumlahmax=0
        jumlahmin=0
        for i in range(100): #for loop untuk mencari maksimal dan minimal candi dari setiap candi yang dibuat
            if totjin[i]!=0 :
                if max<totjin[i][1]: #jika lebih besar dari nilai maksimum
                    max=totjin[i][1] #mengupdate kembali
                    jumlahmax=0  #inisialisasi ulang
                if min>totjin[i][1]: #jika lebih kecil dari nilai maksimum
                    min=totjin[i][1] #mengupdate kembali
                    jumlahmin=0 #inisialisasi ulang
                if min==totjin[i][1]: #jika menemukan nama jin yang sama
                    jumlahmin+=1 #mengupdate kembali
                if max==totjin[i][1]: #jika menemukan nama jin yang sama
                    jumlahmax+=1#mengupdate kembali

        if jumlahmax==0: #jika jin hanya 1
            for i in range (100):
                if totjin[i][1]==max:
                    terendah=totjin[i][0] 
                    break
        else: #jika jin lebih dari 1
            for i in range (100):
                if totjin[i]!=0 and  max==totjin[i][1] :
                    terendah=totjin[i][0]
                    break
            for i in range (100): #for loop untuk menentukan urutan leksikografis
                if totjin[i]!=0 and  max==totjin[i][1] and totjin[i][0]<terendah:
                    terendah=totjin[i][0]   
        if jumlahmin==0: #jika jin hanya 1
            for i in range (100):
                if totjin[i][1]==min:
                    tertinggi=totjin[i][0] 
                    break
        else: #jika jin lebih dari 1
            for i in range (100):
                if totjin[i]!=0 and  min==totjin[i][1] :
                    tertinggi=totjin[i][0]
                    break
            for i in range (100): #for loop untuk menentukan urutan leksikografis
                if totjin[i]!=0 and  min==totjin[i][1] and totjin[i][0]>tertinggi:
                    tertinggi=totjin[i][0]      
        print(f"> Jin Terajin: {terendah}") #output
        print(f"> Jin Termalas: {tertinggi}") #output
    else: #jika tidak ada jin yang dibangun
        print(f"> Jin Terajin: -") #output
        print(f"> Jin Termalas: -") #output
    print(f"> Jumlah Pasir: {bahan[0][2]} unit") #output
    print(f"> Jumlah Air: {bahan[1][2]} unit") #output
    print(f"> Jumlah Batu: {bahan[2][2]} unit\n") #output
    
