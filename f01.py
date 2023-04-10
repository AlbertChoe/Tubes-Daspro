import CSV_Parser as parser
def login(users,role):
    username=input("Username: ")
    password=input("Password: ")
    for i in range (1,parser.length(users)):
        if users[i]==username:
            for j in range (1,3):
                if password==users[i][j]:
                    print (f'\nSelamat datang, {username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.')
                    role=users[i][j][2]
                    return role
            else:
                print()
                print("Password Salah")
                return
    else:
        print()
        print("Username tidak terdaftar")

