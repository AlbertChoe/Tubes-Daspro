# File: main.py
import CSV_Parser as parser
import f01


# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan
role=0 # 0 =belum login  ; 1=Bondowoso ; 2=Rorojongrang , 3=jin pembangun ,  4=jin pengumpul

users=parser.load("user.csv")
candi=parser.load("candi.csv")
bahan_bangunan=parser.load("bahan_bangunan.csv")

def options(commands):
  global users
  global candi
  global bahan_bangunan
  global role

  if commands=="login":
    if role==0 :
      return f01.login(users)
    
  elif commands=="logout":
    if role==1 or role==2:
      return 0
    
  elif commands=="summonjin":
    if role==1 :
      return 0
  
  elif commands=="hapusjin":
    if role==1 :
      return 
  
  elif commands=="ubahjin":
    if role==1:
      return 0
  
  elif commands=="bangun":
    if role==3:
      return 0
  
  elif commands=="kumpul":
    if role==4:
      return 0
  
  elif commands=="batchkumpul":
    if role==1:
      return 0
  
  elif commands=="batchbangun":
    if role==1:
      return 0
  
  elif commands=="laporanjin":
    if role==1:
      return 0
  
  elif commands=="laporancandi":
    if role==1:
      return 0
  
  elif commands=="hancurkancandi":
    if role==2:
      return 0
  
  elif commands=="ayamberkokok":
    if role==2:
      return 0
  
  elif commands=="save":
    if role==1 or role==2:
      return 0
    
  
  elif commands=="help":
    if role==0:
      return help(0)
    elif role==1:
      return help(1)
    elif role==2:
      return help(2)
    elif role==3:
      return help(3)
    elif role==4:
      return help(4)
  
  
  
#Program yang di run
while True:
  masukan = input(">>> ")
  options(masukan)
