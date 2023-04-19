import Fungsi.f14 as f14
import sys

def exit():
    isValid = False
    while(isValid == False):
        jawaban = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if jawaban == 'n' or jawaban == 'N':
            isValid = True
            sys.exit(1) # keluar program
        elif jawaban == 'y' or jawaban == 'Y':
            isValid = True
            f14.save()
        else:
            isValid = False