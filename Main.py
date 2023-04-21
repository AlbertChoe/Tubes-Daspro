# File: main.py
import Fungsi.CSV_Parser as parser
import Fungsi.f01 as f01
import Fungsi.f02 as f02
import Fungsi.f03 as f03
import Fungsi.f04 as f04
import Fungsi.f05 as f05
import Fungsi.f07 as f07
import Fungsi.f08 as f08
import Fungsi.f09 as f09
import Fungsi.f13 as f13
import Fungsi.f14 as f14
import Fungsi.f15 as f15 
import Fungsi.f16 as f16 
import Fungsi.BonusRNG as RNG


# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [[0,0,0] for i in range (102)] # Matriks data user awal persen semua (100 jin + bandung + roro)
candi = [[0,0,0,0,0] for i in range (100) ] # Matriks data candi. (maksimal 100 candi)
bahan_bangunan = [[0,0,0] for i in range (3)] # Matriks Data bahan bangunan. (ada pasir, batu sama air )
jinBangun=[0 for i in range (100)] #Isi jin yang bangun tiap candi kalo diremove ditaruh 0 semua , file cuma dibaca yang bukan 0 () Struktur matriks = [namajin,Totalcandiyangdibuat]
jinKumpul = [0 for i in range(100)]
role=0  #0=belum login
username=0   #0=belum login
file = (users, candi, bahan_bangunan)
fileName = ('user.csv', 'candi.csv', 'bahan_bangunan.csv')

users,candi,bahan_bangunan = f13.load(users,candi,bahan_bangunan)

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
      role,username= f01.login(users, role)
      return 
    else:
      print("\nSilahkan logout dari account sekarang agar bisa login kembali.\n")
    
  elif commands=="logout":
      role,username=f02.logout(role,username)
      return 
  
  elif commands=="exit":
      if role==0:
        f16.exit(file, fileName)
    
  elif commands=="summonjin":
    if role=="bandung_bondowoso" :
      users=f03.summonjin(users)
      return
    else:
      print("\nMaaf kamu tidak memiliki kekuasaan untuk memanggil fungsi ini\n")
  
  elif commands=="hapusjin":
    if role=="bandung_bondowoso" :
      users=f04.hapusjin(users)
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
      jinBangun,bahan_bangunan,candi=f08.batchbangun(users,jinBangun,bahan_bangunan,candi)
      return jinBangun,bahan_bangunan,candi
  
  elif commands=="laporanjin":
    if role=="bandung_bondowoso":
      jinBangun=f09.laporanjin(users,jinBangun,bahan_bangunan)
      return jinBangun
  
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
      f14.save(file, fileName)
    
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
  print(users)
  print(role,username)
  masukan = input(">>> ")
  options(masukan)
  
