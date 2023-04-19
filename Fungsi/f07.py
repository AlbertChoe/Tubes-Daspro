import Fungsi.BonusRNG as RNG
import Fungsi.CSV_Parser as parser
def kumpul(bahan_bangunan):
    pasir,batu,air = RNG.RNGKumpul()
    print("Jin found:", pasir, "sand,", batu, "stone,", air, "water")
    for i in range(1,parser.length(bahan_bangunan)):
        if bahan_bangunan[i][0] == "Pasir":
            bahan_bangunan[i][2] =int(bahan_bangunan[i][2])+ pasir
        elif bahan_bangunan[i][0] == "Batu":
            bahan_bangunan[i][2] = int(bahan_bangunan[i][2]) +batu
        elif bahan_bangunan[i][0] == "Air":
            bahan_bangunan[i][2] = int(bahan_bangunan[i][2]) +air
    return bahan_bangunan,pasir,batu,air