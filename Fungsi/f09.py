def laporanjin(user,bahan,candi):
    totJinkumpul,totJinBangun=0,0
    for i in range(102):
        if user[i][2]=="jin_pengumpul" :
            totJinkumpul+=1
        elif user[i][2]=="jin_pembangun":
            totJinBangun+=1
    print(f"> Total Jin: {totJinBangun+totJinkumpul}")
    print(f"> Total Jin Pengumpul: {totJinkumpul}")
    print(f"> Total Jin Pembangun: {totJinBangun}")
    totjin=[0 for i in range (100)]
    for i in range(100):
        if candi[i]!=[0,0,0,0,0]:
            for j in range (100):
                if totjin[j]!=0 and totjin[j][0]==candi[i][1]:
                    totjin[j][1]+=1
                    break
            else: 
                for j in range(100):
                    if totjin[j]==0:
                        totjin[j]=[candi[i][1],1]
                        break
    for i in range (100):
        if totjin[i]!=0:
            dibangun=True
            break
    else:dibangun=False
    if dibangun :
        max=totjin[0][1]
        min=totjin[0][1]
        jumlahmax=0
        jumlahmin=0
        for i in range(100):
            if totjin[i]!=0 :
                if max<totjin[i][1]:
                    max=totjin[i][1]
                    jumlahmax=0
                if min>totjin[i][1]:
                    min=totjin[i][1]
                    jumlahmin=0
                if min==totjin[i][1]:
                    jumlahmin+=1
                if max==totjin[i][1]:
                    jumlahmax+=1

        if jumlahmax==0:
            for i in range (100):
                if totjin[i][1]==max:
                    terendah=totjin[i][0] 
                    break
        else:
            for i in range (100):
                if totjin[i]!=0 and  max==totjin[i][1] :
                    terendah=totjin[i][0]
                    break
            for i in range (100):
                if totjin[i]!=0 and  max==totjin[i][1] and totjin[i][0]<terendah:
                    terendah=totjin[i][0]   
        if jumlahmin==0:
            for i in range (100):
                if totjin[i][1]==min:
                    tertinggi=totjin[i][0] 
                    break
        else:
            for i in range (100):
                if totjin[i]!=0 and  min==totjin[i][1] :
                    tertinggi=totjin[i][0]
                    break
            for i in range (100):
                if totjin[i]!=0 and  min==totjin[i][1] and totjin[i][0]>tertinggi:
                    tertinggi=totjin[i][0]      
        print(f"> Jin Terajin: {terendah}")
        print(f"> Jin Termalas: {tertinggi}")
    else:
        print(f"> Jin Terajin: -")
        print(f"> Jin Termalas: -")
    print(f"> Jumlah Pasir: {bahan[0][2]} unit")
    print(f"> Jumlah Air: {bahan[1][2]} unit")
    print(f"> Jumlah Batu: {bahan[2][2]} unit\n")
    
