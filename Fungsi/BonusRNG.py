def LCG(seed:int,multiplier:int,increment:int,modulus:int,n:int)->int:
    if n==0:
        return seed
    else: return (multiplier*LCG(seed,multiplier,increment,modulus,n-1)+increment)%modulus

import time

def RNGKumpul() ->tuple: #yang dipakai untuk generate 3 random number 
    seed = int(time.time()*1000)
    multiplier = 1103515245
    increment = 12345
    modulus = 2**31
    n = 3
    result = [None for i in range (3)]
    for i in range(n):
        time.sleep(0.02)
        seed = LCG(seed, multiplier, increment, modulus, 1)
        random_num = seed % 6
        result[i]=random_num
    return result[0],result[1],result[2]

def RNGBangun() ->tuple: #yang dipakai untuk generate 3 random number 
    seed = int(time.time()*1000)
    multiplier = 1103515245
    increment = 12345
    modulus = 2**31
    n = 3
    result = [None for i in range (3)]
    for i in range(n):
        time.sleep(0.02)
        seed = LCG(seed, multiplier, increment, modulus, 1)
        random_num = (seed %5)+1
        result[i]=random_num
    return result[0],result[1],result[2]