# File: main.py
import CSV_Parser as parser
import f01


# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan

users=parser.load("user.csv")
candi=parser.load("candi.csv")
bahan_bangunan=parser.load("bahan_bangunan.csv")

def options(commands):
  global users
  global candi
  global bahan_bangunan

  if commands=="login":
    return f01.login(users)
  

print(users)
while True:
  masukan = input(">>> ")
  options(masukan)
