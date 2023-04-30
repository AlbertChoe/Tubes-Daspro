import sys
def ayamberkokok(candi : list) -> None  :
    print("Kukuruyuk.. Kukuruyuk..\n")
    totCandi = 0
    for i in range (100):
        if candi[i]!=["0","0","0","0","0"]:
            totCandi+=1
    print(f"jumlah candi: {totCandi}\n")
    if totCandi != 100:
        print("Selamat, Roro Jonggrang memenangkan permainan!\n")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
    else:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    sys.exit(1)
