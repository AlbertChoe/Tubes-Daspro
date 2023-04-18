import argparse
import sys
import os
import Fungsi.CSV_Parser as parser

def load():
    parse = argparse.ArgumentParser(usage="python main.py <nama_folder>") 
    parse.add_argument("path")
    if len(sys.argv)==1:
        print("Tidak ada nama folder yang diberikan!")
        sys.exit(1)
    args=parse.parse_args()

    if os.path.exists(args.path):  
        print("Loading...")
        users=parser.load(f"{args.path}/user.csv")
        candi=parser.load(f"{args.path}/candi.csv")
        bahan_bangunan=parser.load(f"{args.path}/bahan_bangunan.csv")
        print("Selamat datang di program “Manajerial Candi”")
        print("Silahkan masukkan username Anda") 
        return users,candi,bahan_bangunan
    else:
        print(f"Folder “{args.path}” tidak ditemukan.")
        sys.exit(1)