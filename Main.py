# File: main.py
import Fungsi.f01 as f01
import Fungsi.f02 as f02
import Fungsi.f03 as f03
import Fungsi.f04 as f04
import Fungsi.f05 as f05
import Fungsi.f06 as f06
import Fungsi.f07 as f07
import Fungsi.f08 as f08
import Fungsi.f09 as f09
import Fungsi.f10 as f10
import Fungsi.f11 as f11
import Fungsi.f12 as f12
import Fungsi.f13 as f13
import Fungsi.f14 as f14
import Fungsi.f15 as f15 
import Fungsi.f16 as f16 

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [[0,0,0] for i in range (102)] # Matriks data user awal persen semua (100 jin + bandung + roro)
candi = [[0,0,0,0,0] for i in range (100) ] # Matriks data candi. (maksimal 100 candi)
bahan_bangunan = [[0,0,0] for i in range (3)] # Matriks Data bahan bangunan. (ada pasir, batu sama air )
role=0  #0=belum login
username=0   #0=belum login
file = (users, candi, bahan_bangunan)
fileName = ('user.csv', 'candi.csv', 'bahan_bangunan.csv')
users,candi,bahan_bangunan = f13.load(users,candi,bahan_bangunan)
if bahan_bangunan[0][0]==0:
  bahan_bangunan[0]=["Pasir","Pasir dari palung mariana",0]
  bahan_bangunan[1]=["Batu","Batu dari palung mariana",0]
  bahan_bangunan[2]=["Air","Air dari palung mariana",0]

def options(commands):
  global users
  global candi
  global bahan_bangunan
  global role
  global username
  global jinBangun

  if commands=="login":
    if role==0 :
      role,username= f01.login(users, role)
      return 
    else:
      print("\nSilahkan logout dari account sekarang agar bisa login kembali.\n")
    
  elif commands=="logout":
      role,username=f02.logout(role,username)
      return 
    
  elif commands=="summonjin":
    if role=="bandung_bondowoso" :
      users=f03.summonjin(users)
      return
    else:
      print("\nMaaf kamu tidak memiliki kekuasaan untuk memanggil fungsi ini\n")
  
  elif commands=="hapusjin":
    if role=="bandung_bondowoso" :
      users,candi=f04.hapusjin(users,candi)
      return
    else:
      print("\nMaaf kamu tidak memiliki kekuasaan untuk memanggil fungsi ini\n")
  
  elif commands=="ubahjin":
    if role=="bandung_bondowoso":
      users=f05.ubah(users)
      return 
    else:
      print("\nMaaf kamu tidak memiliki kekuasaan untuk memanggil fungsi ini\n")
  
  elif commands=="bangun":
    if role=="jin_pembangun":
      candi,bahan_bangunan=f06.bangun(candi,bahan_bangunan,username)
      return 
    else:
      print("\nHanya jin pembangun yang dapat membangun candi.\n")
  
  elif commands=="kumpul":
    if role=="jin_pengumpul":
      bahan_bangunan,pasir,batu,air=f07.kumpul(bahan_bangunan)
      return bahan_bangunan
    else:
      print("\nHanya jin pengumpul yang dapat mengumpulkan bahan.\n")
  
  elif commands=="batchkumpul":
    if role=="bandung_bondowoso":
      bahan_bangunan=f08.batchkumpul(users,bahan_bangunan)
      return bahan_bangunan
    else:
      print("\nMaaf kamu tidak memiliki kekuasaan untuk memanggil fungsi ini\n")
  
  elif commands=="batchbangun":
    if role=="bandung_bondowoso":
      bahan_bangunan,candi=f08.batchbangun(users,bahan_bangunan,candi)
      return bahan_bangunan,candi
  
  elif commands=="laporanjin":
    if role=="bandung_bondowoso":
      f09.laporanjin(users,bahan_bangunan,candi)
      return 
  
  elif commands=="laporancandi":
    if role=="bandung_bondowoso":
      f10.laporancandi(candi)
      return 
  
  elif commands=="hancurkancandi":
    if role=="roro_jonggrang":
      f11.hancurkancandi(candi)
  
  elif commands=="ayamberkokok":
    if role=="roro_jonggrang":
      f12.ayamberkokok(candi)
  
  elif commands=="save":
    if role=="bandung_bondowoso" or role=="roro_jonggrang":
      f14.save(file, fileName)
    else:
      print("\nMaaf kamu tidak memiliki kekuasaan untuk memanggil fungsi ini\n")
    
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
  
  elif commands=="exit":
      if role==0:
        f16.exit(file, fileName)
    
  else:print("input tidak valid\n")
  

#Program yang di run
while True:
  # print(users)
  # print(candi)
  # print(bahan_bangunan)
  masukan = input(">>> ").lower()
  options(masukan)
  
