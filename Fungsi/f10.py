def laporancandi (candi):
    totCandi,totPasir,totBatu,totAir=0,0,0,0
    harga_total=[0 for i in range (100)]
    for i in range (100):
        if candi[i]!=[0,0,0,0,0]:
            totCandi+=1
            totPasir+=int(candi[i][2])
            totBatu+=int(candi[i][3])
            totAir+=int(candi[i][4])
            harga_total[i]=[int(candi[i][0]),int(candi[i][2])*10000 +int(candi[i][3])*15000 +int(candi[i][4])*7500]
    if totCandi==0:
        print(f"> Total Candi: {totCandi}")
        print(f"> Total Pasir yang digunakan: {totPasir}")
        print(f"> Total Batu yang digunakan: {totBatu}")
        print(f"> Total Air yang digunakan: {totAir}")
        print(f"ID Candi termahal: -")
        print(f"ID Candi termurah: -\n")
    else:
        max=0
        min=200000
        for i in range (100):
            if harga_total[i]!=0 and  harga_total[i][1]>max :
                indeksmax=harga_total[i][0]
                max=harga_total[i][1]
            if harga_total[i]!=0 and  harga_total[i][1]<min :
                indeksmin=harga_total[i][0]
                min=harga_total[i][1]
        print(f"> Total Candi: {totCandi}")
        print(f"> Total Pasir yang digunakan: {totPasir}")
        print(f"> Total Batu yang digunakan: {totBatu}")
        print(f"> Total Air yang digunakan: {totAir}")
        print(f"ID Candi termahal: {indeksmax}")
        print(f"ID Candi termurah: {indeksmin}\n")
    