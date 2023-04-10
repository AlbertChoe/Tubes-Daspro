# File: main.py
import CSV_Parser as parser
from Fungsi import f01
from Fungsi import f15 
from Fungsi import f02
from Fungsi import BonusRNG as Random


# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan
jinBangun=[] #Isi jin yang bangun tiap candi
jinKumpul=[] #isi total bahan yang dikumpul tiap jin
role=0  #0=belum login
username=0   #0=belum login

users=parser.load("FileCSV/user.csv")
candi=parser.load("FileCSV/candi.csv")
bahan_bangunan=parser.load("FileCSV/bahan_bangunan.csv")

def options(commands):
  global users
  global candi
  global bahan_bangunan
  global role
  global username
  global jinBangun
  global jinKumpul

  if commands=="login":
    if role==0 :
      role,username=f01.login(users, role)
      return role,username
    
  elif commands=="logout":
      role,username=f02.logout(role,username)
      return role,username
    
    
  elif commands=="summonjin":
    if role=="bandung_bondowoso" :
      return 0
  
  elif commands=="hapusjin":
    if role=="bandung_bondowoso" :
      return 
  
  elif commands=="ubahjin":
    if role=="bandung_bondowoso":
      return 0
  
  elif commands=="bangun":
    if role=="jin_pembangun":
      return 0
  
  elif commands=="kumpul":
    if role=="jin_pengumpul":
      return 0
  
  elif commands=="batchkumpul":
    if role=="bandung_bondowoso":
      return 0
  
  elif commands=="batchbangun":
    if role=="bandung_bondowoso":
      return 0
  
  elif commands=="laporanjin":
    if role=="bandung_bondowoso":
      return 0
  
  elif commands=="laporancandi":
    if role=="bandung_bondowoso":
      return 0
  
  elif commands=="hancurkancandi":
    if role=="roro_jonggrang":
      return 0
  
  elif commands=="ayamberkokok":
    if role=="roro_jonggrang":
      return 0
  
  elif commands=="save":
    if role=="bandung_bondowoso" or role=="roro_jonggrang":
      return 0
    
  
  elif commands=="help":
    if role==0:
      return f15.help(0)
    elif role=="bandung_bondowoso":
      return f15.help("bandung_bondowoso")
    elif role=="roro_jonggrang":
      return f15.help("roro_jonggrang")
    elif role=="jin_pembangun":
      return f15.help("jin_pembangun")
    elif role=="jin_pengumpul":
      return f15.help("jin_pengumpul")
  
  
  
#Program yang di run
while True:
  masukan = input(">>> ")
  options(masukan)
  print(users)
  print(role,username)
