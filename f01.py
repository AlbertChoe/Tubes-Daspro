def login(users):
    username=input("Username: ")
    password=input("Password: ")
    for i in range (1,3):
        if username==users[i][0]:
            if password==users[i][1]:
                print()
                print ("Selamat datang, Bandung!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                return
            else:
                print()
                print("Password Salah")
                return
    else:
        print()
        print("Username tidak terdaftar")

