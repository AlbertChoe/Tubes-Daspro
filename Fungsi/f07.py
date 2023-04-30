import Fungsi.BonusRNG as RNG
def kumpul(bahan_bangunan :list) -> list:
    pasir,batu,air = RNG.RNGKumpul()
    print("Jin found:", pasir, "pasir,", batu, "batu,", air, "air")
    for i in range(3):
        if bahan_bangunan[i][0] == "Pasir":
            bahan_bangunan[i][2] =str(int(bahan_bangunan[i][2])+ pasir)
        elif bahan_bangunan[i][0] == "Batu":
            bahan_bangunan[i][2] = str(int(bahan_bangunan[i][2]) +batu)
        elif bahan_bangunan[i][0] == "Air":
            bahan_bangunan[i][2] = str(int(bahan_bangunan[i][2]) +air)
    return bahan_bangunan
