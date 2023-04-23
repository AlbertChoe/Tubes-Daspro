import argparse
import sys
import os

def parser(csv,list,token):
    file = open(csv,"r")
    i = -1
    for line in file:
        if i == -1:
            i += 1
            continue
        else:
            h = 0
            temp = ""
            for j in range(len(line)):
                if line[j] == token or line[j] == '\n':
                    list[i][h] = temp
                    temp = ""
                    h += 1
                else:
                    temp += line[j]
            if temp != "":
                list[i][h] = temp
            i += 1
    return list
 
def load(users,candi,bahan_bangunan):
    parse = argparse.ArgumentParser(usage="python main.py <nama_folder>") 
    parse.add_argument("path")
    if len(sys.argv)==1:
        print("Tidak ada nama folder yang diberikan!")
        italic_text = "\x1B[3m" + "python main.py" + "\x1B[0m"
        print(f"\nUsage: {italic_text} <nama_folder>")
        sys.exit(1)

    args=parse.parse_args()
    if os.path.exists(args.path):  
        print("Loading...")
        users=parser(f"{args.path}/user.csv",users,";")
        candi=parser(f"{args.path}/candi.csv",candi,";")
        bahan_bangunan=parser(f"{args.path}/bahan_bangunan.csv",bahan_bangunan,";")
        print("Selamat datang di program “Manajerial Candi”")
        print("Silahkan masukkan username Anda") 
        return users,candi,bahan_bangunan
    else:
        print(f"Folder “{args.path}” tidak ditemukan.")
        sys.exit(1)