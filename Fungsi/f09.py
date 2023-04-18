import Fungsi.CSV_Parser as parser

def laporanjin(user,jinPembangun,bahan):
    totJinkumpul=0
    totJinBangun=0
    for i in range(parser.length(user)):
        if user[i][2]=="jin_pengumpul" :
            totJinkumpul+=1
        elif user[i][2]=="jin_pembangun":
            totJinBangun+=1
    print(f"> Total Jin: {totJinBangun+totJinkumpul}")
    print(f"> Total Jin Pengumpul: {totJinkumpul}")
    print(f"> Total Jin Pembangun: {totJinBangun}")
    print(jinPembangun)
    if parser.length(jinPembangun)!=0:
        #sorting algorithm untuk mencari yang terajin dan termales (menggunakan counting sort)
        # Tentukan nilai minimum dan maksimum pada kolom kedua
        minimum = jinPembangun[0][1]
        maksimum = jinPembangun[0][1]
        for i in range(parser.length(jinPembangun)):
            if jinPembangun[i][1] < minimum:
                minimum = jinPembangun[i][1]
            elif jinPembangun[i][1] > maksimum:
                maksimum = jinPembangun[i][1]
        
        # Hitung jumlah kemunculan setiap nilai pada kolom kedua
        counting = [0] * (maksimum - minimum + 1)
        for i in range(parser.length(jinPembangun)):
            counting[jinPembangun[i][1] - minimum] += 1
        
        # Hitung prefix sum pada array counting
        for i in range(1, parser.length(counting)):
            counting[i] += counting[i-1]
        
        # Buat array hasil
        hasil = [0] * parser.length(jinPembangun)
        
        # Lakukan counting sort pada kolom kedua
        for i in range(parser.length(jinPembangun)-1, -1, -1):
            hasil[counting[jinPembangun[i][1] - minimum] - 1] = jinPembangun[i]
            counting[jinPembangun[i][1] - minimum] -= 1
        jinPembangun=hasil
        #untuk mengecek apabila ada jin yang membangun candi dengan jumlah yang sama
        #untuk jin termales
        if hasil[0][1]==hasil[1][1]:
            i=1
            termales=[hasil[0],hasil[1]]
            while i<(parser.length(hasil)-1) and hasil[i][1]==hasil[i+1][1] :
                i+=1
                termales=parser.append(termales,hasil[i])
            # Lakukan iterasi untuk setiap elemen matriks
            maksimum=termales[0][0]
            for x in range(parser.length(termales)):
                if termales[x][0]>maksimum:
                    maksimum=termales[x][0]   
            print(f"termales adalah {maksimum}")
        else:
            print(f"> Jin Termalas: {hasil[0][0]}")

        #untuk jin terajin
        if hasil[parser.length(hasil)-1][1]==hasil[parser.length(hasil)-2][1]:
            i=parser.length(hasil)-2
            terajin=[hasil[i],hasil[i-1]]
            while i>0 and  hasil[i][1]==hasil[i-1][1]:
                i-=1
                terajin=parser.append(terajin,hasil[i])
            minimum=terajin[0][0]
            for x in range(parser.length(terajin)):
                if terajin[x][0]<minimum:
                    minimum=terajin[x][0]  
            print(f"terajin adalah {minimum}")
        else:print(f"> Jin terajin: {hasil[parser.length(hasil)-1][0]}")
    else:
        print("> Jin Terajin: -\n> Jin Termalas: -")
    print(f"> Jumlah Pasir: {bahan[1][2]} unit")
    print(f"> Jumlah Air: {bahan[3][2]} unit")
    print(f"> Jumlah Batu: {bahan[2][2]} unit")
    return jinPembangun