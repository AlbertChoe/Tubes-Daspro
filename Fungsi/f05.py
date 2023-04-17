import random 

# sudah ada users dan variabel bahan_bangunan

def kumpul():
    allowed_users = ["Bondowoso", "Roro"]
    if username in allowed_users or role != "jin_pengumpul":
        print("Hanya jin pengumpul yang dapat mengumpulkan bahan.")
        return None
    pasir = random.randint(0, 5)
    batu = random.randint(0, 5)
    air = random.randint(0, 5)
    print("Jin found:", pasir, "sand,", batu, "stone,", air, "water")
    for i in range(len(bahan_bangunan)):
        if bahan_bangunan[i][0] == "pasir":
            bahan_bangunan[i][2] += pasir
        elif bahan_bangunan[i][0] == "batu":
            bahan_bangunan[i][2] += batu
        elif bahan_bangunan[i][0] == "air":
            bahan_bangunan[i][2] += air
    return None
