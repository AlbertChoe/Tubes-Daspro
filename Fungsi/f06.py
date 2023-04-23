import Fungsi.BonusRNG as RNG
def bangun(candi,bahan,username):
    pasir,batu,air=RNG.RNGBangun()
    if bahan[0][2] < pasir and bahan[1][2] < batu and bahan[2][2] < air:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
        return candi,bahan
    else:
        counter=0
        for i in range(100):
            if candi[i]==[0,0,0,0,0] :
                break
            else: counter+=1
        if counter != 100:
            candi[counter] = [counter+1, username, pasir, batu, air]
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {100-(counter+1)}")
            for i in range(3):
                if bahan[i][0] == "Pasir":
                    bahan[i][2] = int(bahan[i][2])- pasir
                elif bahan[i][0] == "Batu":
                    bahan[i][2] = int(bahan[i][2])- batu
                elif bahan[i][0] == "Air":
                    bahan[i][2] = int(bahan[i][2])- air
            return candi,bahan
        else:
            #jika candi yang dibangun sudah ada 100
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {0}")
            for i in range(3):
                if bahan[i][0] == "Pasir":
                    bahan[i][2] = int(bahan[i][2])- pasir
                elif bahan[i][0] == "Batu":
                    bahan[i][2] = int(bahan[i][2])- batu
                elif bahan[i][0] == "Air":
                    bahan[i][2] = int(bahan[i][2])- air
            return candi,bahan
