import time

def random_number(counter):
    seed = (1103515245 * counter + 12345) % (2**31)
    return seed % 6
def RNG(): #Fungsi yang dipakai
    counter = int(time.time() * 1000)
    num = random_number(counter)
    return num

#Harus disesuaikan sesuai dengan output yang mau
#kalo untuk bangun random number cuma dari 1 sampai 5
#kalo untuk kumpul random number bisa dari 0 sampai 5
